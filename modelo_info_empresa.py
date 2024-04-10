# Data science
import pandas as pd
print(f"Pandas: {pd.__version__}")
import numpy as np
print(f"Numpy: {np.__version__}")

# NER
import spacy
print(f'spaCy: {spacy.__version__}')
import spacy
from spacy.matcher import PhraseMatcher

import PrendasDB


empresa = {
    "Nombre de la empresa": "EcoStyle",
    "Sede": "Nueva York, Estados Unidos",
    "Fundación": "2005",
    "Fundadora": "Emily Johnson",
    "Sostenibilidad": "Utiliza materiales orgánicos y reciclados en sus prendas para minimizar el impacto ambiental. Trabaja con proveedores locales que comparten sus valores éticos y ambientales. Se esfuerza por reducir su huella de carbono y promover prácticas de fabricación responsables.",
    "Política de devolución": "EcoStyle ofrece una política de devolución flexible y sin complicaciones. Acepta devoluciones dentro de los 30 días posteriores a la compra, siempre y cuando las prendas estén en condiciones originales y no hayan sido usadas.",
    "Cantidad de empleados": "Más de 200",
    "Roles de empleados": "Diseño. Producción. Ventas. Atención. al cliente",
    "Compromiso comunitario": "Además de su dedicación a la sostenibilidad ambiental, en EcoStyle se comprometen a ser una fuerza positiva en sus comunidades locales. Colaboran con organizaciones benéficas y sin fines de lucro que apoyan causas sociales y ambientales.",
    "Visión empresarial": "La visión en EcoStyle es seguir siendo líderes en moda sostenible y expandir su presencia a nivel global. Quieren inspirar a otras empresas a adoptar prácticas éticas y sostenibles en la industria de la moda, demostrando que es posible crear belleza sin comprometer el planeta ni las personas."
}


# Cargar el modelo de lenguaje de SpaCy
nlp = spacy.load("es_core_news_sm")

# Inicializar el matcher de SpaCy
matcher = PhraseMatcher(nlp.vocab)
empresa_minusculas = dict(map(lambda x: (x[0].lower(), x[1]), empresa.items()))
claves = [k.lower() for k in empresa.keys()]
patterns = list(nlp.pipe(claves))
matcher.add("Descripcion", None, *patterns)

# Función para identificar la prenda y devolver sus características
def identificar_dato(texto):
    doc = nlp(texto)
    matches = matcher(doc)
    for match_id, start, end in matches:
        dato = doc[start:end].text
        caracteristicas = empresa_minusculas.get(dato)
        if caracteristicas:
            return dato, caracteristicas
    return None, None

#Creamos la base de dattos
print()
PrendasDB.crearDB()
PrendasDB.crear_tabla_descripcion(empresa)

print("Prendas creadas:")
prendas = PrendasDB.consultar_ecostyle()
print(prendas)


# Función para obtener las características de la empresa
def obtener_caracteristicas(dato_identificado):
    caracteristicas = empresa_minusculas.get(dato_identificado)
    if caracteristicas is None:
        return "El dato de la empresa no fue encontrado en la base de datos."
    return caracteristicas

# Ejemplo de uso
texto_ejemplo = "Dime la cantidad de empleados de la empresa"
print("El texto de ejemplo es: ", texto_ejemplo)
dato_identificado, caracteristicas = identificar_dato(texto_ejemplo)
if dato_identificado:
    print(f"Caracteristica de la empresa identificada: {dato_identificado}")
else:
    print("No se encontró ningun dato de la empresa que preguntas")

resultado = obtener_caracteristicas(dato_identificado)
print("El resultado de la consulta es: ", resultado)
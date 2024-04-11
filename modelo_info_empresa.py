# NER
import spacy
print(f'spaCy: {spacy.__version__}')
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

def tratamiento_texto():
    """
    Convierte las claves del diccionario a minúsculas y devuelve el diccionario.

    Args:
        None.

    Returns:
        Diccionario con las claves en minúsculas.
    """
    empresa_minusculas = dict(map(lambda x: (x[0].lower(), x[1]), empresa.items()))
    return empresa_minusculas

 

# Función para identificar la prenda y devolver sus características
def identificar_dato(texto):
    """
    Identifica el dato de la empresa en el texto y devuelve sus características.

    Args:
        texto (str): Texto a analizar.

    Returns:
        tuple: (dato_identificado, caracteristicas)
    """
    nlp = spacy.load("es_core_news_sm")
    matcher = PhraseMatcher(nlp.vocab)
    claves = [k.lower() for k in empresa.keys()]
    patterns = list(nlp.pipe(claves))
    matcher.add("Descripcion", None, *patterns)
    doc = nlp(texto)
    matches = matcher(doc)
    for match_id, start, end in matches:
        dato = doc[start:end].text
        return dato, tratamiento_texto().get(dato)
    return None, None


#Creamos la base de dattos
print()
PrendasDB.crearDB()
PrendasDB.crear_tabla_descripcion(empresa)

# Función para obtener las características de la empresa
def obtener_caracteristicas(dato_identificado):
    """
    Obtiene las características del dato de la empresa a partir del diccionario.

    Args:
        dato_identificado (str): Dato de la empresa.

    Returns:
        str: Descripción del dato o mensaje de error.
    """
    caracteristicas = tratamiento_texto().get(dato_identificado)
    if caracteristicas is None:
        return "El dato de la empresa no fue encontrado en la base de datos."
    return caracteristicas


# Ejemplo de uso
texto_ejemplo = "Quiero saber la política de devolución de EcoStyle"
print(f"\nTexto de ejemplo: {texto_ejemplo}")

dato_identificado, caracteristicas = identificar_dato(texto_ejemplo)

if dato_identificado:
    print(f"\nDato de la empresa identificado: {dato_identificado}")
    print(f"\nCaracterísticas: {caracteristicas}")
else:
    print("\nNo se encontró ningún dato de la empresa que preguntas")

resultado = obtener_caracteristicas(dato_identificado)
print(f"\nResultado de la consulta: {resultado}")

# Liberias de datos
import pandas as pd
print("Las librerias implementadas:")
print(f"Pandas: {pd.__version__}")
import numpy as np
print(f"Numpy: {np.__version__}")
import os

# Deep Learning 
import tensorflow as tf
print(f"Tensorflow: {tf.__version__}")
import sklearn
print(f"Sklearn: {sklearn.__version__}")

# NER
import spacy
print(f'spaCy: {spacy.__version__}')
import random
from spacy.training.example import Example

# BER
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

#DB SQL
import PrendasDB

# KNN y Encoding
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


# Frases de entrenamiento
data = [
    "Quisiera comprar una camiseta.",
    "Me gustaría pedir una camiseta.",
    "Necesito una camiseta nueva.",
    "Quiero una camiseta de algodón.",
    "Estoy buscando una camiseta en talla grande.",
    "Deseo comprar una camiseta con estampado.",
    "¿Puedo pedir una camiseta en color azul?",
    "Necesitaría una camiseta de manga corta.",
    "Estoy interesado en una camiseta deportiva.",
    "Quiero comprar una camiseta para correr.",
    "Me gustaría adquirir una camiseta negra.",
    "Necesito una camiseta para un regalo.",
    "Deseo pedir una camiseta en talla mediana.",
    "¿Podría tener una camiseta en oferta?",
    "Estoy buscando una camiseta con cuello en V.",
    "Quiero una camiseta personalizada.",
    "Quisiera ordenar una camiseta para el verano.",
    "Necesito una camiseta resistente al desgaste.",
    "Quiero adquirir un pantalón.",
    "¿Podría comprar unos zapatos?",
    "¿Tienes camisetas de mi talla?",
    "Estoy interesado en unos pantalones vaqueros.",
    "Busco una camiseta bonita.",
    "Quiero comprar ropa.",
    "Necesito una camiseta de manga corta para este verano.",
    "Quiero unos pantalones calentitos para el invierno.",
    "¿Hay zapatos de la talla 45?",
    "Estoy buscando una chaqueta a juego con mi outfit.",
    "Camiseta de manga larga.",
    "Necesito ropa para renovar mi armario.",
    "¿Puedo comprar una chaqueta bonita?",
    "Hay camisetas azules.",
    "Quiero obtener unos pantalones de esta marca.",
    "Quiero conseguir una chaqueta que me proteja bien del frío.",
    "Mi deseo es obtener una camiseta de tirantes.",
    "Comprar pantalón rojo.",
    "Buenas, me gustaría una camiseta negra básica.",
    "Quiero comprar una camiseta roja en talla S.",
    "Estoy interesado en adquirir unos pantalones negros.",
    "Deseo comprar un vestido azul en talla M.",
    "Necesito comprar una chaqueta gris.",
    "¿Cuánto cuesta una camisa verde en talla L?",
    "¿Tienes sudaderas en negro?",
    "Busco una falda azul.",
    "Estoy buscando un jersey blanco.",
    "Quiero comprar un abrigo gris.",
    "¿Tienes shorts en azul?",
    "¿Puedo comprar una bufanda verde?",
    "¿Dónde puedo comprar un gorro rojo?",
    "¿Tienes chalecos en negro?",
    "¿Dónde puedo comprar un traje blanco?",
    "¿Hay blusas azules disponibles?",
    "¿Dónde puedo encontrar ponchos verdes?",
    "Quiero comprar un cinturón negro.",
    "¿Venden calcetines rojos?",
    "¿Cuál es el precio de las camisetas rojas?",
    "¿Tienen vestidos azules disponibles?",
    "Necesito un pantalón de trabajo resistente.",
    "¿Tienen descuentos en camisetas de manga larga?",
    "Quiero ver los chalecos de lana que tienen.",
    "Busco una camisa de algodón 100%.",
    "¿Qué estilos de faldas tienen?",
    "Necesito una sudadera con capucha.",
    "¿Tienen abrigos en talla grande?",
    "Busco una camiseta con estampado gráfico.",
    "¿Cuál es el precio de este pantalón de mezclilla?",
    "Me interesa un chaleco acolchado para el frío.",
    "¿Tienen camisas de manga corta en oferta?",
    "Estoy buscando una falda para una ocasión especial.",
    "¿Qué colores de sudaderas tienen en stock?",
    "¿Cuánto cuesta este abrigo de piel?",
    "¿Tienen camisetas de equipos deportivos?",
    "Quiero un pantalón cómodo para estar en casa.",
    "¿Qué tipos de chalecos venden?",
    "Busco un abrigo elegante para salir.",
    "¿Tienen camisas formales para hombres?",
    "Estoy buscando una falda de verano ligera.",
    "¿Tienen sudaderas sin capucha?",
    "¿Cuál es el precio de los pantalones de vestir?",
    "Quiero ver la colección de abrigos para niños.",
    "¿Tienen camisetas de algodón orgánico?",
    "Busco un pantalón con bolsillos laterales.",
    "¿Qué modelos de chalecos para mujer tienen?",
    "Necesito un abrigo resistente a la lluvia.",
    "¿Tienen camisas a cuadros?",
    "Me gustaría una falda plisada.",
    "¿Qué talla de sudaderas tienen?",
    "Estoy buscando un pantalón de colores vivos.",
    "¿Tienen chalecos reflectantes?",
    "Quiero un abrigo largo hasta los tobillos.",
    "¿Tienen camisas de seda?",
    "Busco una falda con bolsillos.",
    "¿Qué estampados tienen para sudaderas?",
    "Necesito un pantalón para hacer ejercicio.",
    "¿Tienen chalecos térmicos?",
    "Quiero una camiseta para correr."
]

# Diccionario de entidades con categorías de prendas y colores
entidades = {
    "prenda": [
        "camiseta", "camisetas",
        "pantalón", "pantalones",
        "camisa", "camisas",
        "suéteres", "suéter",
        "chaqueta", "chaquetas",
        "falda", "faldas",
        "vestido", "vestidos",
        "sudadera", "sudaderas",
        "jersey", "jerséis",
        "abrigo", "abrigos",
        "shorts",
        "blusa", "blusas",
        "accesorios",
        "bufanda", "bufandas",
        "gorro", "gorros",
        "chaleco", "chalecos",
        "zapato", "zapatos",
        "poncho", "ponchos",
        "sombrero", "sombreros",
        "cinturón", "cinturones",
        "calcetín", "calcetines"
    ],
    # Lista de colores disponibles
    # "color": [
    #     "rojo", "rojos",
    #     "roja", "rojas",
    #     "azul", "azules",
    #     "negro", "negros",
    #     "negra", "negras",
    #     "verde", "verdes",
    #     "gris", "grises",
    #     "blanco", "blancos", 
    #     "blanca", "blancas", 
    #     "amarillo", "amarillos",
    #     "amarilla", "amarillas",
    #     "rosa", "rosas",
    #     "marrón", "marrones",
    #     "naranja", "naranjas",
    #     "celeste", "celestes",
    #     "añil", "añiles",
    #     "morado", "morados",
    #     "morada", "moradas"
    # ]
}

# Cargar spaCy
nlp = spacy.load("es_core_news_sm")

# Definir la lista para almacenar los datos procesados
training_data = []

# Iterar sobre cada frase y generar los datos de entrenamiento
for utterance in data:
    doc = nlp(utterance)  # Procesar la frase con spaCy
    entities = []  # Lista para almacenar las entidades encontradas en la frase
        
    # Iterar sobre cada palabra en la frase
    for token in doc:
        # Buscar si la palabra está presente en alguna de las listas de entidades
        for label, keywords in entidades.items():
            if token.text.lower() in keywords:
                # Agregar la entidad encontrada al formato requerido por spaCy
                entities.append((token.idx, token.idx + len(token.text), label))
        
    # Almacenar los datos de la frase junto con las entidades encontradas
    training_data.append((utterance, {'entities': entities}))
    TRAINING_DATA = training_data

def obtener_entidades(texto):

        # Inicializar un modelo de SpaCy
    nlp = spacy.blank("es")

    # Crear el pipeline de reconocimiento de entidades
    ner = nlp.add_pipe("ner")

    # Añadir las etiquetas al pipeline
    ner.add_label("PRENDA")

    # Inicializar el optimizador
    optimizer = nlp.begin_training()

    # Entrenar el modelo
    for epoch in range(10):
        random.shuffle(TRAINING_DATA)
        losses = {}
        for text, annotations in TRAINING_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.5, losses=losses)
        print()
        print("Entrenando modelo...")
        print(losses)

    # Obtener la ruta del modelo de Spacy en el mismo directorio
    directorio_actual = os.path.dirname(os.path.realpath(__file__))
    ruta_modelo_spacy = os.path.join(directorio_actual, "modelo_entrenado_spacy")

    # Cargar el modelo de Spacy
    nlp = spacy.load(ruta_modelo_spacy)
    
    # Procesar el texto con el modelo entrenado
    doc = nlp(texto)
    
    # Inicializar el modelo de question-answering
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
    
    # Definir las preguntas para obtener la talla y el color
    preguntas = ["¿Cuál es la talla?", "¿Cuál es el color?"]
    
    # Obtener las respuestas utilizando el modelo de question-answering
    respuestas = qa_model(question=preguntas, context=texto)
    
    # Extraer las entidades del texto procesado por spaCy
    entidades = [ent.text for ent in doc.ents]
    
    # Devolver un diccionario con las entidades extraídas
    return {
        "prenda": entidades[0] if entidades else None,
        "color": respuestas[1]["answer"] if respuestas else None,
        "talla": respuestas[0]["answer"] if respuestas else None
    }


# Base de datos
PrendasDB.crearDB()
PrendasDB.crear_prendas()
prendas = PrendasDB.leer_prendas()
print(prendas)

# Pasamos de SQL a pandas
query = '''
        SELECT * 
        FROM StockPrendas
        '''
df = PrendasDB.sql_query(query)
data= df.drop(columns='id_prenda')

#Normalizamos datos
prenda = data['prenda']
color = data['color']
talla = data['talla']

# Convert strings to lowercase
prenda = [str(p).lower() for p in prenda]
color = [str(c).lower() for c in color]

# Create the DataFrame
df = pd.DataFrame({'prenda': prenda, 'color': color, 'talla': talla})


#Entrenamos el modelo de KNN
# Copia del DataFrame original para evitar cambios
df_encoded = df.copy()

# Inicializar el codificador de etiquetas para cada característica
label_encoders = {}

# Iterar sobre cada columna y aplicar el LabelEncoder
for column in df_encoded.columns:
    label_encoders[column] = LabelEncoder()
    df_encoded[column] = label_encoders[column].fit_transform(df_encoded[column])

# Crear una nueva columna 'ID' con IDs únicos para cada registro
df_encoded['ID'] = range(len(df_encoded))

# Datos de entrada para el KNN
X = df_encoded[['prenda', 'talla', 'color']]
y = df_encoded['ID']  # ID como variable objetivo

# Crear y entrenar el clasificador KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)



# Ejemplo de uso
texto_ejemplo = "Quiero un pantalón azul de la talla S"
entidades = obtener_entidades(texto_ejemplo)
print()
print("Ejemplo de uso")
print('Las entidades son: ', entidades)

# Limpiar los valores y formatearlos adecuadamente
prenda = entidades['prenda'].strip() # Eliminar espacios en blanco al principio y al final
color = entidades['color'].strip()  # Eliminar espacios en blanco al principio y al final
talla = entidades['talla'].strip().upper().replace(".", "")  # Convertir a mayúsculas y eliminar espacios en blanco

# Crear el DataFrame
nueva_entrada = pd.DataFrame({'prenda': [prenda], 'talla': [talla], 'color': [color]})

# Mostrar el DataFrame resultante
print('Este es el dataframe resultante: ', nueva_entrada)

# Codificar la nueva entrada usando los mismos codificadores de etiquetas utilizados en el conjunto de entrenamiento
for column in nueva_entrada.columns:
    nueva_entrada[column] = label_encoders[column].transform(nueva_entrada[column])

# Realizar la predicción
prediccion = knn.predict(nueva_entrada)

# Mostrar el ID predicho
print("ID predicho para la nueva entrada:", df.iloc[prediccion[0]])

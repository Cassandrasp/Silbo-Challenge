# Silbo-Challenge

Descripción breve del proyecto.

### **Requisitos previos**
Python => 3.7


### **1. Instalación**
1. Clona este repositorio.

	`git clone https://github.com/Cassandrasp/Silbo-Challenge.git`
	
2. Instala las dependencias: 

	`pip install -r requirements.txt`.

~~3. Ejecuta `python app.py` para iniciar la aplicación.~~ (API en proceso)

### **2. Estructura del proyecto** 
Sin estructura definida hasta el momento (es el repo sucio). Se están integrando todos los modelos en la api para crear todo el flujo, mientras tanto, una guía para verlos de forma individual. 

**Datos**
-	Conjunto de datos con las frases de entrenamiento para el modelo de intenciones

	`/data/icm_dataset.csv`

**Modelos**
- **Modelo de intención:** Ejecutar desde la rama `modelo_entrenado_bert` el notebook `bert_modelo.ipynb`
	Para realizar nuevas predicciones, en la última celda, modifica la frase que deseas utilizar para probar el modelo entrenado.

	- **Flujo compra** (desde la rama `main`):
		- **Extracción de entities** (talla, prenda y color): Ejecutar `Modelo_compra.ipynb`. Para probarlo, modificar la frase de la última celda.
		- **KNN:** Para extraer una propuesta de prenda a partir de las entities y la base de datos (PrendasDB.db). Ejecutar `knn.ipynb` (Error al importar PrendasDB)

	- **Modelo información de producto:** Desde la rama `main` ejecutar `modelo_info_producto.ipynb` (Error al importar PrendasDB)

	- **Modelo de información de empresa** (en proceso)

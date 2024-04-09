from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import DataLoader, TensorDataset

'''

Para Probar: escribir "python api.py" en terminal y dejarlo.
Despues para probar diferentes textos: ABRIR Command Prompt
Escribir: curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"Quiero información de este pantalon\"}" http://127.0.0.1:5000/v1/intention
Cambiar frase a lo que quieras

'''

app = Flask(__name__)

# Inicializar tokenizer
tokenizer = BertTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased", do_lower_case=False)

# Inicializar y cargar el modelo
model = BertForSequenceClassification.from_pretrained("dccuchile/bert-base-spanish-wwm-cased", num_labels=3)
model.eval()  

# Inicializar label encoder 
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('label_encoder_classes.npy', allow_pickle=True)


@app.route('/v1/intention', methods=['POST'])
def predict_intention():
    data = request.json
    text = data.get('text', '')

    # Predicir intention
    prediction = predict_single_text(text)
    
    # Convertir NumPy int64 to Python int para jsonify 
    if isinstance(prediction, np.int64):
        prediction = int(prediction)

    # Mapear prediccion a su endpoint
    endpoint_mapping = {
        1: '/v1/comprar',
        2: '/v1/info/producto',
        3: '/v1/info/empresa'
    }
    target_endpoint = endpoint_mapping.get(prediction, 'Error: Invalid prediction')
    return jsonify({'prediction': prediction, 'target_endpoint': target_endpoint})

def predict_single_text(text):
    inputs = tokenizer(text, truncation=True, padding=True, max_length=128, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_label_idx = torch.argmax(logits, dim=1).item()
        predicted_label = label_encoder.inverse_transform([predicted_label_idx])[0]
    return predicted_label

if __name__ == '__main__':
    app.run(debug=True)

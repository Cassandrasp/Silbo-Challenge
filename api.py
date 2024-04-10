from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import torch
from fastapi.responses import JSONResponse

'''
En el terminal escribe: uvicorn api:app --reload
Despues, hay que ir a http://127.0.0.1:8000 o http://127.0.0.1:8000/docs (de alli puedes probar textos)

'''

class Item(BaseModel):
    text: str

app = FastAPI()

# Inicializar tokenizer
tokenizer = BertTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased", do_lower_case=False)

# Inicializar y cargar model
model = BertForSequenceClassification.from_pretrained("dccuchile/bert-base-spanish-wwm-cased", num_labels=3)
model.eval()  # Set the model to evaluation mode

# Initicializar label encoder 
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('label_encoder_classes.npy', allow_pickle=True)

@app.post("/v1/intention/")
async def predict_intention(item: Item):
    text = item.text
    print(f"Received text: {text}") 

    # Predicir intention
    prediction = predict_single_text(text)
    prediction_int = int(prediction) 

    # Map prediccion a su endpoint 
    endpoint_mapping = {
        1: '/v1/comprar',
        2: '/v1/info/producto',
        3: '/v1/info/empresa'
    }
    target_endpoint = endpoint_mapping.get(prediction_int, 'Error: Invalid prediction')

    return JSONResponse(content={'prediction': prediction_int, 'target_endpoint': target_endpoint},
                        headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


def predict_single_text(text: str):
    inputs = tokenizer(text, truncation=True, padding=True, max_length=128, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_label_idx = torch.argmax(logits, dim=1).item()
        predicted_label = label_encoder.inverse_transform([predicted_label_idx])[0]
    return predicted_label


'''
Codigo para cuando tengamos los nuevos modelos y queramos adjustar este API:
def comprar():
    # code for "comprar" intention
    return "Handling comprar action"

def producto_info():
    # code for product information request
    return "Providing product information"

def empresa_info():
    # code for company information request
    return "Providing company information"


@app.route('/v1/intention', methods=['POST'])
def predict_intention():
    data = request.json
    text = data.get('text', '')

    prediction = predict_single_text(text)
   
    if isinstance(prediction, np.int64):
        prediction = int(prediction)

    Directly call the appropriate function based on the prediction
    if prediction == 1:
        response = handle_comprar()
    elif prediction == 2:
        response = handle_producto_info()
    elif prediction == 3:
        response = handle_empresa_info()
    else:
        response = 'Error: Invalid prediction'

    return jsonify({'prediction': prediction, 'response': response})
'''

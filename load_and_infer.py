import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
import os
import joblib  

'''
Para usar, hay que escribir en powershell terminal: 
python load_and_infer.py
'''

model_path = "C:\\Users\\dusti\\Documents\\Silbo\\beto\\model_save"

# Load model
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# encoder
label_encoder_path = os.path.join(model_path, "label_encoder.pkl")
label_encoder = joblib.load(label_encoder_path)

# Function: intent 
def predict_intent(frase):
    inputs = tokenizer(frase, padding=True, truncation=True, max_length=128, return_tensors="pt")   #pt = pytorch

    # predict
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_label_id = logits.argmax().item()
    predicted_label = label_encoder.inverse_transform([predicted_label_id])[0]
    return predicted_label

# ejemplo
frase = "Quiero información sobre la camisa azul"
predicted_intent = predict_intent(frase)
print(f"Predicted intent: {predicted_intent}")


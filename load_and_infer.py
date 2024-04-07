import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
import os
import joblib  # Assuming label_encoder is saved with joblib

'''
Para usar, hay que escribir en powershell terminal: 
python load_and_infer.py
'''


# Specify the path where your model and other artifacts are saved
model_path = "C:\\Users\\dusti\\Documents\\Silbo\\beto\\model_save"

# Load the model
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Assuming the label_encoder is saved as a .pkl file in the same directory
label_encoder_path = os.path.join(model_path, "label_encoder.pkl")
label_encoder = joblib.load(label_encoder_path)

# Function to predict the intent of a sentence
def predict_intent(frase):
    # Tokenize input 
    inputs = tokenizer(frase, padding=True, truncation=True, max_length=128, return_tensors="pt")   #pt = pytorch

    # Predict
    with torch.no_grad():
        logits = model(**inputs).logits

    # Get predicted label ID
    predicted_label_id = logits.argmax().item()

    # Decode label ID back to label name
    predicted_label = label_encoder.inverse_transform([predicted_label_id])[0]
    return predicted_label

# Example usage
frase = "Quiero informacion sobre la camiseta azul"
predicted_intent = predict_intent(frase)
print(f"Predicted intent: {predicted_intent}")


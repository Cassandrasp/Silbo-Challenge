import streamlit as st
import requests

# URL de tu API FastAPI
API_URL = 'http://127.0.0.1:8000'  

def send_text_to_api(text):
    endpoint = f"{API_URL}/v1/intention/"
    response = requests.post(endpoint, json={"text": text})
    return response.json()

# Configurar la interfaz de usuario de Streamlit
st.title('Silbo')

# Recoger el texto de entrada del usuario
text_input = st.text_input('Enter Text:', '')

# Enviar el texto a la API cuando se presiona el botón
if st.button('Predict'):
    if text_input:
        result = send_text_to_api(text_input)
        prediction = result['prediction']
        target_endpoint = result['target_endpoint']
        st.write(f"Prediction: {prediction}")
        st.write(f"Target Endpoint: {target_endpoint}")

        # Redirigir al endpoint correspondiente
        if target_endpoint != 'Error: Invalid prediction':
            st.write(f"Redirecting to endpoint: {target_endpoint}")
            st.experimental_rerun()  # Recargar la aplicación con el nuevo endpoint
    else:
        st.warning('Please enter text to predict.')

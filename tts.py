import os
import shutil
from gradio_client import Client

# Obtén el directorio actual del script
current_directory = os.path.dirname(__file__)

# Ruta del archivo de texto
texto_file_path = os.path.join(current_directory, "input.txt")

# Lee el contenido del archivo de texto
with open(texto_file_path, "r", encoding="utf-8") as texto_file:
    texto = texto_file.read()

# Inicializa el cliente de Gradio
client = Client("https://huggingface.co/spaces/k2-fsa/text-to-speech")
result = client.predict(
    "Spanish",    
    'csukuangfj/vits-piper-es_MX-ald-medium',
    #"csukuangfj/vits-piper-es_ES-sharvard-medium",    
    texto,    
    0,
    1.3,
    api_name="/process"
)

# Nombre del archivo de audio de salida
audio_file_name = "audio_salida.wav"
audio_file_path = os.path.join(current_directory, audio_file_name)

# Copia el archivo de audio desde la ubicación temporal al directorio actual
shutil.copyfile(result[0], audio_file_path)

# Elimina el archivo temporal
os.remove(result[0])

print("El archivo de audio se ha guardado en:", audio_file_path)
print(result[1]) # Imprime la respuesta restante

from openai import OpenAI
from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.audio.transcriptions.create(
    model='whisper-1',
    file=open('output.mp3', 'rb'),
    response_format='text',
    language='pt',  # Define o idioma do áudio, pode ser 'en', 'pt', 'es', etc.
    prompt='Transcreva o áudio de forma clara e precisa.',  # Instruções para o modelo
    temperature=0.0  # Define a aleatoriedade da transcrição, 0.0 para transcrições mais precisas e consistentes.
)

print(response)
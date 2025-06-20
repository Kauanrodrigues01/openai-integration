from openai import OpenAI
from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.audio.speech.create(
    model='gpt-4o-mini-tts',
    voice='onyx',
    instructions='Gere um áudio amigável e envolvente. Fale de forma mais natural e humana possível.', # Instruções para o modelo, só disponível para o modelo gpt-4o-mini-tts
    input='Olá, mundo! Esta é uma demonstração de geração de áudio com a OpenAI.',
    response_format='mp3'
)

response.write_to_file('output.mp3')
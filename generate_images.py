import base64
from openai import OpenAI
from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(
    api_key=OPENAI_API_KEY
)

response = client.images.generate(
    model='dall-e-3',
    prompt='A futuristic city skyline at sunset, with flying cars and neon lights',
    n=1,  # Número de imagens a serem geradas
    response_format='b64_json',  # Formato da resposta como base64 JSON, tem tambem a opção 'url' para retornar URLs das imagens
    size='1024x1024',  # Tamanho da imagem gerada
    quality='standard'
)

image_bytes = base64.b64decode(response.data[0].b64_json)
with open('futuristic_city-2.png', 'wb') as image_file:
    image_file.write(image_bytes)

print("Image generated and saved as 'futuristic_city.png'.")

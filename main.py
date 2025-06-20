from openai import OpenAI
from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY')


client = OpenAI(
    api_key=OPENAI_API_KEY
)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    max_tokens=100,  # Define o número máximo de tokens na resposta.
    temperature=0.7,  # Define a aleatoriedade da resposta. Valores mais altos tornam as respostas mais variadas.
    top_p=1.0,  # Define a probabilidade cumulativa para amostragem. Valores mais altos permitem mais diversidade.
    frequency_penalty=0.0,  # Penaliza repetições frequentes de palavras. Valores mais altos reduzem repetições.
    presence_penalty=0.0,  # Penaliza a presença de novas palavras. Valores mais altos incentivam a inclusão de novas palavras.
    messages=[
        {
            'role': 'system', # Mensagem de sistema que define o comportamento do modelo.
            'content': [  # Lista de mensagens que o modelo deve seguir.
                {'type': 'text', 'text': 'Sempre responda com um código em java.'},
                {'type': 'text', 'text': 'Sempre responda de forma amigável.'},
            ]
        },
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'Faça um código que imprima "Olá, mundo!"'}
            ]
        }
    ],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
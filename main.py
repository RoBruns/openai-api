import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
        messages=[
                {
                    "role": "system",
                    "content": "Listar apenas os nomes dos produtos, sem considerar descrição." # noqa
                },
                {
                    "role": "user",
                    "content": "Liste 3 produtos sustentáveis"
                }
        ],
        model="gpt-3.5-turbo-1106"
)


print(resposta.choices[0].message.content)

import os
from langchain.chat_models import ChatOpenAI

MODEL = os.environ.get("MODEL", "gpt-3.5-turbo")
TEMPERATURE = float(os.environ.get("TEMPERATURE", 0.7))
PROMPT = os.environ.get("PROMPT", "")

if PROMPT == "":
    os._exit(0)

chat_model = ChatOpenAI(
    model=MODEL,
    temperature=TEMPERATURE,
)
response = chat_model.predict(PROMPT)

print(response)

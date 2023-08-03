import os
import uuid
from langchain.chat_models import ChatOpenAI

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)


def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)


def main():
    model = os.environ.get("MODEL", "gpt-3.5-turbo")
    temperature = float(os.environ.get("TEMPERATURE", 0.7))
    prompt = os.environ.get("PROMPT", "")

    if prompt == "":
        return

    chat_model = ChatOpenAI(
        model=model,
        temperature=temperature,
    )
    response = chat_model.predict(prompt)

    set_multiline_output("output", response)


if __name__ == "__main__":
    main()

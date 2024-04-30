import ollama

MODEL = "llama3:instruct"

SYSTEM_PROMPT = """
    You are a translator. You need to translate the text which provided by user to chinese language.
    If the text is chinese language, response will be the same as the input.
    Always remember to response in chinese language.
"""

def translator(text):
    reponse = ollama.chat(MODEL, messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": text
        }
    ])
    return reponse['message']['content']


# example_text = "hello world"
# print(translator(example_text))
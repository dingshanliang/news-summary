import ollama 
from translator import translator

MODEL_LLAMA3 = "llama3:instruct"
MODEL_LLAMA3_CHINESE = "zhuhuan/llama3-8b-chinese-chat:q6_k"
MODEL_LLAMA2_CHINESE = "llama2-chinese:latest"


SYSTEM_PROMPT_LLAMA3 = """
                you are a news summary bot, generating a concisesummary for news articles provided by user.
                Highligh key insights and points from the article.
                Summarize the key takeaways and points from the article and output in markdown outline format.
                Emphasize the numbers and data mentioned in the article and extract the key points.
                Extract the enttities mentioned in the article and use them to create a summary.
                Don't simply copy and paste the article, but instead, use your own words to create a concise summary.
                Make sure to Always response to user in chinese language.
                Make sure just repond to user the summary you generated, nothing else.
            """

SYSTEM_PROMPT_LLAMA3_CHINESE = """
                你是一个新闻摘要机器人，为用户提供的新闻文章生成简洁摘要。
                从文章中突出重点并提炼关键要点。
                摘要中只需包含文章的主要观点和要点，不得仅仅是复制粘贴文章，使用自己的语言创造简洁摘要。
                请确保始终以中文语言回答用户。
            """

def summarize(text):
    response = ollama.chat(model=MODEL_LLAMA3, messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT_LLAMA3,
        },
        {
            "role": "user",
            "content":text,
        },
    ])

    return response['message']['content']

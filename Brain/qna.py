fileopen=open("Data\\api.txt","r")
api=fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv

openai.api_key = api
load_dotenv()
completion=openai.Completion()

def questionsAnswers(question,chat_log=None):
    fileLog=open("Database\\qna_log.txt", "r")
    chat_log_template=fileLog.read()
    fileLog.close()

    if chat_log==None:
        chat_log=chat_log_template

    prompt=f'{chat_log}Question: {question}\n Answer: '
    response=completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer=response['choices'][0]['text'].strip()
    chat_log_template_update=chat_log_template+f'\nQuestion: {question}\nAnswer: {answer}'
    fileLog=open("Database\\qna_log.txt", "w")
    fileLog.write(chat_log_template_update)
    fileLog.close()
    return answer

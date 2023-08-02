from config import *
from pyrogram import Client, filters
import openai
import json
import re

client = Client('telepython', api_id, api_hash)

print('Script started!')

openai.api_key = "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"

messages = [
    {"role": "system",
     "content": "you answer short and clear, if you are asked to give a short answer you will make the answer as short as possible"},
]


def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


def get_response(messages):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response['choices'][0]['message']['content']


@client.on_message(filters.regex('prompt'), filters.me)
def ai_text(client, message):
    global messages
    iteration = 0
    for i in client.get_chat_history(message.chat.id):
        iteration += 1
        if iteration == 1:
            with open('data.json', 'w', encoding='utf-8') as file:
                file.write(str(i))
            break

    with open('data.json', 'r', encoding='utf-8') as file:
        last_message = json.loads(file.read())

    text = re.sub('prompt ', '', last_message.get('text'))

    try:
        user_input = text + ' дай максимально короткий ответ'

        messages = update(messages, "user", user_input)

        model_response = get_response(messages)

        client.send_message(message.chat.id, model_response)

        messages = update(messages, "assistant", model_response)

    except:
        client.send_message(message.chat.id, 'Не удалось обработать запрос')


@client.on_message(filters.regex('help') & filters.me)
def help(client, message):
    try:
        client.send_message(message.chat.id, help_message)

    except:
        print('Не удалось обработать запрос')


@client.on_message(filters.regex('send') & filters.me)
def scripting(client, message):
    def go(arg):
        client.send_message(message.chat.id, arg)
    iteration = 0
    for i in client.get_chat_history(message.chat.id):
        iteration += 1
        if iteration == 2:
            with open('data.json', 'w', encoding='utf-8') as file:
                file.write(str(i))
            break

    with open('data.json', 'r', encoding='utf-8') as file:
        script_for_exe = json.loads(file.read())

    try:
        client.send_message(message.chat.id, exec(script_for_exe.get('text')))

    except:
        print('Не удалось обработать запрос')



@client.on_message(filters.regex('calc') & filters.me)
def scripting(client, message):
    iteration = 0
    for i in client.get_chat_history(message.chat.id):
        iteration += 1
        if iteration == 2:
            with open('data.json', 'w', encoding='utf-8') as file:
                file.write(str(i))
            break

    with open('data.json', 'r', encoding='utf-8') as file:
        script_for_exe = json.loads(file.read())

    try:
        client.send_message(message.chat.id, eval(script_for_exe.get('text')))

    except:
        client.send_message(message.chat.id, 'Не удалось обработать запрос')


client.run()

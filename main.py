from config import *
from pyrogram import Client, filters
import json


client = Client('telepython', api_id, api_hash)


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

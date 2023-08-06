from config import *
from pyrogram import Client, filters
import json
import re

client = Client('chervi_broo', api_id, api_hash)

print('Script started!')


@client.on_message(filters.regex('Life Could Be A Dream'))
def lcbad(client, message):
    try:
        client.send_video(message.chat.id, 'All_chervi//lcbad.gif', reply_to_message_id=message.id)
    except:
        client.send_message(message.chat.id, 'Не удалось обработать запрос')


@client.on_message(filters.regex('chervi'))
def chervi(client, message):
    if 'говорят' in message.text:
        try:
            client.send_video(message.chat.id, 'All_chervi/chervi_govorit.gif')
        except:
            client.send_message(message.chat.id, 'Не удалось обработать запрос')
    elif 'армстронг' in message.text:
        try:
            client.send_photo(message.chat.id, 'All_chervi/chervi_armstrong.jpg')
        except:
            client.send_message(message.chat.id, 'Не удалось обработать запрос')
    elif 'sigma' in message.text:
        try:
            client.send_photo(message.chat.id, 'All_chervi/chervi_sigma.jpg')
        except:
            client.send_message(message.chat.id, 'Не удалось обработать запрос')
    elif 'цзлсузша' in message.text:
        try:
            client.send_photo(message.chat.id, 'All_chervi/chervi_emu.jpg')
        except:
            client.send_message(message.chat.id, 'Не удалось обработать запрос')
    elif 'djeskoy' in message.text:
        try:
            client.send_photo(message.chat.id, 'All_chervi/chervi_djeskoy.jpg')
        except:
            client.send_message(message.chat.id, 'Не удалось обработать запрос')
    elif 'гитлер' in message.text:
        try:
            client.send_photo(message.chat.id, 'All_chervi/chervi_gitler.jpg')  # Осуждаю / Condemn
        except:
            client.send_message(message.chat.id, 'Не удалось обработать запрос')
    elif 'гуль' in message.text:
        try:
            client.send_photo(message.chat.id, 'All_chervi/chervi_ghoul.jpg')
        except:
            client.send_message(message.chat.id, 'Не удалось обработать запрос')
    else:
        try:
            client.send_photo(message.chat.id, 'All_chervi/chervi.jpg')
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


@client.on_message(filters.regex('calc'))
def scripting(client, message):
    iteration = 0
    for i in client.get_chat_history(message.chat.id):
        iteration += 1
        if iteration == 1:
            with open('data.json', 'w', encoding='utf-8') as file:
                file.write(str(i))
            break

    with open('data.json', 'r', encoding='utf-8') as file:
        script_for_exe = json.loads(file.read())
    script = re.sub('calc ', '', script_for_exe.get('text'))
    try:
        client.send_message(message.chat.id, eval(script))

    except:
        client.send_message(message.chat.id, 'Не удалось обработать запрос')


client.run()

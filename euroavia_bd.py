import discord
import os
import pandas as pd

client = discord.Client()
excel_tasks = pd.read_excel('Euroavia_bot.xlsx')


def task(dept, sapt):
    #print(excel_tasks.head())

    sapt = int(sapt)

    return excel_tasks[dept][sapt]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$task'):
        info = msg.split('$')
        print(info)
        dept = info[2]
        sapt = info[3]
        sapt = int(sapt)
        sapt -= 1
        await message.channel.send(task(dept, sapt))

client.run(os.getenv('TOKEN'))

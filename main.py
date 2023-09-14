from bardapi import Bard
from bardapi.constants import *
import discord
from config import *
import asyncio
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from tokens import D_TOKEN

async def main():
    global bot,client
    bot = bot()
    try:
        src = Bard(token=B_TOKEN,session=session)
        bot = Bbot(src)
    except:
        src = await Chatbot.create()
        bot = Ebot(src)
    


@client.event
async def on_ready():
    rsp = await bot.ask("hello world")
    print(rsp)

@client.event
async def on_message(msg:discord.Message):
    if not msg.author.bot:
        if msg.author.display_name == AUTHOR and msg.content == "bye":
            await bot.close()
            await client.close()
            exit()
        print('msg from '+msg.author.display_name+' say '+msg.content)
        rsp = await bot.ask(msg.content)
        print('bot say '+rsp)
        print()
        await msg.channel.send(rsp)


asyncio.run(main())
client.run(token=D_TOKEN)

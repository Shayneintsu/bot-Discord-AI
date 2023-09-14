from bardapi import Bard
from bardapi.constants import *
import discord
from config import *
import asyncio
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from tokens import D_TOKEN

async def main():
    global ai,bot
    ai = AI()
    try:
        src = Bard(token=B_TOKEN,session=session)
        ai = Bai(src)
    except:
        tmp = True
        while tmp:
            try:
                src = await Chatbot.create()
                tmp = False
            except:
                tmp = True
        ai = Eai(src)
    


@bot.event
async def on_ready():

    synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ADMIN_ID,type=discord.Guild))
    print(f"Guild Admin {bot.get_guild(GUILD_ADMIN_ID).name}")
    synced = await bot.tree.sync()
    print(f"Sync {len(synced)} slash command:")
    for cmd in synced:
        print(cmd.name)

    rsp = await ai.ask("hello world")
    print(rsp)

@bot.event
async def on_message(msg:discord.Message):
    if not msg.author.bot:
        #ctx:discord.ext.commands.Context = await bot.get_context(msg)
        #await ctx.defer()
        await msg.channel.typing()
        print('msg from '+msg.author.display_name+' say '+msg.content)
        rsp = await ai.ask(msg.content)
        print('bot say '+rsp)
        print()
        await msg.channel.send(rsp)

@bot.tree.command(name="ping",description="Bot is it okay?")
async def ping(interact:discord.Interaction):
    await interact.response.send_message("Pong",ephemeral=True,delete_after=10)

@bot.tree.command(name="kill",description="Byeeeee",guild=discord.Object(id=GUILD_ADMIN_ID,type=discord.Guild))
async def ping(interact:discord.Interaction):
    await interact.response.defer()
    await interact.followup.send("Byeeeee",ephemeral=True)
    await ai.close()
    await bot.close()
    exit()


asyncio.run(main())
bot.run(token=D_TOKEN)

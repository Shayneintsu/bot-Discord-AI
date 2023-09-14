from bardapi import Bard
from bardapi.constants import *
import requests
import json
import discord
from discord.ext import commands
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from tokens import B_TOKEN


INIT_TEXT = ""
GUILD_ADMIN_ID = 1149470321603252326


#bot = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set('__Secure-1PSID',value=B_TOKEN)
    
class AI:
    sourceAI=None
    async def ask(self,text:str):...
    async def close(self):...


class Bai(AI):
    def __init__(self,bard:Bard) -> None:
        self.sourceAI = bard

    async def ask(self,text:str):
        return self.sourceAI.get_answer(text)['content']
    
    async def close(self):...
    

class Eai(AI):
    def __init__(self,bing:Chatbot) -> None:
        self.sourceAI = bing

    async def ask(self,text:str):
        rsp = await self.sourceAI.ask(prompt=text, conversation_style=ConversationStyle.creative, simplify_response=False)
        try:
            rsp = rsp['item']['messages'][-1]['text']
        except:          
            with open("debug.json", "w") as file:
                file.write(json.dumps(rsp))
            rsp = "error"
        return rsp
    
    async def close(self):
        await self.sourceAI.close()

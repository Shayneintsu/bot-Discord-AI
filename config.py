from bardapi import Bard
from bardapi.constants import *
import requests
import discord
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from tokens import B_TOKEN


INIT_TEXT = ""
AUTHOR = "shayneintsu"


client = discord.Client(intents=discord.Intents.all())

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set('__Secure-1PSID',value=B_TOKEN)
    
class bot:
    sourceAI=None
    async def ask(self,text:str):...
    async def close(self):...


class Bbot(bot):
    def __init__(self,bard:Bard) -> None:
        self.sourceAI = bard

    async def ask(self,text:str):
        return self.sourceAI.get_answer(text)['content']
    
    async def close(self):...
    

class Ebot(bot):
    def __init__(self,bing:Chatbot) -> None:
        self.sourceAI = bing

    async def ask(self,text:str):
        rsp = await self.sourceAI.ask(prompt=text, conversation_style=ConversationStyle.balanced, simplify_response=True)
        return rsp['text']
    
    async def close(self):
        await self.sourceAI.close()

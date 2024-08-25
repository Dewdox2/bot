from nextcord.ext import commands
from requests_futures.sessions import FuturesSession
import nextcord, datetime, requests, random

from myserver import  server_on

prefix = '!'
intents = nextcord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix=prefix,intents=intents)
bot.help_command = None

request = FuturesSession()
nawdatatime = datetime.datetime.now()

talkbotch = 1277262775466590310

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if (str(message.channel.id) == str(talkbotch)):
        if message.author != bot.user:
            a = random.choice(requests.get("https://btheruuen-api.shhhtovf.repl.co/text.txt").text.split('\n'))
            if a == "":
                b = random.choice(requests.get("https://btheruuen-api.shhhtovf.repl.co/text.txt").text.split('\n'))
                await message.channel.send(b)
            else:
                await message.channel.send(a)
            
@bot.event
async def on_ready():
    print("BOT BY CYBERSAFE")
    print(f"login bot {bot.user}")
            
server_on()

bot.run(os.getenv('TOKEN'))
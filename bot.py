import os
import configparser

from twitchio.ext import commands
from twitchio import Client

from datetime import datetime, timedelta
from time import sleep



bot = commands.Bot(
	token=os.environ['TMI_TOKEN'],
	client_id=os.environ['CLIENT_ID'],
	nick=os.environ['BOT_NICK'],
	prefix=os.environ['BOT_PREFIX'],
	initial_channels=[os.environ['CHANNEL']]	
)

config = configparser.ConfigParser()
config.read('commands.ini')

async def event_ready(self):
    print(f'Logged in as | {self.nick}')
    print(f'User id is | {self.user_id}')

@bot.event
async def event_ready():
	print(f"{os.environ['BOT_NICK']} is online!")
	ws = bot._ws
	await ws.send_privmsg(os.environ['CHANNEL'], f"/me beeps cheerily as she comes online!")
 
@bot.event
async def event_message(ctx):
    ctx.content=ctx.content.casefold()
    
    if ctx.author.name.casefold() == os.environ['Bot_NICK'].casefold():
        return
    
    await bot.handle_commands(ctx)
    
    if 'hello' in ctx.content:
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")
        
@bot.command(name='alive')
async def alive(ctx):
    await ctx.channel.send(config['UTIL']['ALIVE'])
    
    
    
if __name__=="__main__":
    bot.run()
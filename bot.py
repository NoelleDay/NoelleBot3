import os
import configparser

from twitchio.ext import commands
from twitchio import Client

from datetime import datetime, timedelta
from time import sleep


#The bot gets all variables from a .env file
#You MUST have all five of the variables in the following block in a .env file in the same directory as bot.py, except for CHANNEL which can be removed and replaced with other programmatic ways to join channels
bot = commands.Bot(
	token=os.environ['TMI_TOKEN'],
	client_id=os.environ['CLIENT_ID'],
	nick=os.environ['BOT_NICK'],
	prefix=os.environ['BOT_PREFIX'],
	initial_channels=[os.environ['CHANNEL']]	
)

#The bot reads all commands from an external file. 
#Current iteration uses .ini files using full header/key syntax. All entries in the commands.ini should look like the following two lines:
#[HEADER]
#KEY = "String to be output"
config = configparser.ConfigParser()
config.read('commands.ini')

""" This is commented out while I update to new syntax
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
"""
@bot.command(name='alive')
async def alive(ctx):
    await ctx.channel.send(config['UTIL']['ALIVE'])
    
@bot.command(name='help')
async def help(ctx):
    await ctx.channel.send(config['UTIL']['HELP'])
    
@bot.command(name='info')
async def info(ctx):
    await ctx.channel.send(config['UTIL']['INFO'])
    
@bot.command(name='socials')
async def socials(ctx):
    await ctx.channel.send(config['SOCIAL']['SOCIAL'])

@bot.command(name='social')
async def social(ctx):
    await ctx.channel.send(config['SOCIAL']['SOCIAL'])
    
@bot.command(name='discord')
async def discord(ctx):
    await ctx.channel.send(config['SOCIAL']['DISCORD'])
"""

@bot.command(name='socials')
async def socials(ctx):
    await ctx.channel.send(config['SOCIAL']['SOCIALS'])
@bot.command(name='discord')
async def discord(ctx):
    await ctx.channel.send(config['SOCIAL']['DISCORD'])
"""    
    
    
if __name__=="__main__":
    bot.run()
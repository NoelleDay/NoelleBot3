import os
import configparser

from twitchio.ext import commands
from twitchio import Client

from datetime import datetime, timedelta
from time import sleep

#The bot reads all commands from an external file. 
#Current iteration uses .ini files using full header/key syntax. All entries in the commands.ini should look like the following two lines:
#[HEADER]
#KEY = "String to be output"   
config = configparser.ConfigParser()
config.read('commands.ini')


#The bot gets all variables from a .env file
#You MUST have all five of the variables in the following block in a .env file in the same directory as bot.py, except for CHANNEL which can be removed and replaced with other programmatic ways to join channels
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
	        token=os.environ['TMI_TOKEN'],
	        client_id=os.environ['CLIENT_ID'],
	        nick=os.environ['BOT_NICK'],
	        prefix=os.environ['BOT_PREFIX'],
	        initial_channels=[os.environ['CHANNEL']],
            case_insensitive=True,
            )

    async def event_ready(self):
        print(f'Logged into Twitch as | {self.nick}')
        print(f'Logged in with ID | {self.user_id}')
        await self.connected_channels[0].send(f"/me beeps cheerily as she comes online!")
    
    

    async def event_message(self, message):
        msg = message.content
        if msg.startswith("!"):
            msg = msg[1:]
            
        cmd = {}
        #N0L now uses a rawtext file for commands, editable anytime
        #Format of command MUST be as follows, " = " as dilineator:
        #command = Text Output
        with open ("commands.txt") as file:
            for line in file:
                key, value = line.split(" = ")
                cmd[key] = value
        if msg.casefold() in cmd:
            msg = msg.lower()
            await message.channel.send(cmd[msg])

bot = Bot()
bot.run()
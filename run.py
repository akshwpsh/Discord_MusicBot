import discord
import asyncio
from discord.ext import commands
from config import token
from config import EXTENSIONS
from config import prefix

class ProjectPL (commands.Bot) : 
    def __init__ (self) :
        super().__init__ (
            command_prefix=[prefix],
            help_command=None
        )
        #self.remove_command("help")

        for i in EXTENSIONS :
            self.load_extension (i)
    
    async def on_ready (self) :
        print ('Bot is ready.')
        print ('Bot Name : ' + self.user.name)
    
    async def on_message (self, message) :
        if message.author.bot :
            return
        else :
            await self.process_commands (message)

bot = ProjectPL ()
bot.run (token, bot=True)

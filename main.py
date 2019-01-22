#Importing the necessary libraries
import discord
import asyncio

#This will not be used, but is necessary
command_prefix = ")"

#Assigning bot to a variable which contains the access to commands
bot = commands.Bot(command_prefix)

#Creating a bot event listener fro messages
@bot.event
async def on_message(message):
	

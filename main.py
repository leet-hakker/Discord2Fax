#Setting the chartype
# -*- coding: <utf-8> -*-

#Importing the necessary libraries
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

#This will not be used, but is necessary
command_prefix = ")"

#Assigning bot to a variable which contains the access to commands
bot = commands.Bot(command_prefix)

#Telling me when it is online
@bot.event
async def on_ready():
	print("Ready when you are\n\n")

#Creating a bot event listener for messages
@bot.event
async def on_message(message):
        #Opening a text file as a variable for easy access
        text_file = open("print.txt", "a+")
        #Creating a variable that contains the message
        message = message.content
        #Outputting the message for testing
        text_file.write("\n" + message)
        text_file.close

#This is the client token. Do not share it with anyone, otherwise they will have full access to the application.
bot.run("NTM3MzU5MzI0NTE5ODU4Mjgx.Dyo7vg.BRpL9xFl_B-mMNa5TMO7kANLlHg")

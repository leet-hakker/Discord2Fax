# Setting the chartype
# -*- coding: <utf-8> -*-

# Importing the necessary libraries
# Library is calle python-dotenv never forgetti
from dotenv import load_dotenv

load_dotenv()

import os
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

# This will not be used, but is necessary
command_prefix = ")"

# Assigning bot to a variable which contains the access to commands
bot = commands.Bot(command_prefix)


# Telling you when it is online
@bot.event
async def on_ready():
    print("Ready when you are\n\n")


# Creating a bot event listener for messages
@bot.event
async def on_message(message):
    # Opening a text file as a variable for easy access
    text_file = open("print.txt", "a+", encoding="utf-8")
    # Creating a variable that contains the message

    time = message.timestamp
    sender = message.author.name
    content = message.clean_content

    # Outputting the message for testing
    text_file.write('\n' + str(time) + '\n' + sender + ': ' + content)
    text_file.close()


# This is the client token. Do not share it with anyone, otherwise they will have full access to the application.
# Keep it in an environment variable!
bot.run(os.getenv("API_KEY"))
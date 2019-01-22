#Importing the necessary libraries
import discord
import asyncio

#This will not be used, but is necessary
command_prefix = ")"

#Assigning bot to a variable which contains the access to commands
bot = commands.Bot(command_prefix)

#Creating a bot event listener for messages
@bot.event
async def on_message(message):
	#Creating a variable that contains the message
	message = message.content
	#Outputting the message for testing
	print(message)

#This is the client secret. Do not share it with anyone, otherwise they will have full access to the application.
bot.run("S8rrEcnqt6OW1-NVBzaq0S2x1Rm_Z9VJ")

import discord
import os
from decouple import config


client = discord.Client()

# define messages
welcome_msg = "Welcome to Formica, the in-discord form service! It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# listen for messages.commands
@client.event
async def on_message(message):
    msg = message.content

    #ignore, if the msg is from ourselves
    if message.author == client.user:
        return

    # listen for commands
    if msg.startswith('!formica'):
        #display welcome message
        await message.channel.send(welcome_msg)

# listen for reactions
@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.content == welcome_msg:
        await user.send("hi")

# run bot
BOT_TOKEN = config('TOKEN')
client.run(BOT_TOKEN)


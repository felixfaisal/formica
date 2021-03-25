import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# listen for messages
@client.event
async def on_message(message):
    msg = message.content

    #ignore, if the msg is from ourselves
    if message.author == client.user:
        return

    # listen for commands
    if msg.startswith('!formica'):
        welcome = "Welcome to Formica, the in-discord form service! It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!"
        #display welcome message
        await message.channel.send(welcome)

# run bot
client.run(os.getenv('TOKEN'))
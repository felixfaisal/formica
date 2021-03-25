import discord
import os
from decouple import config


client = discord.Client()

# define messages
welcome_title = "Welcome to Formica, the in-discord form service!"
welcome_msg = "It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!"
form_name = "Event Registration"

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
        #embed constructor
        welcome_embed = discord.Embed(title = welcome_title, description = welcome_msg, color = 0xff8906)
        welcome_embed.add_field(name = "Form: ", value = form_name, inline = False)

        await message.channel.send(embed=welcome_embed)

# listen for reactions
@client.event
async def on_reaction_add(reaction, user):
    # grab the title of the embed msg that was reacted to
    message_title = reaction.message.embeds[0].title

    # check if the message was the welcome msg
    if message_title == welcome_title:
        await user.send("hi")


# run bot
BOT_TOKEN = config('TOKEN')
client.run(BOT_TOKEN)


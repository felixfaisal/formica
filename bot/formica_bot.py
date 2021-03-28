import discord
import os
import json
from decouple import config



client = discord.Client()

form_color = 0xff8906
# define messages
welcome_title = "Welcome to Formica, the in-discord form service!"
welcome_msg = "It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!"
form_name = "Event Registration"


form_init_msg = "To start, type !start"

# tmp
cur_q = "What is your first name?"
cur_q_description = " "
cur_response = "response"

def get_questions():
    with open("dummy_questions.json", "r") as q:
        questions = json.load(q)
    return questions

def start_form():
    questions = get_questions()
    cur_q_embed = discord.Embed(title = questions[0]['question'], description = questions[0]['description'], color = form_color)
    return cur_q_embed

def set_response(response, author, index):
    # get the responses from the database
    with open("dummy_responses.json", "r") as r:
        database_responses = json.load(r)
    
    # test
    # print("retrieved responses: ", database_responses)
    # print("type: ", type(database_responses))
    # print(f"response: {response}, author: {author}, author id: {author.id}")

    # search database for the user
    try:
        target = next(user for user in database_responses if user['username'] == str(author) )
        print("target: ", target)

        # get index
        target_index = database_responses.index(target)
        print("found at index ", target_index)    

        #set response
    except:
        print("not found")
        # append to database

    #write to the database


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    get_questions()

# listen for messages/commands
@client.event
async def on_message(message):
    msg = message.content

    #ignore, if the msg is from ourselves
    if message.author == client.user:
        return

    # listen for commands
    if msg.startswith('!formica'):
        #embed constructor
        welcome_embed = discord.Embed(title = welcome_title, description = welcome_msg, color = form_color)
        welcome_embed.add_field(name = "Form: ", value = form_name, inline = False)

        # send welcome message
        await message.channel.send(embed=welcome_embed)
    
    if msg.startswith('!start'):
        # send form start prompt
        start_embed = start_form()
        await message.channel.send(embed=start_embed)

        # wait for response
        def check(m):
            # check that it's the right user and channel
            # later: check that we're on the right question or else the form restarts
            return m.author.id == message.author.id and m.channel == message.channel

        msg = await client.wait_for('message', check=check)

        # save response
        cur_response = msg.content
        set_response(msg.content, message.author, 0)

        # send feedback to user
        await message.channel.send(f"Response received: {msg.content}")




# listen for reactions
@client.event
async def on_reaction_add(reaction, user):
    # grab the title of the embed msg that was reacted to
    message_title = reaction.message.embeds[0].title

    # check if the message was the welcome msg
    if message_title == welcome_title:
        # send the form instruction message to the user
        form_init = discord.Embed(title = form_name, description = form_init_msg, color = form_color)
        form_init.add_field(name = "Instructions: ", value = "Respond to my questions by typing a message like you normally would!\n You can edit your response by hovering on your message and clicking 'edit'.\n To see a list of available commands, type !help.", inline = False)

        await user.send(embed=form_init)



# run bot
BOT_TOKEN = config('TOKEN')
client.run(BOT_TOKEN)


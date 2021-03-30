import discord
import os
import json
from decouple import config

intents = discord.Intents().default()
intents.members = True
intents.reactions = True

client = discord.Client(intents = intents)

form_color = 0xff8906
emoji_options = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣']
# define messages
welcome_title = "Welcome to Formica, the in-discord form service!"
welcome_msg = "It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!"
form_name = "Event Registration"


form_init_msg = "To start, type !start"

author_index = 0
responses = []
form_started = False

def start_form():
    form_started = True
    global responses
    with open("dummy_questions.json", "r") as q:
        questions = json.load(q)
        q_count = len(questions)
    
    with open('dummy_responses.json', 'r') as r:
        responses = json.load(r)

    return questions, q_count


def get_question(questions, cur_index):
    # The process of making the embed is the same, whether the q_type is text or multi-choice
    cur_q_embed = discord.Embed(title = questions[cur_index]['question'], description = questions[cur_index]['description'], color = form_color) 

    # check if we have an m/c question
    if questions[cur_index]['input_type'] == "multiple choice":
        tot_options = len(questions[cur_index]['options'])

        # add m/c instructions to question description
        cur_q_embed.description += "\nAnswer by reacting with the corresponding emoji."

        # iterate through the options and emojis, adding them to the embed
        for index in range(tot_options):
            print(emoji_options[index])
            print(index)
            cur_q_embed.add_field(name = f"{emoji_options[index]} {questions[cur_index]['options'][index]}", value = '** **', inline = False)
    
    return cur_q_embed

def set_response(response, author, index):
    global responses
    global author_index
    # get the responses from the database
    # with open('dummy_responses.json', 'r') as r:
    #     responses = json.load(r)
    
    # test
    # print("retrieved responses: ", database_responses)
    # print("type: ", type(database_responses))
    # print(f"response: {response}, author: {author}, author id: {author.id}")

    # search database for the user
    try:
        target = next(user for user in responses if user['username'] == str(author) )
        # print("target: ", target)

        # get index
        author_index = responses.index(target)
        #print("found at index ", target_index)    

        #set response & id
        responses[author_index]['responses'].append(response.content)
        responses[author_index]['response_ids'].append(response.id)
        print("set: ", responses)
    except:
        print("not found")
        # append to database
        responses.append({'username': str(author), 'user_id': str(author.id), 'responses': [response.content], 'response_ids': [response.id]})
        print("appended: ", responses)

        author_index = len(responses) - 1
    
    #return user_index

def edit_response(new_response):
    global author_index
    # search responses for corresponding id

    try:
        print("response ids:")
        for item in responses[author_index]['response_ids']:
            if item == new_response.id:
                target = item
                target_index = responses[author_index]['response_ids'].index(target)

    except:
        print("id not found")
    else:
        print(f"id found at index {target_index}")
        # write over the response 
        responses[author_index]['responses'][target_index] = str(new_response.content)
    

def end_form(questions, author_index):
    form_started = False
    global responses
    confirmation_embed = discord.Embed(title = 'Confirm your answers', description = 'React with ✅ to submit.\n If you need to edit your answers, go back and do so, then come back here.', color = form_color)

    # print("responses: ", responses)
    # print("1st q: ", questions[0]['question'])
    # print("1st response: ", responses[author_index]['responses'][0])

    for item in range(len(questions)):
        confirmation_embed.add_field(name = questions[item]['question'], value = responses[author_index]['responses'][item], inline = False)
    
    return confirmation_embed

def submit_responses():
    global responses
    #write to the database
    with open('dummy_responses.json', 'w') as w:
        json.dump(responses, w)
    #make an embed
    submitted_embed = discord.Embed(title = 'Form submitted', description = 'You can view and manage your responses here: <insert link>', color = form_color)
    return submitted_embed


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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

        # wait for a reaction
        def check_reaction(reaction, user):
            return True, user == message.author #true, b'c we're accepting any reaction

        try:
            reaction, user = await client.wait_for('reaction_add', check=check_reaction)
        except:
            print("something went wrong")
        else:
            print(user)
            form_init = discord.Embed(title = form_name, description = form_init_msg, color = form_color)
            form_init.add_field(name = "Instructions: ", value = "Respond to my questions by typing a message like you normally would!\n You can edit your response by hovering on your message and clicking 'edit'.\n To see a list of available commands, type !help.", inline = False)

            await user.send(embed=form_init)
    
    if msg.startswith('!start'):
        if form_started == False:
            cur_index = 0
            questions, q_count = start_form()   

        while cur_index < q_count:
            #print(f"cur index: {cur_index}, total qs: {q_count}")

            # send the current question
            q_embed = get_question(questions, cur_index)
            await message.channel.send(embed=q_embed)
            print("question id: ", message.id)
            print("question sent at: ", message.created_at)
            print("question: ", q_embed.title)

            # wait for response
            def check(m):
                # check that it's the right user and channel
                # later: check that we're on the right question or else the form restarts
                return m.author.id == message.author.id and m.channel == message.channel

            msg = await client.wait_for('message', check=check)

            # save response
            cur_response = msg.content
            #author_index = set_response(msg, message.author, cur_index)
            set_response(msg, message.author, cur_index)
            print(f"received response: {cur_response}, id: {msg.id}")

            # send feedback to user
            # await message.channel.send(f"Response received: {msg.content}")

            # update counters
            cur_index += 1
        
        #await message.channel.send("Questions completed")
        confirmation_embed = end_form(questions, author_index)
        confirmation_msg = await message.channel.send(embed=confirmation_embed)
        await confirmation_msg.add_reaction('✅')

        # wait for a reaction
        def check_reaction(reaction, user):
            return str(reaction.emoji) == '✅' and user == message.author

        try:
            reaction, user = await client.wait_for('reaction_add', check=check_reaction) #add timeout?
        except:
            print("wrong reaction")
        else:
            print(user)
            submitted_embed = submit_responses()
            await user.send(embed=submitted_embed)

# detect message edits
@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
        print(f"Edit detected.\n Before: {before.content}, {before.id}, {before.created_at}\n After: {after.content}, {after.id}, {after.created_at}")
        # edit the response
        edit_response(after)

# listen for reactions
# @client.event
# async def on_reaction_add(reaction, user):
#     print("user: ", user)
#     #ignore, if the reaction is from ourselves
#     if user == client.user:
#         print("reaction is from ourselves")
#     else:
#         # print("message content: ", reaction.message.content)
#         # print("message content: ", reaction.message.embeds[0].title)
#         # grab the title of the embed msg that was reacted to
#         message_title = reaction.message.embeds[0].title

#         # check if the message was the welcome msg
#         if message_title == welcome_title:
#         #if reaction.message.content == welcome_msg:
#             # send the form instruction message to the user
#             form_init = discord.Embed(title = form_name, description = form_init_msg, color = form_color)
#             form_init.add_field(name = "Instructions: ", value = "Respond to my questions by typing a message like you normally would!\n You can edit your response by hovering on your message and clicking 'edit'.\n To see a list of available commands, type !help.", inline = False)

#             await user.send(embed=form_init)

        # if reaction.emoji == '✅' and reaction.message.content == '!start':
        #     submit_responses()
        #     await user.send("Responses have been submitted")



# run bot
BOT_TOKEN = config('TOKEN')
client.run(BOT_TOKEN)


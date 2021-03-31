import discord
import os
import json
from decouple import config

intents = discord.Intents().all()
# intents.members = True
# intents.reactions = True

client = discord.Client(intents = intents)

# form stuff
form_name = "Name"
form_color = 0xff8906
#form_server = ""
form_alert_channel = ""

emoji_options = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣']
# define messages
welcome_title = "Welcome to Formica, the in-discord form service!"
welcome_msg = "It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!"


form_init_msg = "To start, type !start"

author_index = 0
responses = []
questions = []
mc_ids = []
tot_options = 0
q_count = 0
confirmation_embed = discord.Embed(title = 'Confirm your answers', description = 'React with ✅ to submit.\n If you need to edit your answers, go back and do so, then come back here.', color = form_color)

confirmation_id = 0
form_started = False

def start_form():
    form_started = True
    global responses, questions, q_count

    # get questions
    with open("dummy_questions.json", "r") as q:
        questions = json.load(q)
        q_count = len(questions)
    
    # get responses
    with open('dummy_responses.json', 'r') as r:
        responses = json.load(r)


def get_question(cur_index):
    global questions, tot_options
    q_type = questions[cur_index]['input_type']
    # The process of making the embed is the same, whether the q_type is text or multi-choice
    cur_q_embed = discord.Embed(title = questions[cur_index]['question'], description = questions[cur_index]['description'], color = form_color) 

    # check if we have an m/c question
    if q_type == "multiple choice":
        tot_options = len(questions[cur_index]['options'])

        # add m/c instructions to question description
        cur_q_embed.description += "\nAnswer by reacting with the corresponding emoji."

        # iterate through the options and emojis, adding them to the embed
        for index in range(tot_options):
            cur_q_embed.add_field(name = f"{emoji_options[index]} {questions[cur_index]['options'][index]}", value = '** **', inline = False)


    return cur_q_embed, q_type

def set_response(response, response_id, author, index):
    global responses, author_index
    
    print(f"response: {response}, author: {author}, author id: {author.id}")

    # search database for the user
    try:
        target = next(user for user in responses if user['username'] == str(author) )
        # print("target: ", target)

        # get index
        author_index = responses.index(target)
        #print("found at index ", target_index)    

        #set response & id
        responses[author_index]['responses'].append(response)
        responses[author_index]['response_ids'].append(response_id)
        #print("set: ", responses)
    except:
        print("not found")
        # append to database
        responses.append({'username': str(author), 'user_id': str(author.id), 'responses': [response], 'response_ids': [response_id]})
        #print("appended: ", responses)

        author_index = len(responses) - 1
    
    #return user_index

def edit_response(edited_response, question_type):
    global author_index, questions, confirmation_embed
    
    #grab the message and id
    if question_type == "text":
        new_response = edited_response.content
        new_response_id = edited_response.id

    elif question_type == "multiple choice":
        # get the index
        emoji_index = emoji_options.index(str(edited_response.emoji))

        #check that index is valid
        if emoji_index >= tot_options:
            print(f"invalid option {emoji_index} selected")
            return
        
        # get the id
        new_response_id = edited_response.message.id

        # find the question index
        for index in range(len(questions)):
            if questions[index]['question_id'] == new_response_id:
                print("FLAG: question found")
                q_index = index

        # grab the corresponding option and set that as the new message
        new_response = questions[q_index]['options'][emoji_index]       

    # search responses for corresponding id
    try:
        for item in responses[author_index]['response_ids']:
            if item == new_response_id:
                target = item
                target_index = responses[author_index]['response_ids'].index(target)

    except:
        print("id not found")
    else:
        print(f"id found at index {target_index}")

        # write over the response      
        responses[author_index]['responses'][target_index] = str(new_response)

        #edit the confirmation message
        new_confirmation = confirmation_embed
        new_confirmation.set_field_at(index = target_index, name = questions[target_index]['question'], value = new_response, inline = False)
        return new_confirmation
        


def end_form(author_index):
    global questions, responses, confirmation_embed

    # confirmation_embed = discord.Embed(title = 'Confirm your answers', description = 'React with ✅ to submit.\n If you need to edit your answers, go back and do so, then come back here.', color = form_color)

    # add questions and answers to the embed
    for item in range(len(questions)):
        confirmation_embed.add_field(name = questions[item]['question'], value = responses[author_index]['responses'][item], inline = False)
    
    return confirmation_embed

def submit_responses(user):
    global responses, form_name, form_started
    form_started = False

    #write to the database
    with open('dummy_responses.json', 'w') as w:
        json.dump(responses, w)

    #make submission confirmation for the user
    submission_alert_user = discord.Embed(title = 'Form submitted', description = 'You can view and manage your responses here: <insert link>', color = form_color)

    # make a submission confirmation for the form author
    submission_alert_author = discord.Embed(title = f'{user} has submitted a form', description = 'To manage your forms, click here: <insert link>', color = form_color)
    submission_alert_author.add_field(name = 'Form:', value = form_name, inline = False)

    return submission_alert_user, submission_alert_author


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # later: get form name, form server, and channel to send updates to
    global form_name, form_channel, form_alert_channel
    form_name = "Event Registration"
    form_alert_channel = client.get_channel(824348394411262013)

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
            form_init.add_field(name = "Instructions: ", value = "Respond to my questions by typing a message like you normally would.\n You can edit your response by hovering on your message and clicking 'edit'", inline = False)

            await user.send(embed=form_init)
    
    if msg.startswith('!start'):
        # check that we're in a DM channel, with the user that sent the command
        print("channel type: ", message.channel)
        #print(f"channel recipient: {message.channel.recipient}, message author: {message.author}")
        if message.channel.type != "private" and message.channel.recipient != message.author:
            print("!start invoked in a non-private channel")
            return
        
        global tot_options, confirmation_id, form_started

        if form_started == False:
            form_started = True
            cur_index = 0
            start_form()
        else:
            print("form already started")
            await message.author.send("Oops! You've already started this form. Answer the previous question to proceed.\nYou can answer by sending a message, or if it's a multiple choice, by reacting to the message.")
    
        while cur_index < q_count:
            print(f"cur index: {cur_index}, total qs: {q_count}")

            # send the current question
            q_embed, q_type = get_question(cur_index)
            q_message = await message.author.send(embed=q_embed)
            # save the question id
            questions[cur_index]['question_id'] = q_message.id
            print("question id: ", q_message.id)
            print("question: ", q_embed.title)

            # check question type
            if q_type == "text":
                # wait for response
                def check(m):
                    # check that it's the right user and channel
                    # ignore message if it's the !start command
                    return m.author.id == message.author.id and m.channel == message.channel and m.content.startswith('!start') == False

                msg = await client.wait_for('message', check=check)

                # save response
                set_response(msg.content, msg.id, message.author, cur_index)

            elif q_type == "multiple choice":
                global mc_ids
                mc_ids.append(q_message.id)

                # add the option emojis to our message
                for index in range(tot_options):
                    await q_message.add_reaction(emoji_options[index])
                
                # wait for reaction
                def check_reaction(reaction, user):
                    # check that the emoji is within the range of alloted options & it's from the right user
                    return (str(reaction.emoji) in emoji_options[0:tot_options]) and (user == message.author)
                
                reaction, user = await client.wait_for('reaction_add', check=check_reaction)

                #get the option they selected
                option_index = emoji_options.index(str(reaction.emoji))
                response = questions[cur_index]['options'][option_index]

                #save response
                set_response(response, q_message.id, user, cur_index)
                
            # update counters
            cur_index += 1
                    
        # send confirmation message
        confirmation_embed = end_form(author_index)
        confirmation_msg = await message.channel.send(embed=confirmation_embed)
        confirmation_id = confirmation_msg.id
        await confirmation_msg.add_reaction('✅')

        # wait for a reaction
        def check_reaction(reaction, user):
            return str(reaction.emoji) == '✅' and user == message.author

        try:
            reaction, user = await client.wait_for('reaction_add', check=check_reaction) #add timeout?
        except:
            print("wrong reaction")
        else:
            # submit response, get the confirmation embeds
            submission_alert_user, submission_alert_author = submit_responses(user)

            # send a submission confirmation to the user
            await user.send(embed=submission_alert_user)

            # send a submission confirmation to the author
            await form_alert_channel.send(embed=submission_alert_author)

# detect message edits
@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
        # print(f"Edit detected.\n Before: {before.content}, {before.id}, {before.created_at}\n After: {after.content}, {after.id}, {after.created_at}")
        # edit the response & get an updated embed
        old_confirmation = await after.channel.fetch_message(confirmation_id)
        new_confirmation = edit_response(after, "text")
        await old_confirmation.edit(embed = new_confirmation)

# detect edits to mc questions
@client.event
async def on_reaction_add(reaction, user):
    # need to make sure this doesn't clash with the intital rxn
    # print("user: ", user)
    # print("message id: ", reaction.message.id)

    #ignore, if the reaction is from ourselves
    if user == client.user:
        return

    # check if it's an mc question
    if (reaction.message.id in mc_ids):
        print("change to mc response detected")

        old_confirmation = await reaction.message.channel.fetch_message(confirmation_id)
        new_confirmation = edit_response(reaction, "multiple choice")
        await old_confirmation.edit(embed = new_confirmation)

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


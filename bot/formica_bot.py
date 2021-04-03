import discord
import os
import json
from decouple import config

import globals 

from bot_functions import get_form_specs
from bot_functions import get_form
from bot_functions import get_question
from bot_functions import get_user 
from bot_functions import set_response 
from bot_functions import edit_response 
from bot_functions import end_form 
from bot_functions import submit_responses

intents = discord.Intents().all()
intents.reactions = True
client = discord.Client(intents = intents)


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
        # get form specs
        alert_channel_id, globals.form_name = get_form_specs()
        globals.form_alert_channel = client.get_channel(alert_channel_id)
        #embed constructor
        welcome_embed = discord.Embed(title = "Welcome to Formica, the in-discord form service!", description = "It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!", color = globals.form_color)
        welcome_embed.add_field(name = "Form: ", value = globals.form_name, inline = False)

        # send welcome message
        await message.channel.send(embed=welcome_embed)

        # wait for a reaction
        def check_reaction(reaction, user):
            return True, user == message.author #true, b'c we're accepting any reaction

        try:
            reaction, user = await client.wait_for('reaction_add', check=check_reaction)
        except:
            # add timeout here if needed
            print("something went wrong")
        else:
            form_init = discord.Embed(title = globals.form_name, description = "To start, type !start", color = globals.form_color)
            form_init.add_field(name = "Instructions: ", value = "Respond to my questions by typing a message like you normally would.\n You can edit your response by hovering on your message and clicking 'edit'", inline = False)

            await user.send(embed=form_init)
    
    if msg.startswith('!start'):
        # check that we're in a DM channel, with the user that sent the command
        print("channel type: ", message.channel)
        #print(f"channel recipient: {message.channel.recipient}, message author: {message.author}")
        if message.channel.type != "private" and message.channel.recipient != message.author:
            print("!start invoked in a non-private channel")
            return
        
        # check if form has already been started
        if globals.form_started == False:
            globals.form_started = True

            # get form specs
            alert_channel_id, globals.form_name = get_form_specs()
            globals.form_alert_channel = client.get_channel(alert_channel_id)
            cur_index = 0
            
            # get our questions and responses
            q_count = get_form()
            # search for the user in the saved responses
            get_user(message.author)
        else:
            print("form already started")
            await message.author.send("Oops! You've already started this form. Answer the previous question to proceed.\nYou can answer by sending a message, or by reacting to the question if it's a multiple choice.")
        
        # check if form has already been submitted by the user
        if globals.form_submitted == True:
            print("This user has already submitted a form")
            await message.author.send("It looks like you've already submitted this form. You can manage your responses here: <insert link>")
            return
    
        while cur_index < q_count:
            print(f"cur index: {cur_index}, total qs: {q_count}")

            # send the current question
            q_embed, q_type = get_question(cur_index)
            q_message = await message.author.send(embed=q_embed)
            # save the question id
            globals.questions[cur_index]['question_id'] = q_message.id
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
                #global mc_ids
                globals.mc_ids.append(q_message.id)

                # add the option emojis to our message
                for index in range(globals.tot_options):
                    await q_message.add_reaction(globals.emoji_options[index])
                
                # wait for reaction
                def check_reaction(reaction, user):
                    # check that the emoji is within the range of alloted options & it's from the right user
                    return (str(reaction.emoji) in globals.emoji_options[0:globals.tot_options]) and (user == message.author) and reaction.message.content.startswith('!start') == False
                
                reaction, user = await client.wait_for('reaction_add', check=check_reaction)

                #get the option they selected
                option_index = globals.emoji_options.index(str(reaction.emoji))
                response = globals.questions[cur_index]['options'][option_index]
                
                #save response
                set_response(response, q_message.id, user, cur_index)
                
            # update counters
            cur_index += 1
                    
        # send confirmation message
        confirmation_embed = end_form()
        confirmation_msg = await message.channel.send(embed=confirmation_embed)
        globals.confirmation_id = confirmation_msg.id
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
            submission_alert_user, submission_alert_creator = submit_responses(user)

            # send a submission confirmation to the user
            await user.send(embed=submission_alert_user)

            # send a submission confirmation to the form creator
            await globals.form_alert_channel.send(embed=submission_alert_creator)

# detect message edits
@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
        # print(f"Edit detected.\n Before: {before.content}, {before.id}, {before.created_at}\n After: {after.content}, {after.id}, {after.created_at}")
        # edit the response & get an updated embed
        old_confirmation = await after.channel.fetch_message(globals.confirmation_id)
        new_confirmation = edit_response(old_confirmation, after, "text")
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
    if (reaction.message.id in globals.mc_ids):
        try:
            old_confirmation = await reaction.message.channel.fetch_message(globals.confirmation_id)
            new_confirmation = edit_response(old_confirmation, reaction, "multiple choice")
            await old_confirmation.edit(embed = new_confirmation)
            print("change to mc response detected")
        except:
            return

# run bot
BOT_TOKEN = config('TOKEN')
client.run(BOT_TOKEN)


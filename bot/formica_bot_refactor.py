# Changing control flow to accomodate mult users

import discord
from discord.ext import commands
import os
import json
from decouple import config
#from dotenv import load_dotenv

import globals 

from bot_requests import get_forms
from bot_requests import get_responses
from bot_requests import submit_responses

from bot_functions import get_question
from bot_functions import get_user 
from bot_functions import set_response 
from bot_functions import edit_response 
from bot_functions import end_form 

from bot_validation import validate_response

#load_dotenv()

intents = discord.Intents().all()
intents.reactions = True
client = commands.Bot(command_prefix="!", intents=intents)


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

    await client.process_commands(message)

@client.command()
async def test(ctx):
    await ctx.channel.send("I hear you")

@client.command()
async def formica(ctx, *, received_name: str): # so we don't have to wrap form name in quotes
    print("formica called")
    # get forms from the database
    get_forms(ctx.guild.id)

    # check if name is empty
    if received_name == "start":
        if len(globals.forms) == 0:
            await ctx.send("It looks like there are no forms to fill out.")
            return
        else:
            # make a list of available forms
            list_embed = discord.Embed(title = "Welcome to Formica, the in-discord form service!", description = "To start filling out a form, please type !formica <form name>", color = globals.form_color)

            form_list = ""
            for item in globals.forms:
                form_list += f" - {item['FormName']}\n"

            list_embed.add_field(name = "Available Forms: ", value = form_list, inline = False)

            await ctx.send(embed = list_embed)
            return
    else:
        # check that form exists
        target = next((item for item in globals.forms if item["FormName"].lower() == received_name.lower()), None)
        if target == None:
            await ctx.send("It looks like this form doesn't exist. Please try again!")
            return
        else:
            print(target)

            # get the index of the form
            
            globals.form_index = globals.forms.index(target)
            print("form index is: ", globals.form_index)

            # save the form name
            globals.form_name = target["FormName"]

            # get the channel to send alerts to
            alert_channel_id = 824348394411262013
            globals.form_alert_channel = client.get_channel(alert_channel_id)

            # extract the questions
            globals.questions = globals.forms[globals.form_index]["Formfields"]

            # get the responses
            get_responses(globals.form_name)

        #embed constructor
        welcome_embed = discord.Embed(title = "Welcome to Formica, the in-discord form service!", description = "It looks like you have a form to fill out. To do so, please react to this message with any emoji. Then, check your inbox!", color = globals.form_color)
        welcome_embed.add_field(name = "Form: ", value = globals.form_name, inline = False)

        # send welcome message
        welcome_msg = await ctx.send(embed=welcome_embed)
        globals.welcome_ids.append(welcome_msg.id)

@client.command()
async def start(ctx):
    # check that we're in a DM channel, with the user that sent the command
        print("channel type: ", ctx.channel)
        #print(f"channel recipient: {message.channel.recipient}, message author: {message.author}")
        if ctx.channel.type != "private" and ctx.channel.recipient != ctx.author:
            print("!start invoked in a non-private channel")
            return

        # search for the user in the saved responses
        user_submitted = get_user(ctx.author)

        # check if form has already been submitted by the user
        if user_submitted == True:
            print("This user has already submitted a form")
            await ctx.author.send("It looks like you've already submitted this form. You can manage your responses here: <insert link>")
            return
        
        # check if form has already been started
        if globals.trackers[ctx.author.id]['form_started'] == False:
            globals.trackers[ctx.author.id]['form_started'] = True
            cur_index = 0
        else:
            print("form already started")
            await ctx.author.send("Oops! You've already started this form. Answer the previous question to proceed.\nYou can answer by sending a message, or by reacting to the question if it's a multiple choice.")
        
        # check if there's any forms to fill out
        if len(globals.forms) == 0:
            await ctx.author.send("It looks like there's no forms to fill out. Please go back to your server and check again.")
            return

        
    
        while cur_index < len(globals.questions):
            print(f"cur index: {cur_index}, total qs: {len(globals.questions)}")

            # send the current question
            q_embed, q_type = get_question(cur_index)
            q_message = await ctx.author.send(embed=q_embed)

            # save the question id
            globals.questions[cur_index]['question_id'] = q_message.id
            print("question: ", q_embed.title)
            print("question id: ", q_message.id)
            print("question type: ", q_type)

            # check question type (we don't need to validate text or m/c)
            if q_type == "multiple choice":
                globals.mc_ids.append(q_message.id)
                print("mcs: ", globals.mc_ids)

                # add the option emojis to our message
                for index in range(globals.tot_options):
                    await q_message.add_reaction(globals.emoji_options[index])
                
                # wait for reaction
                def check_reaction(reaction, user):
                    # check that the emoji is within the range of alloted options & it's from the right user
                    return (str(reaction.emoji) in globals.emoji_options[0:globals.tot_options]) and user==ctx.author
                
                reaction, user = await client.wait_for('reaction_add', check=check_reaction)

                print(user, ctx.author)

                #get the option they selected
                option_index = globals.emoji_options.index(str(reaction.emoji))
                response = globals.questions[cur_index]['options'][option_index]

                
                #save response
                set_response(response, q_message.id, user, cur_index)
            else:
                # wait for response
                def check(m):
                    # check that it's the right user and channel
                    # ignore message if it's the !start command
                    return m.author.id == ctx.author.id and m.channel == ctx.channel and m.content.startswith('!start') == False

                msg = await client.wait_for('message', check=check)

                # validate response (if it's an email, phone, or number)
                if q_type == "email" or q_type == "phone" or q_type =="number":                        
                    #print("🔴 non text or mc detected")
                    valid_response = validate_response(msg.content, q_type)

                    #if response is invalid, prompt user to try again
                    while valid_response == False:
                        await ctx.author.send("It looks like your response was in the wrong format. Please try again")
                        msg = await client.wait_for('message', check=check) # wait for response
                        valid_response = validate_response(msg.content, q_type) # re-validate
                    
                # If it's a text response, save the response
                set_response(msg.content, msg.id, ctx.author, cur_index)
                
            # update counters
            cur_index += 1
                    
        # send confirmation message
        confirmation_embed = end_form(ctx.author)
        confirmation_msg = await ctx.channel.send(embed=confirmation_embed)
        globals.trackers[ctx.author.id]['confirmation_id'] = confirmation_msg.id
        await confirmation_msg.add_reaction('✅')

        # wait for a reaction
        def check_reaction(reaction, user):
            return str(reaction.emoji) == '✅' and user == ctx.author

        try:
            reaction, user = await client.wait_for('reaction_add', check=check_reaction) #add timeout?
        except:
            print("wrong reaction")
        else:
            print("🔴 confirmation detected")
            # submit response, get the confirmation embeds
            submission_alert_user, submission_alert_creator = submit_responses(user)

            # send a submission confirmation to the user
            await ctx.author.send(embed=submission_alert_user)

            # send a submission confirmation to the form creator
            await globals.form_alert_channel.send(embed=submission_alert_creator)

# detect message editd

@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
        #print(f"🔴 Edit detected.\n Before: {before.content}, {before.id}, {before.created_at}\n After: {after.content}, {after.id}, {after.created_at}")
        # edit the response & get an updated embed
        try:
            confirmation_id = globals.trackers[before.author.id]['confirmation_id']
            old_confirmation = await after.channel.fetch_message(confirmation_id)
        except:
            # if user edited response b4 the end of the form, we don't need to update the confirmation msg
            new_confirmation, valid_response = edit_response(None, after, after.id)
            if valid_response == False:
                await after.reply("It looks like your edited response was in the wrong format. Please try editing your response again.")
        else:
            new_confirmation, valid_response = edit_response(old_confirmation, after, after.id)
            if valid_response == False:
                await after.reply("It looks like your edited response was in the wrong format. Please try editing your response again.")
            else:
                await old_confirmation.edit(embed = new_confirmation)

# detect edits to mc questions
@client.event
async def on_reaction_add(reaction, user):
    #print("🔴 reaction detected")
    #ignore, if the reaction is from ourselves
    if user == client.user:
        return

    # check if reaction was added to form welcome message
    if (reaction.message.id in globals.welcome_ids):
        #print("🔴 user reacted to formica")
        form_init = discord.Embed(title = globals.form_name, description = "To start, type !start", color = globals.form_color)
        form_init.add_field(name = "Instructions: ", value = "Respond to my questions by typing a message like you normally would.\n You can edit your response by hovering on your message and clicking 'edit'", inline = False)

        await user.send(embed=form_init)

    # check if it's an mc question; we don't need to validate mc responses
    elif (reaction.message.id in globals.mc_ids):
        #print("🔴 user reacted to mc")
        try:
            confirmation_id = globals.trackers[before.author.id]['confirmation_id']
            old_confirmation = await reaction.message.channel.fetch_message(globals.confirmation_id)
        except:
            # if user edited response b4 the end of the form, we don't need to update the confirmation msg
            new_confirmation, valid_response = edit_response(None, reaction, reaction.message.id)
        else:
            new_confirmation, valid_response = edit_response(old_confirmation, reaction, reaction.message.id)
            await old_confirmation.edit(embed = new_confirmation)

# run bot
#BOT_TOKEN = os.getenv("TOKEN")
BOT_TOKEN = config("TOKEN")
client.run(BOT_TOKEN)


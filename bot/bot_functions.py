# Functions that handle the form go here

import discord
import os
import json
import globals

from bot_validation import validate_response

# Description: Fetches the current question to create an embedded question message
def get_question(cur_index, user_id):
    user_index = globals.trackers[user_id]['response_index']
    form_id = globals.local_responses[user_index]['form_id']
    questions = globals.local_forms[form_id]["Formfields"]
    # get question type
    q_type = questions[cur_index]['input_type']
    # The process of making the embed is the same, whether the q_type is text or multi-choice
    cur_q_embed = discord.Embed(title = questions[cur_index]['question'], description = "", color = globals.form_color) 

    # add the appropriate insturctions to the question
    if q_type == "multiple choice":
        tot_options = len(questions[cur_index]['options'])

        # add m/c instructions to question description
        cur_q_embed.description = "\nAnswer by reacting with the corresponding emoji."

        # iterate through the options and emojis, adding them to the embed
        for index in range(tot_options):
            cur_q_embed.add_field(name = f"{globals.emoji_options[index]} {questions[cur_index]['options'][index]}", value = '** **', inline = False)
    elif q_type == "phone":
        cur_q_embed.description = "Answer in the format +X XXX XXXX, starting with your country code.\n Example: +1 123 123 1234\n If you need help, you can find your country code here: https://countrycode.org"

    return cur_q_embed, q_type

# Description: Searches the saved responses for the user. 
# If not found, appends them to the responses. If found, checks if they already submitted this form
def get_user(user, form_index):
    user_submitted = False
    #search for the user
    try:
        target = next(item for item in globals.local_responses if ((item['user_id'] == user.id) and (item['form_id'] == form_index))) 
    except:
        #create a new user with empty responses
        print("not found")
        # append to database
        globals.local_responses.append({'form_id': form_index, 
                                        'username': str(user), 
                                        'user_id': str(user.id), 
                                        'responses': [], 
                                        'response_ids': []})
        #print("appended: ", responses)
        # initialize a new tracker item
        globals.trackers[user.id] = {'form_started': False,
                            'response_index': len(globals.local_responses) - 1,
                            'confirmation_id': 0,
                            'mc_ids': []}
    else:
        user_submitted = True
        # # get index
        # user_index = globals.local_responses.index(target)
        # #print("found at index ", globals.user_index) 
        # globals.trackers[user.id]['response_index'] = user_index

        # # check if the form has already been completed by them
        # if len(globals.local_responses[user_index]['responses']) >= len(globals.questions):
        #     user_submitted = True
    
    return user_submitted
        

# Description: Saves the received response
def set_response(response, response_id, author, index):    
    print(f"response: {response}, author: {author}, author id: {author.id}")

    #set response & id
    user_index = globals.trackers[author.id]['response_index']
    globals.local_responses[user_index]['responses'].append(response)
    globals.local_responses[user_index]['response_ids'].append(response_id)
    #print("🔴 set: ", globals.local_responses)

# Description: Overwrites the old message with the new message
# Uses message ids to determine where to overwrite the message
def edit_response(old_confirmation, edited_response, new_response_id, author_id):
    # get the user index (in the responses)
    user_index = globals.trackers[author_id]['response_index']
    form_id = globals.local_responses[user_index]['form_id']
    questions = globals.local_forms[form_id]["Formfields"]
    # get the question index
    try:
        q_index = globals.local_responses[user_index]['response_ids'].index(new_response_id)
    except:
        print("question id not found")
   
    # get the question type
    question_type = questions[q_index]['input_type']   
    #print("🔴 edited question type: ", question_type)

    # validate response and grab the message content
    if question_type == "multiple choice":
        valid_response = True
        # get the index of the emoji
        emoji_index = globals.emoji_options.index(str(edited_response.emoji))
        tot_options = len(questions[q_index]['options'])

        #check that index is valid
        if emoji_index >= tot_options:
            print(f"invalid option {emoji_index} selected")
            return

        # use the emoji index to grab the corresponding option and set that as the new message
        new_response = questions[q_index]['options'][emoji_index]      
    else:
        if question_type == "email" or question_type == "phone" or question_type == "number":
            valid_response = validate_response(edited_response.content, question_type)

            if valid_response == False:
                return(None, valid_response)
        else:
            # If the q_type isn't any of the above, then it's a text response
            # Text responses are always valid 
            valid_response = True    

        new_response = edited_response.content

    # write over the response      
    globals.local_responses[user_index]['responses'][q_index] = str(new_response)

    #edit the confirmation message (if form was completed)
    if old_confirmation != None:
        #print("old confirmation: ", old_confirmation)
        new_confirmation = old_confirmation.embeds[0]
        new_confirmation.set_field_at(index = q_index, name = questions[q_index]['question'], value = new_response, inline = False)
    else:
        new_confirmation = None
    return new_confirmation, valid_response
    
# Description: Creates a confirmation message. Summarizes questions and answers
def end_form(user):
    user_index = globals.trackers[user.id]['response_index']
    form_id = globals.local_responses[user_index]['form_id']
    questions = globals.local_forms[form_id]["Formfields"]
    # create a confirmation embed
    confirmation_embed = discord.Embed(title = 'Confirm your answers', description = 'React with ✅ to submit.\n If you need to edit your answers, go back and do so, then come back here.', color = globals.form_color)
    # add questions and answers to the embed
    for item in range(len(questions)):
        confirmation_embed.add_field(name = questions[item]['question'], value = globals.local_responses[user_index]['responses'][item], inline = False)
    
    return confirmation_embed

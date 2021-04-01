import discord
import os
import json
import globals

intents = discord.Intents().all()
intents.reactions = True
client = discord.Client(intents = intents)

# Description: Gets the form details (eg. form name)
def get_form_specs():
    # get channel to send alerts to
    alert_channel_id = 824348394411262013
    # get form name
    form_name = "Event Registration"
    #form_alert_channel = client.get_channel(alert_channel_id)

    return alert_channel_id, form_name

# Description: Gets the questions and responses from the database
def get_form():
    # get questions
    with open("dummy_questions.json", "r") as q:
        globals.questions = json.load(q)
        q_count = len(globals.questions)
    
    # get responses
    with open('dummy_responses.json', 'r') as r:
        globals.responses = json.load(r)
    
    return q_count

# Description: Fetches the current question to create an embedded question message
def get_question(cur_index):
    # get question type
    q_type = globals.questions[cur_index]['input_type']
    # The process of making the embed is the same, whether the q_type is text or multi-choice
    cur_q_embed = discord.Embed(title = globals.questions[cur_index]['question'], description = globals.questions[cur_index]['description'], color = globals.form_color) 

    # check if we have an m/c question
    if q_type == "multiple choice":
        globals.tot_options = len(globals.questions[cur_index]['options'])

        # add m/c instructions to question description
        cur_q_embed.description += "\nAnswer by reacting with the corresponding emoji."

        # iterate through the options and emojis, adding them to the embed
        for index in range(globals.tot_options):
            cur_q_embed.add_field(name = f"{globals.emoji_options[index]} {globals.questions[cur_index]['options'][index]}", value = '** **', inline = False)

    return cur_q_embed, q_type

# Description: Searches the saved responses for the user. 
# If not found, appends them to the responses. If found, checks if they already submitted this form
def get_user(user):
    #search for the user
    try:
        target = next(item for item in globals.responses if item['username'] == str(user))      
    except:
        #create a new user with empty responses
        print("not found")
        # append to database
        globals.responses.append({'username': str(user), 'user_id': str(user.id), 'responses': [], 'response_ids': [], 'form_submitted': "false" })
        #print("appended: ", responses)

        globals.user_index = len(globals.responses) - 1
    else:
        # get index
        globals.user_index = globals.responses.index(target)
        print("found at index ", globals.user_index) 
        # if user exists, check if they've already submitted a form
        if globals.responses[globals.user_index]['form_submitted'] == "true":
            print("User has already submitted a form")
            globals.form_submitted = True
            return

# Description: Saves the received response
def set_response(response, response_id, author, index):    
    print(f"response: {response}, author: {author}, author id: {author.id}")

    #set response & id
    globals.responses[globals.user_index]['responses'].append(response)
    globals.responses[globals.user_index]['response_ids'].append(response_id)
    #print("set: ", responses)

# Description: Overwrites the old message with the new message
# Uses message ids to determine where to overwrite the message
def edit_response(old_confirmation, edited_response, question_type):    
    #grab the message and id
    if question_type == "text":
        new_response = edited_response.content
        new_response_id = edited_response.id

    elif question_type == "multiple choice":
        # get the index
        emoji_index = globals.emoji_options.index(str(edited_response.emoji))

        #check that index is valid
        if emoji_index >= globals.tot_options:
            print(f"invalid option {emoji_index} selected")
            return
        
        # get the id
        new_response_id = edited_response.message.id

        # find the question index
        for index in range(len(globals.questions)):
            if globals.questions[index]['question_id'] == new_response_id:
                q_index = index

        # grab the corresponding option and set that as the new message
        new_response = globals.questions[q_index]['options'][emoji_index]       

    # search responses for corresponding id
    try:
        for item in globals.responses[globals.user_index]['response_ids']:
            if item == new_response_id:
                target = item
                target_index = globals.responses[globals.user_index]['response_ids'].index(target)

    except:
        print("id not found")
    else:
        print(f"id found at index {target_index}")

        # write over the response      
        globals.responses[globals.user_index]['responses'][target_index] = str(new_response)

        #edit the confirmation message
        print("🔴 old confirmation: ", old_confirmation)
        new_confirmation = old_confirmation.embeds[0]
        new_confirmation.set_field_at(index = target_index, name = globals.questions[target_index]['question'], value = new_response, inline = False)
        return new_confirmation
    
# Description: Creates a confirmation message. Summarizes questions and answers
def end_form():
    # create a confirmation embed
    confirmation_embed = discord.Embed(title = 'Confirm your answers', description = 'React with ✅ to submit.\n If you need to edit your answers, go back and do so, then come back here.', color = globals.form_color)
    # add questions and answers to the embed
    for item in range(len(globals.questions)):
        confirmation_embed.add_field(name = globals.questions[item]['question'], value = globals.responses[globals.user_index]['responses'][item], inline = False)
    
    return confirmation_embed

# Description: Writes the responses to the database, creates a submission confirmation message for the user and form creator
def submit_responses(user):
    globals.form_started = False
    globals.form_submitted = True

    # flag the user as haven already responded
    globals.responses[globals.user_index]['form_submitted'] = "true"

    # write to the database
    with open('dummy_responses.json', 'w') as w:
        json.dump(globals.responses, w)
    
    #make submission confirmation for the user
    submission_alert_user = discord.Embed(title = 'Form submitted', description = 'You can view and manage your responses here: <insert link>', color = globals.form_color)

    # make a submission confirmation for the form creator
    submission_alert_creator = discord.Embed(title = f'{user} has submitted a form', description = 'To manage your forms, click here: <insert link>', color = globals.form_color)
    submission_alert_creator.add_field(name = 'Form:', value = globals.form_name, inline = False)

    return submission_alert_user, submission_alert_creator
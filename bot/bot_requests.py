# Functions that interact with the backend go here

import discord
import os
import json
import requests
import globals

PARAMS = {}
# API endpoints
GET_FORMS_URL = "http://localhost:8000/api/bot/forms" # questions
GET_RESPONSES_URL = "http://localhost:8000/api/bot/form/response/" # responses we receive from database
POST_RESPONSES_URL = "http://localhost:8000/api/bot/response/" # responses we send to database

# API key

# keep performing get requests to get the most up to date data (querying mechanisms)

# Description: Gets the forms from the database
def get_forms():
    # get forms (tmp; for local testing)
    #with open("dummy_questions.json", "r") as f:
    #    globals.forms= json.load(f)

    # # get forms from database
    get_forms = requests.get(url = GET_FORMS_URL, params = PARAMS)
    print(get_forms.json())
    globals.forms = get_forms.json()

# Description: Gets the responses from the database
def get_responses(form_name):
    # get responses (tmp; for local testing)
    with open('dummy_responses.json', 'r') as r:
        globals.local_responses = json.load(r)

    # get responses from database (specific form)
    #get_responses = requests.get(url = GET_RESPONSES_URL, params = PARAMS)
    #db_responses = []
    # api/bot/form/<userid>/<formName> 
    # Response 
    # User has not responded 
    # # fill a local array with the database responses
    # globals.local_responses = []

    # for item in db_responses:
    #     responses = list(item["Response"].values()) # grab the responses
    #     globals.local_responses.append({'form_id': item['form_id'], 'username': "", 'user_id': item['user_id'], 'responses': responses, 'response_ids': []})

# Description: Writes the responses to the database, creates a submission confirmation message for the user and form creator
def submit_responses(user):
    globals.form_started = False

    # write to the database (tmp; for local testing)
    with open('dummy_responses.json', 'w') as w:
        json.dump(globals.local_responses, w)

    # # format responses to send to database
    tmp_qs = []
    db_responses = []

    for item in globals.questions:
         tmp_qs.append(item['question'])

    for item in globals.local_responses:
         tmp_responses = {key:value for key, value in zip(tmp_qs, item['responses'])}
         db_responses.append({"form_id": item['form_id'], "user_id": item['user_id'], "Response": tmp_responses})
    
    print(db_responses)
    # # send post request and save response
    # post_request = requests.post(url = POST_RESPONSES_URL+str(FormName), data = db_responses)
    
    
    #make submission confirmation for the user
    submission_alert_user = discord.Embed(title = 'Form submitted', description = 'You can view and manage your responses here: <insert link>', color = globals.form_color)

    # make a submission confirmation for the form creator
    submission_alert_creator = discord.Embed(title = f'{user} has submitted a form', description = 'To manage your forms, click here: <insert link>', color = globals.form_color)
    submission_alert_creator.add_field(name = 'Form:', value = globals.form_name, inline = False)

    return submission_alert_user, submission_alert_creator

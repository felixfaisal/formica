# Functions that interact with the backend go here

import discord
import os
import json
import requests
import globals

PARAMS = {}
# API endpoints
GET_FORMS_URL = "http://backend:8000/api/bot/forms/" # questions
GET_RESPONSES_URL = "http://backend:8000/api/bot/form/response/" # responses we receive from database
POST_RESPONSES_URL = "http://backend:8000/api/bot/response/" # responses we send to database

# API key

# keep performing get requests to get the most up to date data (querying mechanisms)

# Description: Gets the forms from the database
def get_forms(server_id):
    print("server id: ", server_id)
    # get forms (tmp; for local testing)
    # with open("dummy_questions.json", "r") as f:
    #   db_forms = json.load(f)
    
    # get forms from database
    get_forms = requests.get(url = GET_FORMS_URL+str(server_id), params={})
    print(get_forms.json())
    db_forms = get_forms.json()

    # format to local forms
    for item in db_forms:
        globals.local_forms[item['form_id']] = {"FormName": item["FormName"], 
                                                "Formfields": item["Formfields"], 
                                                "serverid": item["serverid"],
                                                "channel_id": 824348394411262013, # hard-coded; change once we get from frontend
                                                }
    print("finished retrieving forms")
    #print("🔴 local forms: ", globals.local_forms)

# Description: Gets the responses from the database
def get_responses(form_name):
    # get responses (tmp; for local testing)
    # with open('dummy_responses.json', 'r') as r:
    #     db_responses = json.load(r)

    # get responses from database (specific form)
    get_responses = requests.get(url = GET_RESPONSES_URL+str(form_name), params = PARAMS)
    db_responses = get_responses.json()

    #print("🔴 db responses: ", db_responses)
    # fill a local array with the database responses & reformat
    globals.local_responses = []

    for item in db_responses:
        responses = list(item["Response"].values()) # grab the responses
        globals.local_responses.append({'form_id': item['form_id'], 'username': "", 'user_id': item['user_id'], 'responses': responses, 'response_ids': []})
    
    #print("🔴 local responses: ", globals.local_responses)
    

# Description: Writes the responses to the database, creates a submission confirmation message for the user and form creator
def submit_responses(user, form_id):
    form_name = globals.local_forms[form_id]["FormName"]
    questions = globals.local_forms[form_id]["Formfields"]
    # # # format responses to send to database
    tmp_qs = []
    db_responses = []

    for item in questions:
          tmp_qs.append(item['question'])

    for item in globals.local_responses:
          tmp_responses = {key:value for key, value in zip(tmp_qs, item['responses'])}
          db_responses.append({"form_id": item['form_id'], "user_id": int(item['user_id']), "Response": json.dumps(tmp_responses)})

    # write to the database (tmp; for local testing)
    # with open('dummy_responses.json', 'w') as w:
    #     json.dump(db_responses, w)
    
    print(db_responses[0])
    requestdata = json.dumps(db_responses[len(db_responses)-1])
    requestdatajson = json.loads(requestdata)
    print(requestdatajson['Response'])
    # # send post request and save response
    data = {
        'form_id':requestdatajson['form_id'],
        'user_id':requestdatajson['user_id'],
        'Response':requestdatajson['Response']
    }
    post_request = requests.post(url = POST_RESPONSES_URL, data = data)
    print('Post Request succesfully sent')
    print(post_request)
    
    #make submission confirmation for the user
    submission_alert_user = discord.Embed(title = 'Form submitted', description = 'You can view and manage your responses here: http://formica.centralindia.cloudapp.azure.com:3000/', color = globals.form_color)

    # make a submission confirmation for the form creator
    submission_alert_creator = discord.Embed(title = f'{user} has submitted a form', description = 'To manage your forms, click here: http://formica.centralindia.cloudapp.azure.com:3000/', color = globals.form_color)
    submission_alert_creator.add_field(name = 'Form:', value = form_name, inline = False)

    return submission_alert_user, submission_alert_creator

import re

# define regex patterns
email_regex = r"^\w+((-|\.|_)\w+)*\w*@\w+(-\w)?(\w*)?\.\w{2,3}(\.\w{2,3})?$"

phone_regex = r"^\+(\d{1,3}|(\d{1,2}\-\d{3,4}))\s(\d{3}\s){2}\d{4}$" # follows the ITU format for international phone numbers (+X XXX XXX XXX)

number_regex = r"\d+"

def validate_response(response, input_type):
    if input_type == "email":
        #print("email:", response)
        return bool(re.match(email_regex, response))
    elif input_type == "phone":
        #print("phone:", response)
        return bool(re.match(phone_regex, response))
    elif input_type == "number":
        #print("number:", response)
        return bool(re.match(number_regex, response))

# -------- quick testing ----------- #
# valid_response = validate_response("nhi@gmail.com", "email")
# print(valid_response)

# valid_response = validate_response("+1 604 441 3471", "phone")
# print(valid_response)

# valid_response = validate_response("3471", "number")
# print(valid_response)
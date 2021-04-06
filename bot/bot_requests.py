# practice GET & POST requests
# following: https://www.geeksforgeeks.org/get-post-requests-using-python/

import requests

# API endpoint
URL = ""

# API key

# define params dict for the params that we need to send to the API
PARAMS = {}

# send get request and save response as response obj
get_request = requests.get(url = URL, params = PARAMS)

# extract data in json
data = get_request.json()

# keep performing get requests to get the most up to date data (querying mechanisms)

# send post request save response
post_request = requests.post(url = URL, data = data)

import requests
import re
import os

from requests.exceptions import HTTPError

BASE_URL = r"https://random-word-api.herokuapp.com/"
api_key = None

debug = True

with open("api_key.txt","r") as f:
    api_key = f.readlines()[0]

def get_random_from_api():
    response = None
    try:
        response = requests.get(BASE_URL+"word?key={}&number={}".format(api_key,1))        
        response.raise_for_status()
    except HTTPError as http_err:
        print("HTTP error occured: {}".format(http_err))
    except Exception as err:
        print("Error occured: {}".format(err))
    else:
        print("Fetching new random word from URL = {}".format(BASE_URL))
        if debug:            
            print("Success")
        return re.sub('[\[\]"]','',"".join(response.content.decode("utf-8")))
    return None

if __name__ == "__main__":    
    # resp = get_random_from_api()
    # print(resp)
    # print(repr(resp))
    # print(type(resp))
    # print(len(resp))
    print(api_key)
    print(type(api_key))
    print(len(api_key))
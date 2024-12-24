import requests
import os

from pprint import pprint

# https://api.restful-api.dev/objects

def get_cellphones ():
    id =input("\n\nenter id:\n")
    url = f"{os.getenv("API_URL")}/objects/{id}"
    data = requests.get(url)

    pprint(data.json())

if __name__ == "__main__" :
    get_cellphones()
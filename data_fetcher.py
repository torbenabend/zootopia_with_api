import requests
import os
from dotenv import load_dotenv


# LOAD ENVIRONMENT VARIABLES
load_dotenv()
os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
    }
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY}, timeout=5)
    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code, response.text)
    return response.json()

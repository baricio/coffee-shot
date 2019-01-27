import json
import os
import random
import requests
from dotenv import load_dotenv
from os.path import join, dirname

with open('choices.json', encoding='utf-8') as choices_file:
    choices = json.load(choices_file)

with open('phrases.json', encoding='utf-8') as phrases_file:
    phrases = json.load(phrases_file)

max_range_choices = len(choices)
max_range_phrases = len(phrases)

lucky_number = random.randint(1,max_range_choices) - 1
phrase_number = random.randint(1,max_range_phrases) - 1

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

content = {"attachments": [{
    "pretext": phrases[phrase_number]["text"], 
    "text":choices[lucky_number]["name"] + " <"+ choices[lucky_number]["login"] +"> vai fazer o café :coffee: :tada: <@here>",
    "color": "danger",
    }]
}
webhook_url  = os.environ.get("WEBHOOK_URL")

response = requests.post(
    webhook_url, data=json.dumps(content),
    headers={'Content-Type': 'application/json'}
)

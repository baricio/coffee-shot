import json
import os
import random
import requests
from dotenv import load_dotenv
from os.path import join, dirname

class LuckRoulette:

    def __init__(self):
        self.choices = self.getChoices()
        self.phrases = self.getPhrases()
        self.lucky_number = -1
        self.phrase_number = -1

    def raffle(self):
        self.getLuckyNumber()
        self.sendToWebhook()

    def getChoices(self):
        with open('choices.json', encoding='utf-8') as choices_file:
            choices = json.load(choices_file)
            return choices

    def getPhrases(self):
        with open('phrases.json', encoding='utf-8') as phrases_file:
            phrases = json.load(phrases_file)
            return phrases

    def getLuckyNumber(self):
        max_range_choices = len(self.choices)
        max_range_phrases = len(self.phrases)
        self.lucky_number = random.randint(1,max_range_choices) - 1
        self.phrase_number = random.randint(1,max_range_phrases) - 1

    def getContent(self):
        content = {"attachments": [{
            "pretext": self.phrases[self.phrase_number]["text"], 
            "text":self.choices[self.lucky_number]["name"] + " <"+ self.choices[self.lucky_number]["login"] +"> vai fazer o café :coffee: :tada: <@here>",
            "color": "danger",
            }]
        }
        return content

    def sendToWebhook(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)

        webhook_url  = os.environ.get("WEBHOOK_URL")

        response = requests.post(
            webhook_url, data=json.dumps(self.getContent()),
            headers={'Content-Type': 'application/json'}
        )

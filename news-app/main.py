import requests
from datetime import datetime, timedelta
from random import randrange
from typing import Optional
from fastapi import FastAPI

HackerNewsBaseURL = "https://hacker-news.firebaseio.com/v0/"


def getMaxItem():
    HackerNewsMaxItemURL = HackerNewsBaseURL + "maxitem.json"
    response = requests.get(HackerNewsMaxItemURL)
    response_json = response.json()
    return response_json


def getItem(item_id):
    HackerNewsItemURL = HackerNewsBaseURL + "item/" + str(item_id) + ".json"
    response = requests.get(HackerNewsItemURL)
    response_json = response.json()
    return response_json

def getRandomStory():
    max_story = getMaxItem()
    random_story = randrange(1, int(max_story) + 1)
    random_story_item = getItem(random_story)
    return random_story_item


app = FastAPI()

@app.get("/")
def read_root():
    ret_random_story = getRandomStory()
    return ret_random_story
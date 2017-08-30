#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json

import requests
from bs4 import BeautifulSoup
from flask import current_app

import memory.data as data
from memory.extensions.flasksqlalchemy import db
from memory.models.post import Post
from memory.models.twitter import Twitter
from memory.models.hollow import Hollow
from memory.models.comment import Comment
from memory.models.via import Via


DOUBAN_HOLLOW_TOPIC = "https://www.douban.com/group/topic/34289325/"

def parse_date(time_str):
    """
    :param time_str: like "/Date(1453196817000)/"
    :return: datetime
    """
    timestamp = int(time_str[6:-2])
    return datetime.datetime.fromtimestamp(timestamp / 1e3)


def load_hollows():
    response = requests.get(DOUBAN_HOLLOW_TOPIC)
    soup = BeautifulSoup(response.text, 'html.parser')

    for ul_tag in soup.find_all('ul', { 'class': "topic-reply" }):
        for li_tag in ul_tag.find_all('li'):
            hollow = Hollow()
            hollow.external_id = li_tag['id']
            
            # handle span tag - via field
            span_tag = li_tag.find('span', { 'class': "via" })
            

    
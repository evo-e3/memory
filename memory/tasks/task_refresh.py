#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

import datetime
import json

import requests
from flask import current_app

import memory.data as data
from memory.extensions.flasksqlalchemy import db
from memory.models.post import Post
from memory.models.twitter import Twitter
from memory.models.hollow import Hollow
from memory.models.comment import Comment


def refresh_posts():
    pass

    
def refresh_twitters():
    pass

def refresh_hollows():
    pass

def refresh_comments():
    pass

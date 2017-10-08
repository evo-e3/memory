#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from memory.models.post import Post
from memory.models.twitter import Twitter
from memory.models.hollow import Hollow
from memory.models.comment import Comment
from sqlalchemy import and_


def get_posts():
    return Post.query.all()

def get_latest_posts(cnt=10):
    return Post.query.order_by(Post.date_created.desc()).limit(cnt).all()

def get_post(post_id):
    return Post.query.get(post_id)


def get_twitters():
    return Twitter.query.all()

def get_latest_twitters(cnt=10):
    return Twitter.query.order_by(Twitter.date_created.desc()).limit(cnt).all()

def get_twitter(twitter_id):
    return Twitter.query.get(twitter_id)

def get_hollows():
    return Hollow.query.all()

def get_latest_hollows(cnt=10):
    return Hollow.query.order_by(Hollow.date_created.desc()).limit(cnt).all()

def get_hollow(hollow_id):
    return Hollow.query.get(hollow_id)

def get_comments(cnt=20):
    return Comment.query.order_by(Comment.date_created.desc()).limit(cnt).all()

def get_comments_more(start, cnt=20):
    return Comment.query.filter(Comment.id < start).order_by(Comment.date_created.desc()).limit(cnt).all()
    
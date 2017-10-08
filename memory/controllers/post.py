#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

import lxml.html
from flask import render_template, Blueprint, json, abort

import memory.data as data
from memory.extensions.flasksqlalchemy import db

bp_post = Blueprint('post', __name__)


@bp_post.route('/')
def latest_posts():
    posts = data.get_latest_posts(10)
    return render_template('latest.html')


@bp_post.route('/posts')
def posts():
    posts = data.get_posts()
    return render_template('posts.html', posts=posts)



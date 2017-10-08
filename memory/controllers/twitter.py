#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

import lxml.html
from flask import render_template, Blueprint, json, abort

import memory.data as data
from memory.extensions.flasksqlalchemy import db

bp_twitter = Blueprint('twitter', __name__)


@bp_twitter.route('/')
def latest_twitters():
    twitters = data.get_latest_twitters(10)
    return render_template('latest.html')


@bp_twitter.route('/twitters')
def twitters():
    twitters = data.get_twitters()
    return render_template('twitters.html', twitters=twitters)



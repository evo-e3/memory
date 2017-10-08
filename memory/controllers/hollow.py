#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

import lxml.html
from flask import render_template, Blueprint, json, abort

import memory.data as data
from memory.extensions.flasksqlalchemy import db

bp_hollow = Blueprint('hollow', __name__)


@bp_hollow.route('/')
def latest_hollows():
    hollows = data.get_latest_hollows(10)
    return render_template('latest.html')


@bp_hollow.route('/hollows')
def hollows():
    hollows = data.get_hollows()
    return render_template('hollows.html', hollows=hollows)



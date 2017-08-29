#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import current_app, request, abort, jsonify

import memory.tasks.task as task

bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


def login():
    if current_app.config['USERNAME'] != request.args.get('username') or current_app.config['PASSWORD'] != request.args.get('password'):
        abort(404)


bp_admin.before_request(login)


@bp_admin.route('/refresh_posts')
def refresh_posts():
    return jsonify(task.refresh_posts())


@bp_admin.route('/refresh_tweets')
def refresh_twitters():
    return jsonify(task.refresh_twitters())

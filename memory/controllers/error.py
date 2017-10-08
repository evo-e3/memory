#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from flask import render_template, Blueprint

bp_error = Blueprint('error', __name__, template_folder="../templates")


@bp_error.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error)


@bp_error.app_errorhandler(500)
def server_error(error):
    return render_template('50x.html', error=error)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

import logging
from logging.handlers import RotatingFileHandler


def init_logger(app):
    handler = RotatingFileHandler('logs/memory.log', maxBytes=1024 * 1024 * 2, backupCount=2)
    logging_format = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

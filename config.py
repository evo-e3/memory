#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
APP_PATH = os.path.dirname(os.path.abspath(__file__)) + '/memory'
HOST = '0.0.0.0'
PORT = 7000
DEBUG = True
SQLALCHEMY_DATABASE_URI='sqlite:///' + APP_PATH + '/db/memory.db'

USERNAME='itabas'
PASSWORD='123456'
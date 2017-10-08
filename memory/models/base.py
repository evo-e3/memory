#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from memory.extensions.flasksqlalchemy import db

class Base(db.Model):

    __abstract__  = True
    
    __doc__ = '''
    Define a base model for other database tables to inherit:
    Contains id(integar), date_created(datetime), date_modified(datetime) three columns
    '''

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp())
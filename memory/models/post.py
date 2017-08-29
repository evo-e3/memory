#!/usr/bin/env python
# -*- coding: utf-8 -*-

from memory.extensions.flasksqlalchemy import db

class Post(Base):

    __tablename__ = 'm_post'
    
    title           = db.Column(db.String(256), nullable=False)
    content         = db.Column(db.Text, nullable=True)
    source_id       = db.Column(db.Integer, nullable=False)
    external_id     = db.Column(db.Integer, nullable=True)
    external_addr   = db.Column(db.String(512), nullable=True)
    external_date   = db.Column(db.DateTime,  default=db.func.current_timestamp())
    ext_1           = db.Column(db.String(256), nullable=False)
    ext_2           = db.Column(db.String(512), nullable=False)
    status          = db.Column(db.SmallInteger, default=1)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from memory.extensions.flasksqlalchemy import db

class Source(Base):

    __tablename__ = 'm_source'
    
    name = db.Column(db.String(128), nullable=False)
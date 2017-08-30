#!/usr/bin/env python
# -*- coding: utf-8 -*-

from memory.extensions.flasksqlalchemy import db

class Via(Base):

    __tablename__ = 'm_via'
    
    name     = db.Column(db.String(64), nullable=True)
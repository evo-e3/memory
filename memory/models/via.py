#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>

from memory.extensions.flasksqlalchemy import db
from memory.models.base import Base

class Via(Base):

    __tablename__ = 'm_via'
    
    name     = db.Column(db.String(64), nullable=True)
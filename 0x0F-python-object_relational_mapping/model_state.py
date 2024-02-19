#!/usr/bin/python3

from sqlalchemy import MetaData, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

import sys
metaD = MetaData()

Base = declarative_base()

class State(Base):
	__tablename__ = "states"
	
	id = Column(Integer, nullable=False, unique=True, primary_key=True)
	name = Column(String(128), nullable=False)
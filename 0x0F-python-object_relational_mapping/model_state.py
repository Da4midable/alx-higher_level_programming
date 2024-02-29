#!/usr/bin/python3
"""Script defines class State and an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with maximum 128
characters and can’t be null
"""

from sqlalchemy import MetaData, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

import sys
metaD = MetaData()

Base = declarative_base()


class State(Base):
    """
    State is a class with id and name attributes of each state
    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

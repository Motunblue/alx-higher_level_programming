#!/usr/bin/python3
"""
    lists all State objects from a database
"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

rows = session.query(State).order_by(State.id.asc()).all()

for row in rows:
    print("{}: {}".format(row.id, row.name))

session.close()

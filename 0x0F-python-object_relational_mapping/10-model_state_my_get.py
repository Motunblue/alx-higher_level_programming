#!/usr/bin/python3
"""
    lists all State objects from a database
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).filter(State.name == sys.argv[4]).first()

    if row is not None:
        print("{}".format(row.id))
    else:
        print("Not found")

    session.close()

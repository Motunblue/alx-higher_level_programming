#!/usr/bin/python3
"""
    lists all State objects from a database
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy import collate

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    print('{}'.format(new.id))

    session.close()

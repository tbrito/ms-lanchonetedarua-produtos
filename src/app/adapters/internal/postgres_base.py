from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class PostgresContext:
    def __init__(self, database_uri):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    @property
    def session(self):
        return self._session
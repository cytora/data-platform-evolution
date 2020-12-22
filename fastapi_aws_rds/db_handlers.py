from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import PostgresConfiguration
from models import ToidsTable
#from sqlalchemy.exc import InvalidRequestError


class PosgresHandler:
    def __init__(self, db_string):
        self.engine = create_engine(db_string)
        self.session = sessionmaker(bind=self.engine)
        self.session = self.session()

    # --------------------------------------------------TOIDS----------------------------------------------------

    def get_toid_by_uid(self, uid: str):
        toid = self.session.query(ToidsTable).filter(
            ToidsTable.toid_uid == uid).all()
        if toid:
            return toid


pg_handler = PosgresHandler(PostgresConfiguration().postgres_db_path)

#import requests
from db_handlers import pg_handler
#from datetime import datetime


def get_toid_by_uid(uid: str):
    toid_data = pg_handler.get_toid_by_uid(uid)
    if toid_data:
        return toid_data[0]

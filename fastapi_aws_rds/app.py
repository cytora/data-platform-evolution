import uvicorn
from fastapi import FastAPI
import time
from datetime import datetime

from handlers import get_toid_by_uid
from settings import APP_PORT

app = FastAPI()


@app.get('/toid/{toid_uid}', summary='get TOID by toid_uid', tags=['TOIDs'])
async def get_user(toid_uid: str):
    now = datetime.utcnow()
    init = time.perf_counter()
    toid_data = get_toid_by_uid(toid_uid)
    if not toid_data:
        toid_data = 'Could not find TOID in database'
    toid_resultset = dict(toid_data=toid_data)
    cost = time.perf_counter() - init
    toid_resultset['exec_cost_seconds'] = cost
    return toid_resultset #dict(toid_data=toid_data)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(APP_PORT))

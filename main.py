from datetime import datetime, timedelta

import requests
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
lite_db = dict()


def is_company_on_nalogru(data: str):
    response = requests.post('https://rmsp.nalog.ru/search-proc.json', {"query": data}).json()
    if 'data' in response:
        if data in (response['data'][0]['inn'], response['data'][0]['ogrn']):
            return True
        else:
            return False

def db_by_time(minutes=5):
    d = []
    t = timedelta(minutes=minutes)
    for key, v in lite_db.items():
        if (datetime.now() - t) < datetime.fromtimestamp(int(v[1])):
            d.append([key, v[0]])
    return d

@app.post("/company")
def find_company(data: dict):
    check = False
    if 'query' in data:
        check = is_company_on_nalogru(data['query'])
        lite_db[data['query']] = [check, datetime.now().timestamp()]
    return {'data': check}

@app.get("/company")
def get_company():
    data = db_by_time()
    return {'data': data}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8080)




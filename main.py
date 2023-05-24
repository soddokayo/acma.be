from fastapi import FastAPI
from pydantic import BaseModel
import secrets, os, json
from pymongo import MongoClient
from dotenv import load_dotenv

app = FastAPI()

load_dotenv(verbose=True)
mongoURL = os.getenv('MONGODB_URL')

db_conn = MongoClient(mongoURL)
print('DB connected: ', db_conn.acma)

class Memo(BaseModel):
    author: str
    text: str

@app.post("/api/memo/create")
async def create_memo(memo: Memo):
    token = secrets.token_hex(nbytes=16)
    fpath = "./memo/"+token
    while os.path.isfile(fpath):
        token = secrets.token_hex(nbytes=16)
        fpath = "./memo/"+token

    contents = {
        "id": token,
        "author": memo.author,
        "text": memo.text,
        "catogry": None
    }
    fout = open(fpath, 'w')
    fout.write(json.dumps(contents, ensure_ascii=False))
    fout.close()
    return memo

@app.get("/api/memo")
async def list_memo(useFile:bool=False):
    if useFile:
        dpath = './memo/'
        flist = os.listdir(dpath)

        memoList = []
        for f in flist:
            fpath = dpath+f
            fin = open(fpath, 'r')
            contents  = json.load(fin)
            memoList.append(contents)

        return memoList
    else:
        return []

@app.get("/api/memo/{id}")
async def list_memo(id: str):
    dpath = './memo/'
    flist = os.listdir(dpath)
    
    memoList = []
    for f in flist:
        fpath = dpath+f
        fin = open(fpath, 'r')
        contents  = json.load(fin)
        memoList.append(contents)

    return memoList
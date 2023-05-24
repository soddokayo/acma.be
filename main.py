from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
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
    id: str | None = None
    author: str
    text: str
    category: str | None = None

@app.post("/api/memo") # Create
async def create_memo(memo:Memo, useFile:bool=False):
    if useFile:
        id = secrets.token_hex(nbytes=16)
        fpath = "./memo/"+id
        while os.path.isfile(fpath):
            id = secrets.token_hex(nbytes=16)
            fpath = "./memo/"+id

        contents = {
            "id": id,
            "author": memo.author,
            "text": memo.text,
            "catogry": None
        }
        fout = open(fpath, 'w')
        fout.write(json.dumps(contents, ensure_ascii=False))
        fout.close()
        return contents
    else:
        return None

@app.get("/api/memo") # Read All
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
            fin.close()

        return jsonable_encoder(memoList)
    
    else: # use db
        return None

@app.get("/api/memo/{id}") # Read One
async def read_memo(id:str, useFile:bool=False):
    if useFile:
        fpath = './memo/'+id
        
        if os.path.isfile(fpath):
            fin = open(fpath, 'r')
            contents  = json.load(fin)
            return jsonable_encoder(contents)
        else:
            return None
    
    else: # use db
        return None
    
@app.put("/api/memo/{id}") # Update
async def update_memo(id:str, memo:Memo, useFile:bool=False):
    if useFile:
        fpath = "./memo/"+id
        if os.path.isfile(fpath):
            os.remove(fpath)

        contents = {
            "id": id,
            "author": memo.author,
            "text": memo.text,
            "catogry": None
        }
        if not os.path.isfile(fpath):
            fout = open(fpath, 'w')
            fout.write(json.dumps(contents, ensure_ascii=False))
            fout.close()
            return contents
        else:
            return None
    else:
        return None
    
@app.delete("/api/memo/{id}") # Delete
async def delete_memo(id:str, useFile:bool=False):
    if useFile:
        fpath = './memo/'+id
        
        if os.path.isfile(fpath):
            os.remove(fpath)
            return {"msg" : "delete complete"}
        else:
            return None
    
    else: # use db
        return None
    
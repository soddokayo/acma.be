from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from model import Memo
from file_crud import create_memo_file, list_memo_file, read_memo_file, update_memo_file, delete_memo_file
import db_crud

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="build/static"))

@app.post("/api/memo") # Create
async def create_memo(memo:Memo, useFile:bool=False):
    if useFile: # use file
        return create_memo_file(memo)
    else: # use db
        return None

@app.get("/api/memo") # Read All
async def list_memo(useFile:bool=False):
    if useFile: # use file
        return list_memo_file()
    else: # use db
        return None

@app.get("/api/memo/{id}") # Read One
async def read_memo(id:str, useFile:bool=False):
    if useFile:
        return read_memo_file(id)
    else: # use db
        return None
    
@app.put("/api/memo/{id}") # Update
async def update_memo(id:str, memo:Memo, useFile:bool=False):
    if useFile:
        return update_memo_file(id, memo)
    else:
        return None
    
@app.delete("/api/memo/{id}") # Delete
async def delete_memo(id:str, useFile:bool=False):
    if useFile:
        return delete_memo_file(id)
    
    else: # use db
        return None
    
@app.get("/")
@app.get("/list")
@app.get("/create")
def index():
    return FileResponse("build/index.html")
from fastapi.encoders import jsonable_encoder
import secrets, os, json

from model import Memo, cats
from translate import translate
from classificate import classificate

def create_memo_file(memo:Memo): # Create
    id = secrets.token_hex(nbytes=16)
    fpath = "./memo/"+id
    while os.path.isfile(fpath):
        id = secrets.token_hex(nbytes=16)
        fpath = "./memo/"+id

    # 번역 및 분류
    text_en = translate(memo.text)
    category = classificate(text_en, cats)

    contents = {
        "id": id,
        "author": memo.author,
        "text": memo.text,
        "text_en": text_en,
        "category": category,
    }
    fout = open(fpath, 'w')
    fout.write(json.dumps(contents, ensure_ascii=False))
    fout.close()
    return contents

def list_memo_file(): # Read All
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

def read_memo_file(id:str): # Read One
    fpath = './memo/'+id
    
    if os.path.isfile(fpath):
        fin = open(fpath, 'r')
        contents  = json.load(fin)
        return jsonable_encoder(contents)
    else:
        return None

def update_memo_file(id:str, memo:Memo): # Update
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
    
def delete_memo_file(id:str): # Delete
    fpath = './memo/'+id
    
    if os.path.isfile(fpath):
        os.remove(fpath)
        return {"msg" : "delete complete"}
    else:
        return None
from pydantic import BaseModel

cats = ['music', 'computer', 'health', 'money', 'english']

class Memo(BaseModel):
    id: str | None = None
    author: str
    text: str
    category: str | None = None
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(verbose=True)
mongoURL = os.getenv('MONGODB_URL')

db_conn = MongoClient(mongoURL)
print('DB connected: ', db_conn.acma)
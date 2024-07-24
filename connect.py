import os
from peewee import MySQLDatabase
from dotenv import load_dotenv
import pymysql

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))
DB_USER = os.getenv('DB_USER')
DB_PASSWD = os.getenv('DB_PASSWD')

def create_database():
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD)
        conn.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.close()
    except Exception as e:
        print(f"Erro ao criar database: {e}")
    
create_database()
db = MySQLDatabase(database=DB_NAME, host=DB_HOST, port=DB_PORT,
                   user=DB_USER, passwd=DB_PASSWD)

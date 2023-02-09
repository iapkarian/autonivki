import sqlite3
from sqlite3 import Error


class BotDB:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT 'id' FROM 'user' WHERE 'user_telegram' = ?")

    def close(self):
        self.connection.close()

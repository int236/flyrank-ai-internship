import os
import time
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class PostgresRepository:
    def __init__(self):
        while True:
            try:
                self.conn = psycopg2.connect(os.getenv("DATABASE_URL"))
                break
            except psycopg2.OperationalError:
                print("Waiting for PostgreSQL...")
                time.sleep(2)

        self.cur = self.conn.cursor()

    def add_message(self, text):
        self.cur.execute(
            "INSERT INTO messages (message) VALUES (%s)",
            (text,)
        )
        self.conn.commit()

    def get_messages(self):
        self.cur.execute("SELECT * FROM messages")
        return self.cur.fetchall()
import sqlite3

class Database:
    def __init__(self, db_name='app.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_users_table()

    def create_users_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_user(self, email, password):
        try:
            query = 'INSERT INTO users (email, password) VALUES (?, ?)'
            self.conn.execute(query, (email, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verify_user(self, email, password):
        query = 'SELECT * FROM users WHERE email = ? AND password = ?'
        cursor = self.conn.execute(query, (email, password))
        return cursor.fetchone() is not None

    def close(self):
        self.conn.close()

    def get_all_users(self):
        query = 'SELECT id, email FROM users'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

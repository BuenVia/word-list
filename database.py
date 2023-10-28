import sqlite3

CREATE_NEW_DB = """CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    spa_word TEXT,
    eng_word TEXT,
    created_at REAL
);"""

INSERT_WORD = f"INSERT INTO words (spa_word, eng_word, created_at) VALUES (?, ?, ?);"
SELECT_ALL_WORDS = "SELECT * FROM words;"

connection = sqlite3.connect('./data.db')

def create_tables():
    with connection:
        connection.execute(CREATE_NEW_DB)

def insert_word(spa_text, eng_text, created_at):
    with connection:
        connection.execute(INSERT_WORD, (spa_text, eng_text, created_at))

def show_all_words():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_WORDS)
        return cursor.fetchall()
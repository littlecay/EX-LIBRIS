import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

# 添加状态字段
c.execute('''
CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY, title TEXT, author TEXT, publisher TEXT, category TEXT, quantity INTEGER, status TEXT, image BLOB)
''')

def add_book(title, author, publisher, category, quantity, status, image_path):
    with open(image_path, 'rb') as file:
        image_data = file.read()
    c.execute("INSERT INTO books (title, author, publisher, category, quantity, status, image) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (title, author, publisher, category, quantity, status, image_data))
    conn.commit()

def remove_book(book_id):
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()

def update_book(book_id, title, author, publisher, category, quantity, status):
    c.execute("UPDATE books SET title=?, author=?, publisher=?, category=?, quantity=?, status=? WHERE id=?",
              (title, author, publisher, category, quantity, status, book_id))
    conn.commit()

def search_books(query):
    c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR publisher LIKE ? OR category LIKE ?",
              (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
    return c.fetchall()

def get_book_image(book_id):
    c.execute("SELECT image FROM books WHERE id=?", (book_id,))
    result = c.fetchone()
    return result[0] if result else None

def display_books():
    c.execute("SELECT * FROM books")
    return c.fetchall()

def close_connection():
    conn.close()

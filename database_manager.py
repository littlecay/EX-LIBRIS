import sqlite3
from io import BytesIO

def create_connection():
    conn = sqlite3.connect('books.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publisher TEXT,
        category TEXT,
        quantity INTEGER,
        status TEXT,
        cover BLOB
    )
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, publisher, category, quantity, status, image_path):
    conn = create_connection()
    cursor = conn.cursor()

    with open(image_path, 'rb') as file:
        img_data = file.read()

    cursor.execute('''
    INSERT INTO books (title, author, publisher, category, quantity, status, cover)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, author, publisher, category, quantity, status, img_data))

    conn.commit()
    conn.close()

def get_book(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id, title, author, publisher, category, quantity, status, cover
    FROM books
    WHERE id = ?
    ''', (book_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def display_books():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, author, publisher, category, quantity, status, cover FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def get_book_image(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT cover FROM books WHERE id = ?', (book_id,))
    img_data = cursor.fetchone()[0]
    conn.close()
    return img_data

def update_book(book_id, title, author, publisher, category, quantity, status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE books
    SET title = ?, author = ?, publisher = ?, category = ?, quantity = ?, status = ?
    WHERE id = ?
    ''', (title, author, publisher, category, quantity, status, book_id))
    conn.commit()
    conn.close()

def remove_book(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()

def search_books(query):
    conn = create_connection()
    cursor = conn.cursor()
    search_query = f"%{query}%"
    cursor.execute('''
    SELECT id, title, author, publisher, category, quantity, status, cover
    FROM books
    WHERE title LIKE ? OR author LIKE ? OR publisher LIKE ? OR category LIKE ? OR status LIKE ?
    ''', (search_query, search_query, search_query, search_query, search_query))
    results = cursor.fetchall()
    conn.close()
    return results

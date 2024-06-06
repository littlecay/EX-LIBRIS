import tkinter as tk
from tkinter import ttk
from database_manager import create_table
from page_display_books import create_display_books_page
from page_add_book import create_add_book_page
from page_search_books import create_search_books_page
from page_copyright_info import create_copyright_info_page

# 创建数据库和表
create_table()

root = tk.Tk()
root.title("图书管理系统 V1.0.0")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# 创建各个页面
create_display_books_page(notebook)
create_add_book_page(notebook)
create_search_books_page(notebook)
create_copyright_info_page(notebook)

root.mainloop()

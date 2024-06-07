import tkinter as tk
from tkinter import ttk, messagebox, Label
from PIL import Image, ImageTk
import io
from database_manager import search_books, update_book, remove_book, get_book_image

def create_search_books_page(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text='查询图书')

    search_var = tk.StringVar()
    title_var = tk.StringVar()
    author_var = tk.StringVar()
    publisher_var = tk.StringVar()
    category_var = tk.StringVar()
    quantity_var = tk.StringVar()
    status_var = tk.StringVar()

    def search_and_display_books():
        search_results = search_books(search_var.get())
        list_books.delete(0, tk.END)
        for book in search_results:
            list_books.insert(tk.END, f"{book[0]}: {book[1]} - {book[2]} - {book[6]}")  # Display book ID, title, author, and status

    def show_book_details(event=None):
        selected = list_books.curselection()
        if selected:
            selected_book_id = int(list_books.get(selected[0]).split(":")[0])
            print(f"Selected book ID: {selected_book_id}")  # Debug print
            book = search_books(str(selected_book_id))
            print(f"Search results: {book}")  # Debug print
            if book:
                book = book[0]
                title_var.set(book[1])
                author_var.set(book[2])
                publisher_var.set(book[3])
                category_var.set(book[4])
                quantity_var.set(str(book[5]))
                status_var.set(book[6])

                img_data = get_book_image(selected_book_id)
                if img_data:
                    image = Image.open(io.BytesIO(img_data))
                    image = image.resize((200, 300), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                    label_image.config(image=photo)
                    label_image.image = photo  # keep a reference!
            else:
                messagebox.showerror("错误", "未找到选定的图书信息")

    def update_book_details():
        selected = list_books.curselection()
        if selected:
            selected_book_id = int(list_books.get(selected[0]).split(":")[0])
            update_book(selected_book_id, title_var.get(), author_var.get(), publisher_var.get(),
                        category_var.get(), quantity_var.get(), status_var.get())
            messagebox.showinfo("信息", "图书信息已更新")
            search_and_display_books()

    def delete_selected_book():
        selected = list_books.curselection()
        if selected:
            selected_book_id = int(list_books.get(selected[0]).split(":")[0])
            remove_book(selected_book_id)
            messagebox.showinfo("信息", "图书已删除")
            search_and_display_books()  # Refresh the list

    tk.Label(frame, text="搜索").grid(row=0, column=0)
    entry_search = tk.Entry(frame, textvariable=search_var)
    entry_search.grid(row=0, column=1)
    tk.Button(frame, text="搜索图书", command=search_and_display_books).grid(row=0, column=2)

    list_books = tk.Listbox(frame, height=10)
    list_books.grid(row=1, column=0, columnspan=3, sticky='nsew')
    list_books.bind('<<ListboxSelect>>', show_book_details)

    scrollbar = ttk.Scrollbar(frame, command=list_books.yview)
    scrollbar.grid(row=1, column=3, sticky='ns')
    list_books.config(yscrollcommand=scrollbar.set)

    # Display and edit book details
    label_image = Label(frame)
    label_image.grid(row=1, column=4, rowspan=6)

    tk.Label(frame, text="标题").grid(row=2, column=0)
    tk.Entry(frame, textvariable=title_var).grid(row=2, column=1, columnspan=2)
    tk.Label(frame, text="作者").grid(row=3, column=0)
    tk.Entry(frame, textvariable=author_var).grid(row=3, column=1, columnspan=2)
    tk.Label(frame, text="出版社").grid(row=4, column=0)
    tk.Entry(frame, textvariable=publisher_var).grid(row=4, column=1, columnspan=2)
    tk.Label(frame, text="分类").grid(row=5, column=0)
    tk.Entry(frame, textvariable=category_var).grid(row=5, column=1, columnspan=2)
    tk.Label(frame, text="数量").grid(row=6, column=0)
    tk.Entry(frame, textvariable=quantity_var).grid(row=6, column=1, columnspan=2)
    tk.Label(frame, text="状态").grid(row=7, column=0)
    tk.Entry(frame, textvariable=status_var).grid(row=7, column=1, columnspan=2)
    tk.Button(frame, text="更新图书", command=update_book_details).grid(row=8, column=0, columnspan=3)

    tk.Button(frame, text="删除选定图书", command=delete_selected_book).grid(row=8, column=4, columnspan=3)

    return frame

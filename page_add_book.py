import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from database_manager import add_book

def create_add_book_page(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text='添加图书')

    title_var = tk.StringVar()
    author_var = tk.StringVar()
    publisher_var = tk.StringVar()
    category_var = tk.StringVar()
    quantity_var = tk.StringVar()
    status_var = tk.StringVar()
    image_path = tk.StringVar()

    def choose_image():
        filename = filedialog.askopenfilename()
        image_path.set(filename)

    def submit_book():
        title = title_var.get()
        author = author_var.get()
        publisher = publisher_var.get()
        category = category_var.get()
        quantity = quantity_var.get()
        status = status_var.get()
        image = image_path.get()

        if title and author and publisher and category and quantity and status and image:
            try:
                add_book(title, author, publisher, category, quantity, status, image)
                messagebox.showinfo("成功", "图书添加成功！")
                title_var.set("")
                author_var.set("")
                publisher_var.set("")
                category_var.set("")
                quantity_var.set("")
                status_var.set("")
                image_path.set("")
            except Exception as e:
                messagebox.showerror("错误", f"无法添加图书: {e}")
        else:
            messagebox.showwarning("警告", "请填写所有字段并选择封面图片")

    tk.Label(frame, text="标题").grid(row=0, column=0)
    tk.Entry(frame, textvariable=title_var).grid(row=0, column=1)
    tk.Label(frame, text="作者").grid(row=1, column=0)
    tk.Entry(frame, textvariable=author_var).grid(row=1, column=1)
    tk.Label(frame, text="出版社").grid(row=2, column=0)
    tk.Entry(frame, textvariable=publisher_var).grid(row=2, column=1)
    tk.Label(frame, text="分类").grid(row=3, column=0)
    tk.Entry(frame, textvariable=category_var).grid(row=3, column=1)
    tk.Label(frame, text="数量").grid(row=4, column=0)
    tk.Entry(frame, textvariable=quantity_var).grid(row=4, column=1)
    tk.Label(frame, text="状态").grid(row=5, column=0)
    tk.Entry(frame, textvariable=status_var).grid(row=5, column=1)
    tk.Button(frame, text="选择封面", command=choose_image).grid(row=6, column=0, columnspan=2)
    tk.Button(frame, text="添加图书", command=submit_book).grid(row=7, column=0, columnspan=2)

    return frame

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Label
from PIL import Image, ImageTk
import io
from database_manager import add_book, update_book, remove_book, search_books, display_books, get_book_image, create_table

# 创建数据库和表
create_table()

root = tk.Tk()
root.title("图书管理系统 V1.0.0")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# 定义所有全局变量
title_var = tk.StringVar()
author_var = tk.StringVar()
publisher_var = tk.StringVar()
category_var = tk.StringVar()
quantity_var = tk.StringVar()
status_var = tk.StringVar()
image_path = tk.StringVar()

# 标签页1: 显示所有图书
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='显示图书')

scrollbar = ttk.Scrollbar(frame1, orient='vertical')
scrollbar.pack(side='right', fill='y')

canvas = tk.Canvas(frame1, yscrollcommand=scrollbar.set)
canvas.pack(side='left', fill='both', expand=True)
scrollbar.config(command=canvas.yview)

scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

def display_all_books():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    books = display_books()
    rows = len(books) // 3 + (1 if len(books) % 3 > 0 else 0)
    for i in range(rows):
        for j in range(3):
            if 3 * i + j < len(books):
                book = books[3 * i + j]
                img_data = book[7]  # Assuming that the image data is in the 8th field
                if img_data:
                    image = Image.open(io.BytesIO(img_data))
                    image = image.resize((200, 300), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(image)
                    panel = Label(scrollable_frame, image=photo)
                    panel.image = photo  # keep a reference!
                    panel.grid(row=i * 2, column=j, padx=10, pady=10)
                    Label(scrollable_frame, text=f"{book[1]}\n{book[6]}").grid(row=i * 2 + 1, column=j)

    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# 绑定鼠标滚轮事件
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

tk.Button(frame1, text="刷新图书列表", command=display_all_books).pack(fill='x')
display_all_books()  # 初始加载图书

# 标签页2: 添加图书
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='添加图书')

def choose_image():
    filename = filedialog.askopenfilename()
    image_path.set(filename)

def update_title_var(*args):
    title_var.set(title_entry.get())

def update_author_var(*args):
    author_var.set(author_entry.get())

def update_publisher_var(*args):
    publisher_var.set(publisher_entry.get())

def update_category_var(*args):
    category_var.set(category_entry.get())

def update_quantity_var(*args):
    quantity_var.set(quantity_entry.get())

def update_status_var(*args):
    status_var.set(status_entry.get())

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
            display_all_books()  # 更新显示图书列表
        except Exception as e:
            messagebox.showerror("错误", f"无法添加图书: {e}")
    else:
        messagebox.showwarning("警告", "请填写所有字段并选择封面图片")

# 添加初始化
tk.Label(frame2, text="标题").grid(row=0, column=0)
title_entry = tk.Entry(frame2, textvariable=title_var)
title_entry.grid(row=0, column=1)
title_entry.bind('<KeyRelease>', update_title_var)

tk.Label(frame2, text="作者").grid(row=1, column=0)
author_entry = tk.Entry(frame2, textvariable=author_var)
author_entry.grid(row=1, column=1)
author_entry.bind('<KeyRelease>', update_author_var)

tk.Label(frame2, text="出版社").grid(row=2, column=0)
publisher_entry = tk.Entry(frame2, textvariable=publisher_var)
publisher_entry.grid(row=2, column=1)
publisher_entry.bind('<KeyRelease>', update_publisher_var)

tk.Label(frame2, text="分类").grid(row=3, column=0)
category_entry = tk.Entry(frame2, textvariable=category_var)
category_entry.grid(row=3, column=1)
category_entry.bind('<KeyRelease>', update_category_var)

tk.Label(frame2, text="数量").grid(row=4, column=0)
quantity_entry = tk.Entry(frame2, textvariable=quantity_var)
quantity_entry.grid(row=4, column=1)
quantity_entry.bind('<KeyRelease>', update_quantity_var)

tk.Label(frame2, text="状态").grid(row=5, column=0)
status_entry = tk.Entry(frame2, textvariable=status_var)
status_entry.grid(row=5, column=1)
status_entry.bind('<KeyRelease>', update_status_var)

tk.Button(frame2, text="选择封面", command=choose_image).grid(row=6, column=0, columnspan=2)
tk.Button(frame2, text="添加图书", command=submit_book).grid(row=7, column=0, columnspan=2)

# 标签页3: 查询图书
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text='查询图书')

search_var = tk.StringVar()

def search_and_display_books():
    search_results = search_books(search_var.get())
    list_books.delete(0, tk.END)
    for book in search_results:
        list_books.insert(tk.END, f"{book[0]}: {book[1]} - {book[2]} - {book[6]}")  # Display book ID, title, author, and status

def show_book_details(event=None):
    selected = list_books.curselection()
    if selected:
        selected_book_id = int(list_books.get(selected[0]).split(":")[0])
        book = search_books(str(selected_book_id))[0]

        title_var.set(book[1])
        author_var.set(book[2])
        publisher_var.set(book[3])
        category_var.set(book[4])
        quantity_var.set(str(book[5]))
        status_var.set(book[6])

        img_data = get_book_image(selected_book_id)
        if img_data:
            image = Image.open(io.Bytes.IO(img_data))
            image = image.resize((200, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label_image.config(image=photo)
            label_image.image = photo  # keep a reference!

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

tk.Label(frame3, text="搜索").grid(row=0, column=0)
entry_search = tk.Entry(frame3, textvariable=search_var)
entry_search.grid(row=0, column=1)
tk.Button(frame3, text="搜索图书", command=search_and_display_books).grid(row=0, column=2)

list_books = tk.Listbox(frame3, height=10)
list_books.grid(row=1, column=0, columnspan=3, sticky='nsew')
list_books.bind('<<ListboxSelect>>', show_book_details)

scrollbar = ttk.Scrollbar(frame3, command=list_books.yview)
scrollbar.grid(row=1, column=3, sticky='ns')
list_books.config(yscrollcommand=scrollbar.set)

# Display and edit book details
label_image = Label(frame3)
label_image.grid(row=1, column=4, rowspan=6)

tk.Label(frame3, text="标题").grid(row=2, column=0)
tk.Entry(frame3, textvariable=title_var).grid(row=2, column=1, columnspan=2)
tk.Label(frame3, text="作者").grid(row=3, column=0)
tk.Entry(frame3, textvariable=author_var).grid(row=3, column=1, columnspan=2)
tk.Label(frame3, text="出版社").grid(row=4, column=0)
tk.Entry(frame3, textvariable=publisher_var).grid(row=4, column=1, columnspan=2)
tk.Label(frame3, text="分类").grid(row=5, column=0)
tk.Entry(frame3, textvariable=category_var).grid(row=5, column=1, columnspan=2)
tk.Label(frame3, text="数量").grid(row=6, column=0)
tk.Entry(frame3, textvariable=quantity_var).grid(row=6, column=1, columnspan=2)
tk.Label(frame3, text="状态").grid(row=7, column=0)
tk.Entry(frame3, textvariable=status_var).grid(row=7, column=1, columnspan=2)
tk.Button(frame3, text="更新图书", command=update_book_details).grid(row=8, column=0, columnspan=3)

tk.Button(frame3, text="删除选定图书", command=delete_selected_book).grid(row=8, column=4, columnspan=3)

# 标签页4: 版权信息页展示
frame4 = ttk.Frame(notebook)
notebook.add(frame4, text='版权信息')

# 添加版权信息文字
copyright_label = tk.Label(frame4, text="图书管理系统\n版本 1.0\n版权所有 © 2024\n开发者: littlecay")
copyright_label.pack(side="left", padx=10)

# 创建一个新的框架来包含图片和图片上方的文字
image_frame = tk.Frame(frame4)
image_frame.pack(side="right", padx=10)

# 添加“请作者喝杯咖啡”文字
coffee_label = tk.Label(image_frame, text="请作者喝杯咖啡")
coffee_label.pack()

# 添加图片
try:
    image = Image.open("moneyme.jpg")
    image = image.resize((200, 300), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(image_frame, image=photo)
    image_label.image = photo  # keep a reference!
    image_label.pack()
except Exception as e:
    print(f"Error loading image: {e}")

root.mainloop()

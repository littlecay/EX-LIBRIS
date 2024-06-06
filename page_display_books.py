import tkinter as tk
from tkinter import ttk, Label
from PIL import Image, ImageTk
import io
from database_manager import display_books

def create_display_books_page(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text='显示图书')

    scrollbar = ttk.Scrollbar(frame, orient='vertical')
    scrollbar.pack(side='right', fill='y')

    canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
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

    tk.Button(frame, text="刷新图书列表", command=display_all_books).pack(fill='x')
    display_all_books()  # 初始加载图书

    return frame

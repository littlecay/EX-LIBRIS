import tkinter as tk
from tkinter import ttk, Label
from PIL import Image, ImageTk

def create_copyright_info_page(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text='版权信息')

    # 添加版权信息文字
    copyright_label = tk.Label(frame, text="图书管理系统\n版本 1.0\n版权所有 © 2024\n开发者: littlecay\n贡献者:TiferKing")
    copyright_label.pack(side="left", padx=10)

    # 创建一个新的框架来包含图片和图片上方的文字
    image_frame = tk.Frame(frame)
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

    return frame

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

def open_github_url(url):
    webbrowser.open_new(url)

def create_copyright_info_page(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text='版权信息')

    # 创建一个包含版权信息的框架
    info_frame = tk.Frame(frame)
    info_frame.pack(side="left", padx=10)

    # 添加版权信息文字
    tk.Label(info_frame, text="图书管理系统\n版本 1.0\n版权所有 © 2024").pack(anchor="w")

    # 添加开发者信息
    developer_label = tk.Label(info_frame, text="开发者: ", anchor="w")
    developer_label.pack(anchor="w")

    # 添加可点击的开发者链接
    littlecay_label = tk.Label(info_frame, text="littlecay", fg="blue", cursor="hand2", anchor="w")
    littlecay_label.pack(anchor="w")
    littlecay_label.bind("<Button-1>", lambda e: open_github_url("https://github.com/littlecay"))

    # 添加贡献者信息
    contributor_label = tk.Label(info_frame, text="贡献者: ", anchor="w")
    contributor_label.pack(anchor="w")

    # 添加可点击的贡献者链接
    tiferking_label = tk.Label(info_frame, text="TiferKing", fg="blue", cursor="hand2", anchor="w")
    tiferking_label.pack(anchor="w")
    tiferking_label.bind("<Button-1>", lambda e: open_github_url("https://github.com/TiferKing"))

    # 创建一个新的框架来包含图片和图片上方的文字
    image_frame = tk.Frame(frame)
    image_frame.pack(side="right", padx=10)

    # 添加“请作者喝杯咖啡”文字
    coffee_label = tk.Label(image_frame, text="请作者喝杯咖啡")
    coffee_label.pack()

    # 添加图片
    try:
        image = Image.open("moneyme.jpg")
        image = image.resize((200, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(image_frame, image=photo)
        image_label.image = photo  # keep a reference!
        image_label.pack()
    except Exception as e:
        print(f"Error loading image: {e}")

    return frame
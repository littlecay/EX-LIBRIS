# 图书管理系统使用说明书

---

## 目录
1. 系统概述
2. 安装步骤
3. 功能介绍
4. 操作指南
   - 显示所有图书
   - 添加图书
   - 查询图书
   - 更新图书信息
   - 删除图书
5. 注意事项
6. 常见问题

---

## 1. 系统概述

本图书管理系统使用 Python 和 Tkinter 库开发，提供了基本的图书管理功能，包括图书的添加、查询、显示和删除。该系统支持图书封面的显示，并能够管理图书的详细信息，如标题、作者、出版社、分类、数量和状态。

## 2. 安装步骤

### 系统要求
- Python 3.x
- Tkinter 库
- Pillow 库

### 安装步骤
1. **安装 Python**: 请确保已安装 Python 3.x 版本。可以从 [Python 官网](https://www.python.org) 下载并安装。

2. **安装 Tkinter**: Tkinter 通常随 Python 安装包一起安装。如果没有安装，可以使用以下命令安装：
   ```bash
   sudo apt-get install python3-tk
   
3. **安装 Pillow**: Pillow 是一个 Python 图像处理库。可以使用以下命令安装：

    ```bash
    pip install pillow

4. **下载代码**: 将图书管理系统的代码下载到本地目录。

5. **配置数据库**: 确保 database_manager.py 文件中正确配置了数据库连接。

## 3. 功能介绍
本图书管理系统主要包括以下功能：

- 显示所有图书
- 添加图书
- 查询图书
- 更新图书信息
- 删除图书

## 4. 操作指南
### 显示所有图书
启动程序后，系统会默认显示所有已添加的图书。
可以通过点击“刷新图书列表”按钮来更新显示的图书列表。
### 添加图书
切换到“添加图书”标签页。
在相应的输入框中填写图书的标题、作者、出版社、分类、数量和状态。
点击“选择封面”按钮，从本地选择图书的封面图片。
填写完毕后，点击“添加图书”按钮，系统会将新图书添加到数据库中并在“显示图书”标签页更新显示。
### 查询图书
切换到“查询图书”标签页。
在“搜索”输入框中输入需要查询的图书信息（如标题、作者等）。
点击“搜索图书”按钮，系统会显示符合条件的图书列表。
选择某一本图书，可以在右侧查看其详细信息，包括封面图。
### 更新图书信息
在“查询图书”标签页中，选择需要更新的图书。
在右侧的详细信息区域中修改相应的图书信息。
点击“更新图书”按钮，系统会将修改后的信息保存到数据库中。
### 删除图书
在“查询图书”标签页中，选择需要删除的图书。
点击“删除选定图书”按钮，系统会将该图书从数据库中删除，并更新显示的图书列表。

## 5. 注意事项
确保在添加图书时，所有字段均已填写完整，并选择了封面图片。
在查询图书时，可以输入部分信息进行模糊查询。
删除图书操作不可恢复，请谨慎操作。

## 6. 常见问题
**问题1**: 启动程序后无法显示图书列表？
- 解决方案: 请确保数据库已正确配置，并且数据库中已有图书数据。

**问题2**: 添加图书时提示“请填写所有字段并选择封面图片”？

- 解决方案: 请检查所有输入框是否已填写完整，并且已选择了封面图片。

**问题3**: 更新或删除图书后列表未更新？

- 解决方案: 请点击“刷新图书列表”按钮，手动更新图书显示列表。

如果有更多问题或需要进一步的帮助，请联系系统开发人员littlesummercat@gmail.com。

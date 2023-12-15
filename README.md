# Flask 简易留言板

这是一个使用 Flask 框架和 SQLAlchemy 数据库的简易留言板应用。该应用允许用户查看留言、添加新留言以及删除现有留言。

## 如何运行

1. 安装依赖：

   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

2. 运行应用：

   ```bash
   python your_app_file.py
   ```

   替换 `your_app_file.py` 为你的应用文件名。

3. 访问应用：

   打开浏览器并访问 [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 查看应用。

## 数据库配置

应用使用 SQLite 数据库来存储留言信息。数据库文件为 `messages.db`，并保存在应用的根目录下。你可以根据需要更改数据库 URI，修改以下行代码：

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
```

## 模型

应用定义了一个简单的留言模型，包含作者和留言内容：

```python
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
```

## 路由

- `/` - 首页展示所有留言。
- `/add` - 提交表单以添加新留言。
- `/delete/<int:message_id>` - 删除指定ID的留言。

## 如何使用

1. 访问首页 [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 查看所有留言。
2. 点击页面上的 "Add Message" 连接，填写作者和留言内容，然后提交表单。
3. 留言成功添加后，将重定向回首页，显示更新后的留言列表。
4. 若要删除留言，点击相应留言后的 "Delete" 连接。

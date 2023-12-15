from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)


@app.route('/add', methods=['POST'])
def add_message():
    author = request.form['author']
    content = request.form['content']
    new_message = Message(author=author, content=content)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:message_id>')
def delete_message(message_id):
    message = Message.query.get(message_id)
    db.session.delete(message)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

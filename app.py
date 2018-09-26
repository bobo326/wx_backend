from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from config import pgsql_config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = pgsql_config['url']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# app.register_blueprint()
# app.add_url_rule("/login", view_func=login, methods=["POST"])


# 测试用例
@app.route('/', methods=["GET"])
def hello_world():
    return "nice to meet you!"


@app.route('/login', methods=['POST'])
def login():
    x = 0
    username = request.form['username']
    password = request.form['password']
    userz = User.query.filter(User.username == username).first()
    print(userz)
    if userz:
        if userz.password == password:
            x = 1
        else:
            x = 0
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return str(x)


class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键ID
    username = Column(String(length=255))  # 用户名
    password = Column(String(length=255))  # 密码

    def __init__(self, username, password):
        self.username = username
        self.password = password

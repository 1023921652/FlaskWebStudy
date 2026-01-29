from flask import Flask, render_template, request,jsonify
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column
from flask_sqlalchemy import SQLAlchemy
from exts import db, migrate,mail
from flask_mail import Message

from models import *
from flask_migrate import Migrate
import config
import random
import string
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app, db)
mail.init_app(app)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/pub')
def pub():
    return render_template('pub.html')

@app.route('/detail/<int:vegetable_id>')
def detail(vegetable_id):
    return render_template('detail.html')
@app.get('/email/code')
@app.get("/email/code")
def get_email_code():
    # /email/code?email=abc@qq.com
    email = request.args.get("email")
    if not email:
        return jsonify({"result": False, "message": "请传入邮箱！"})

    # 生成验证码
    source = string.digits * 4
    code = "".join(random.sample(source, 4))
    message = Message(
        subject="【知了蔬菜供应商】注册验证码",
        recipients=[email],
        body=f"【知了蔬菜供应商】注册验证码：{code}"
    )
    try:
        mail.send(message)
    except Exception as e:
        return jsonify({"result": False, "message": str(e)})
    # memcached/redis
    code_model = EmailCode(code=code, email=email)
    db.session.add(code_model)
    db.session.commit()
    return jsonify({"result": True, "message": None})
if __name__ == '__main__':
    app.run(debug=True)
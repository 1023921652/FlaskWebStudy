import os

SECRET_KEY = "sdfsdfk2rjl23"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, "media")


MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'vegetable_provider'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4'


# 邮箱配置,使用个人邮箱发送
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "1023921652@qq.com"
# 授权码 在邮箱设置的安全设置下的POP3/IMAP/SMTP/Exchange/CardDAV 服务  里配置
MAIL_PASSWORD = "sbelgrhezlllbeid"
MAIL_DEFAULT_SENDER = "1023921652@qq.com"
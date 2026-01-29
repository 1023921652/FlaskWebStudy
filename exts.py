from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column
from flask_migrate import Migrate
from flask_mail import Mail
# 定义命名约定的Base类
class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        # ix: index，索引。
        "ix": 'ix_%(column_0_label)s',
        # un：unique，唯一约束
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        # ck：Check，检查约束
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        # fk：Foreign Key，外键约束
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        # pk：Primary Key，主键约束
        "pk": "pk_%(table_name)s"
    })
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
mail = Mail()
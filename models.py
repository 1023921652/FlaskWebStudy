from exts import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Float, DateTime, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from typing import List


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    username: Mapped[str] = mapped_column(String(50))
    _password: Mapped[str] = mapped_column(String(200))
    vegetables: Mapped["Vegetable"] = relationship("Vegetable", back_populates="publisher")

    def __init__(self, *args, **kwargs):
        password = kwargs.get("password")
        if password:
            kwargs.pop("password")
        super().__init__(*args, **kwargs)
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        # hash的密码和原始密码进行比较,原始密码正确,返回true
        return check_password_hash(self.password, raw_password)



class VegetableCategory(db.Model):
    __tablename__ = 'vegetable_category'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))

    vegetables: Mapped[List["Vegetable"]] = relationship("Vegetable", back_populates="category")


class Vegetable(db.Model):
    __tablename__ = 'vegetable'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float)
    picture: Mapped[str] = mapped_column(String(200))
    mobile: Mapped[str] = mapped_column(String(20))
    place: Mapped[str] = mapped_column(String(100))
    provider: Mapped[str] = mapped_column(String(100))
    pub_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("vegetable_category.id"))
    category: Mapped[VegetableCategory] = relationship("VegetableCategory", back_populates="vegetables")

    publisher_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    publisher: Mapped[User] = relationship("User", back_populates="vegetables")


class EmailCode(db.Model):
    __tablename__ = 'email_code'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(10))
    email: Mapped[str] = mapped_column(String(100))
    create_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
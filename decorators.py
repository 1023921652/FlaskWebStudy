from flask import g, redirect
from functools import wraps


def login_required(func):
    # @wraps 的作用是伪装。它让 inner 看起来、用起来、查起来都像原来的 func。
    # 例如会将原始函数的元数据复制给 inner 函数
    # @app.route('/pub'),是和函数名进行关联的,所以通过使用@wraps把inner的inner__name__修改成原函数的函数名
    # def pub():
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect("/login")
    return inner
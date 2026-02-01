from models import VegetableCategory
from exts import db


def init_vegetable_category():
    categories = ["豌豆", "苦瓜", "蒲瓜", "茄子", "西兰花", "卷心菜", "灯笼椒", "胡萝卜", "花菜", "黄瓜", "木瓜", "土豆", "南瓜", "萝卜", "西红柿"]
    category_models = [VegetableCategory(name=category) for category in categories]
    db.session.add_all(category_models)
    db.session.commit()
    print("蔬菜分类初始化成功！")
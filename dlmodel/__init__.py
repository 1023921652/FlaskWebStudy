# pip install torch torchvision

from torch import nn
import torch
from PIL import Image
from torchvision import transforms
import os

# 原始列表
vegetable_list = ['Bean', 'Bitter_Gourd', 'Bottle_Gourd', 'Brinjal', 'Broccoli', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']

# 中文对应列表
chinese_names = ['豌豆', '苦瓜', '蒲瓜', '茄子', '西兰花', '卷心菜', '灯笼椒', '胡萝卜', '花菜', '黄瓜', '木瓜', '土豆', '南瓜', '萝卜', '西红柿']

n_classes = len(chinese_names)


class VegetableCNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Conv2d(3, 100, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(100, 150, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(150, 200, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(200, 200, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Conv2d(200, 250, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(250, 250, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),

            nn.Flatten(),
            nn.Linear(6250, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(0.25),
            nn.Linear(32, n_classes),
        )
    def forward(self, x):
        return self.network(x)


model = VegetableCNNModel()
model_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "model.pth"
    )
)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

def predict(picture_path):
    image = Image.open(picture_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize(40),  # resize shortest side
        transforms.CenterCrop(40),  # crop longest side
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225]
        )
    ])
    image_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(image_tensor)
    category_index = output.argmax().item()
    category_name = chinese_names[category_index]
    return category_name
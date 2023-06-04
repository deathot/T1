import json
import requests
import os
from pycocotools.coco import COCO
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

image_path = "./val2017"
json_path = "C:/Text737/cocoshujuji/annotations/instances_val2017.json"

# 加载JSON标注文件
with open(json_path, "r") as f:
    json_labels = json.load(f)

print(json_labels["info"])

# 新建COCO数据集描述
dataset_info = {'description': 'COCO 2017 Dataset',
                'url': 'http://cocodataset.org', 'version': '1.0', 'year': 2017,
                'contributor': 'COCO Consortium', 'date_created': '2017/09/01'}

# 下载图像并在本地保存
urls = ['http://images.cocodatest.org/val2017/000000117425.jpg',
        'http://images.cocodatest.org/val2017/000000343218.jpg',
        'http://images.cocodatest.org/val2017/000000439715.jpg',
        'http://images.cocodatest.org/val2017/000000102356.jpg',
        'http://images.cocodatest.org/val2017/00000010363.jpg']
image_ids = ['139', '724', '785', '885', '1000']

for url, image_id in zip(urls, image_ids):
    filename = image_id + '.jpg'
    response = requests.get(url)
    with open(os.path.join(image_path, filename), 'wb') as f:
        f.write(response.content)

# 加载COCO对象
coco = COCO(annotation_file=json_path)

ids = list(sorted(coco.imgs.keys()))
print("number of images:{}".format(len(ids)))

# 构建类别ID与类别名称的字典
coco_classes = {v["id"]: v["name"] for k, v in coco.cats.items()}

# 可视化1000张图像中的物体实例
for img_id in ids[:1000]:
    ann_ids = coco.getAnnIds(imgIds=img_id)
    targets = coco.loadAnns(ann_ids)
    path = coco.loadImgs(img_id)[0]['file_name']

    img = Image.open(os.path.join(image_path, path)).convert('RGB')
    draw = ImageDraw.Draw(img)
    for target in targets:
        x, y, w, h = target["bbox"]
        # 由于bbox格式为[x_min, y_min, bbox_width, bbox_height]，需要转换为(x_min, y_min, x_max, y_max)
        x1, y1, x2, y2 = x, y, int(x + w), int(y + h)
        draw.rectangle((x1, y1, x2, y2))
        draw.text((x1, y1), coco_classes[target["category_id"]])

    plt.imshow(img)
    plt.show()

# 构建一个只包含指定图像ID的新的COCO数据集
new_data = {'images': [], 'annotations': []}
img_ids = [139, 724, 785, 885, 1000]

for img in json_labels['images']:
    if img['id'] in img_ids:
        new_data['images'].append(img)

for ann in json_labels['annotations']:
    if ann['image_id'] in img_ids:
        new_data['annotations'].append(ann)

with open('new_data.json', 'w') as f:
    json.dump(new_data, f)






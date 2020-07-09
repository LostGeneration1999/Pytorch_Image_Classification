import io

import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
size = 224

def transform_image(image_bytes, size, mean, std):
    my_transforms = transforms.Compose(
        [#transforms.RandomResizedCrop(resize, scale=(0.5, 1.0)),
        transforms.CenterCrop(size),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)]                       
        )
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

with open('./fukuoka.jpg', 'rb') as f:
    image_bytes = f.read()
    tensor = transform_image(image_bytes, size, mean, std)
    print(tensor)


    

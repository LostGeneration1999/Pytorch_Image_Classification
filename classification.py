import io
import json
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
size = 224

model = models.densenet121(pretrained=True)
model.eval()
class_index = json.load(open('./imagenet_class_index.json'))

def transform_image(image_bytes, size, mean, std):
    my_transforms = transforms.Compose(
        [#transforms.RandomResizedCrop(resize, scale=(0.5, 1.0)),
        transforms.CenterCrop(size),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)]                       
        )
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes, size, mean, std):
    tensor = transform_image(image_bytes, size, mean, std)
    outputs = model.forward(tensor)
    _, pred = outputs.max(1)
    prediction_class = str(pred.item())
    return class_index[prediction_class]
    
with open('./dog.jpg', 'rb') as f:
    image_bytes = f.read()
    print(get_prediction(image_bytes, size, mean, std))


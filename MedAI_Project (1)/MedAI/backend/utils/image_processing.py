from PIL import Image
import torchvision.transforms as transforms
import pydicom
import numpy as np
import torch

def process_xray_image(file):
    image = Image.open(file).convert('L')  # Gri ton (1 kanal)
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    return transform(image)  # [1, H, W]

def process_dicom_image(file):
    dicom = pydicom.dcmread(file)
    img_array = dicom.pixel_array.astype(np.float32)
    img_array = (img_array - np.min(img_array)) / (np.max(img_array) - np.min(img_array))  # normalize
    img_resized = np.resize(img_array, (256, 256))  # uygun şekilde yeniden boyutlandır
    tensor = torch.tensor(img_resized).unsqueeze(0)  # kanal ekle: [1, H, W]
    return tensor

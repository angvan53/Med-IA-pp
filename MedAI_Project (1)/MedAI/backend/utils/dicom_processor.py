import pydicom
import numpy as np
import torch
import torchvision.transforms as transforms
from PIL import Image
import io

def process_dicom_image(file):
    dicom_data = pydicom.dcmread(file)
    image = dicom_data.pixel_array.astype(np.float32)

    # Normalize
    image = (image - np.min(image)) / (np.max(image) - np.min(image))

    # Resize & convert to tensor
    image_pil = Image.fromarray((image * 255).astype(np.uint8)).convert('L')
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    image_tensor = transform(image_pil)
    return image_tensor


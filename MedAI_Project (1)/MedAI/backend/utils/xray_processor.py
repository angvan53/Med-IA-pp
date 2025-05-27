from PIL import Image
import torchvision.transforms as transforms

def process_xray_image(file):
    image = Image.open(file).convert('L')  # grayscale
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    image_tensor = transform(image)
    return image_tensor

import torch
import torch.nn as nn
import numpy as np

class SimpleUNet(nn.Module):
    def __init__(self, in_channels=1, out_channels=5):
        super(SimpleUNet, self).__init__()
        self.encoder1 = nn.Sequential(
            nn.Conv2d(in_channels, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding=1),
            nn.ReLU()
        )
        self.pool = nn.MaxPool2d(2, 2)
        self.decoder1 = nn.Sequential(
            nn.ConvTranspose2d(64, out_channels, 2, stride=2),
            nn.Sigmoid()
        )

    def forward(self, x):
        x1 = self.encoder1(x)
        x2 = self.pool(x1)
        x3 = self.decoder1(x2)
        return x3

def interpret_xray_output(prediction):
    threshold = 0.5
    labels = ['Pnömoni', 'Kalp büyümesi', 'Fibrozis', 'Normal', 'Nodül']
    results = []
    for i, value in enumerate(prediction):
        if value > threshold:
            results.append(f"{labels[i]} ihtimali yüksek ({round(value*100, 1)}%)")
    if not results:
        results = ["Belirgin anormallik tespit edilmedi."]
    return results

def interpret_mri_output(prediction):
    tumor_threshold = 0.5
    if isinstance(prediction, (list, np.ndarray)):
        tumor_area = np.sum(prediction) if isinstance(prediction, np.ndarray) else sum(prediction)
    else:
        tumor_area = prediction

    if tumor_area > tumor_threshold:
        return ["Beyin tümörü tespiti yüksek ihtimalle mevcut."]
    else:
        return ["Tümör tespiti yok veya düşük ihtimal."]

def predict_image(model, image_tensor, image_type="xray"):
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    with torch.no_grad():
        image_tensor = image_tensor.unsqueeze(0).to(device)
        output = model(image_tensor)
        output_cpu = output.squeeze().cpu()

        if image_type == "xray":
            class_scores = output_cpu.mean(dim=[1, 2]).numpy().tolist()
            prediction = class_scores[:5]
            interpretation = interpret_xray_output(prediction)

        elif image_type == "dicom":
            prediction = output_cpu.numpy()
            interpretation = interpret_mri_output(prediction)

        else:
            prediction = []
            interpretation = ["Bilinmeyen görüntü tipi."]

    return {
        "prediction": prediction,
        "interpretation": interpretation
    }

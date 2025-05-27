from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from model import SimpleUNet, predict_image
from utils.image_processing import process_xray_image, process_dicom_image  # kendi fonksiyonların

app = Flask(__name__)
CORS(app)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleUNet(in_channels=1, out_channels=5)
model.load_state_dict(torch.load('model_weights.pth', map_location=device))  # model ağırlık dosyan var ise
model.to(device)
model.eval()

# Basit çeviri sözlüğü örneği (dilersen genişletebilirsin)
translations = {
    "tr": {
        "ihtimali yüksek": "ihtimali yüksek",
        "Belirgin anormallik tespit edilmedi.": "Belirgin anormallik tespit edilmedi.",
        "Beyin tümörü tespiti yüksek ihtimalle mevcut.": "Beyin tümörü tespiti yüksek ihtimalle mevcut.",
        "Tümör tespiti yok veya düşük ihtimal.": "Tümör tespiti yok veya düşük ihtimal.",
        "Bilinmeyen görüntü tipi.": "Bilinmeyen görüntü tipi."
    },
    "en": {
        "ihtimali yüksek": "high probability",
        "Belirgin anormallik tespit edilmedi.": "No significant abnormality detected.",
        "Beyin tümörü tespiti yüksek ihtimalle mevcut.": "High probability of brain tumor detected.",
        "Tümör tespiti yok veya düşük ihtimal.": "No tumor detected or low probability.",
        "Bilinmeyen görüntü tipi.": "Unknown image type."
    },
    "de": {
        "ihtimali yüksek": "hohe Wahrscheinlichkeit",
        "Belirgin anormallik tespit edilmedi.": "Keine signifikante Anomalie festgestellt.",
        "Beyin tümörü tespiti yüksek ihtimalle mevcut.": "Hohe Wahrscheinlichkeit eines Hirntumors festgestellt.",
        "Tümör tespiti yok veya düşük ihtimal.": "Kein Tumor festgestellt oder geringe Wahrscheinlichkeit.",
        "Bilinmeyen görüntü tipi.": "Unbekannter Bildtyp."
    }
}

def translate_text(text, lang):
    for tr_key in translations["tr"]:
        if tr_key in text:
            text = text.replace(tr_key, translations[lang].get(tr_key, tr_key))
    return text

@app.route("/analyze", methods=["POST"])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "Dosya bulunamadı"}), 400

    file = request.files['image']
    image_type = request.form.get("type", "xray")
    lang = request.form.get("lang", "tr")
    if lang not in translations:
        lang = "tr"

    # Görüntü işleme
    if image_type == "dicom":
        image_tensor = process_dicom_image(file)
    else:
        image_tensor = process_xray_image(file)

    # Tahmin yap
    result = predict_image(model, image_tensor, image_type=image_type)

    # Çeviri uygula
    translated_interpretation = [translate_text(t, lang) for t in result["interpretation"]]
    result["interpretation"] = translated_interpretation

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

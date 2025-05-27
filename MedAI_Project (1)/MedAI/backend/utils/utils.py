# utils.py

translations = {
    "en": {
        "Pnömoni": "Pneumonia",
        "Kalp büyümesi": "Cardiomegaly",
        "Fibrozis": "Fibrosis",
        "Normal": "Normal",
        "Nodül": "Nodule",
        "Belirgin anormallik tespit edilmedi.": "No significant abnormality detected.",
        "Beyin tümörü tespiti yüksek ihtimalle mevcut.": "High probability of brain tumor detected.",
        "Tümör tespiti yok veya düşük ihtimal.": "No tumor detected or low probability.",
        "Bilinmeyen görüntü tipi.": "Unknown image type."
    },
    "de": {
        "Pnömoni": "Pneumonie",
        "Kalp büyümesi": "Kardiomegalie",
        "Fibrozis": "Fibrose",
        "Normal": "Normal",
        "Nodül": "Knoten",
        "Belirgin anormallik tespit edilmedi.": "Keine signifikanten Abnormalitäten festgestellt.",
        "Beyin tümörü tespiti yüksek ihtimalle mevcut.": "Hohe Wahrscheinlichkeit eines Hirntumors festgestellt.",
        "Tümör tespiti yok veya düşük ihtimal.": "Kein Tumor festgestellt oder geringe Wahrscheinlichkeit.",
        "Bilinmeyen görüntü tipi.": "Unbekannter Bildtyp."
    }
}

def translate_labels(text_list, lang):
    if lang not in translations:
        return text_list
    return [translations[lang].get(t, t) for t in text_list]

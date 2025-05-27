# MedAI - Tıbbi Görüntü İşleme Uygulaması

Bu proje, MRI (DICOM) ve X-Ray görüntülerini yükleyip analiz edebilen, doktorlara öneri amaçlı destek sağlayan çok dilli bir tıbbi görüntü analiz platformudur.

## 🔍 Özellikler

- MRI ve X-ray görüntü desteği (DICOM, JPEG/PNG)
- Yapay zeka destekli segmentasyon ve sınıflandırma
- TR / EN / DE dil desteği
- Modern web arayüzü
- Doktorlara tavsiye amaçlı kullanım
- Uygulama sahibi: **Dr. Mustafa Okutan**
- Muson Mühendislik destekli

## 🧠 Model

- PyTorch tabanlı U-Net segmentasyon modeli
- Kanserli dokuların otomatik belirlenmesi

## 🖥️ Kurulum

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 2. Frontend (Statik dosyalar)

`frontend/index.html` tarayıcıda açılarak kullanılabilir.

### 3. Docker (isteğe bağlı)

```bash
docker build -t medai-app .
docker run -p 8501:8501 medai-app
```

## 🚀 Canlıya Alma

### AWS EC2:

- EC2 instance oluştur
- Dosyaları yükle ve çalıştır
- `http://<ip-adresi>:8501` ile eriş

### AWS S3:

- `frontend/` klasörünü S3'e yükle
- Statik barındırmayı aktif et

## 📄 Lisans

Bu proje ticari amaçla kullanılmaz. Yalnızca doktorlara tavsiye amaçlıdır.

---

# 🧠 MedAI – Tıbbi Görüntü Analiz Uygulaması

Bu uygulama, X-Ray ve MRI (DICOM) görüntülerini yükleyerek tahmini bir analiz sonucu sunar. Yalnızca doktorlara tavsiye amacıyla geliştirilmiştir.

## 📌 Amaç

- DICOM veya X-Ray görüntülerini yükle
- AI modeli ile analiz et
- Sonucu görselleştir
- Çok dilli (TR / EN / DE) arayüz desteği

## 🩺 Hedef Kullanıcılar

- Radyoloji Uzmanları
- Göğüs Hastalıkları Hekimleri
- Ortopedi Uzmanları

## 📦 Proje Yapısı

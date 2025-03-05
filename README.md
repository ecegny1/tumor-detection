# Tümör Tespit Sistemi

Bu uygulama, MR görüntüleri üzerinden tümör tespiti ve analiz yapmaktadır. Streamlit kullanılarak geliştirilmiş bir web uygulamasıdır.

---
title: Tumor Dedection
emoji: 🧠
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.40.2
app_file: app.py
pinned: false
license: MIT
---

## Özellikler

- MR görüntülerinde tümör tespiti
- Örnek analizler
- Hasta bilgilerinin kaydedilmesi
- Kullanıcı dostu arayüz

## Kullanım

Uygulama, sol taraftaki menü çubuğu ile farklı bölümlere erişim sağlar:

1. **Anasayfa**: Uygulamanın genel tanıtımı
2. **Hakkımızda**: Uygulama ve ekip hakkında bilgiler
3. **Tümör Tespiti**: MR görüntüsü yükleyerek tümör analizi yapma
4. **Örnek Analizlerimiz**: Örnek MR görüntüleri ve analizleri
5. **Hasta Yorumları**: Kullanıcı yorumları ve geri bildirimleri
6. **Bize Ulaşın**: İletişim bilgileri ve iletişim formu

## Teknik Detaylar

Uygulama aşağıdaki teknolojileri kullanmaktadır:

- Python 3.9+
- Streamlit
- Pillow (PIL)
- NumPy
- Pandas
- Matplotlib
- OpenCV
- TensorFlow

## Kurulum

Uygulamayı yerel olarak çalıştırmak için:

```bash
pip install -r requirements.txt
streamlit run tumor_detection_app.py
```

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

# Beyin Tümörü Tespit Projesi

Bu proje, manyetik rezonans görüntüleri (MRI) üzerinde beyin tümörlerini tespit etmek için derin öğrenme tekniklerini kullanmaktadır. Kullanılan teknoloji Python'dur ve projede **TensorFlow** veya **PyTorch** gibi derin öğrenme kütüphaneleri ile eğitilen bir model bulunmaktadır. Ayrıca, **Streamlit** ile kullanıcı dostu bir arayüz geliştirilmiştir.

## Proje Özeti

Bu projenin amacı, beyin MR görüntülerini analiz ederek tümör olup olmadığını tespit etmektir. Eğer bir tümör bulunursa, model tümörü işaretler ve 'var' şeklinde bilgi verir. Eğer tümör bulunmazsa, model 'tümör yoktur' şeklinde çıktı üretir. Proje, tıbbi görüntülerin erken teşhisi amacıyla kullanılabilecek bir yapay zeka uygulaması geliştirmeyi hedeflemektedir.

## Kullanılan Teknolojiler

- **Python**: Proje dili.
- **TensorFlow / PyTorch**: Derin öğrenme kütüphaneleri.
- **Streamlit**: Kullanıcı arayüzü için web uygulaması.
- **OpenCV**: Görüntü işleme ve analiz için kullanıldı.

## Proje Adımları

1. **Veri Kümesi**: 
   - Proje, **dwb2023/brain-tumor-image-dataset-semantic-segmentation** veri kümesi üzerinde çalışmaktadır.
   - Veri kümesi, beyin MR görüntülerini içermektedir ve her bir resimdeki tümörler etiketlenmiştir.
   - Proje dosyalarına ve veri kümesine [Google Drive linki](https://drive.google.com/drive/folders/1K6Ymo0ty1o_VUjVV6lZ_-v7h4zk6PH2D) üzerinden erişebilirsiniz.

2. **Veri Ön İşleme**: 
   - Görüntüler yüklendikten sonra, modelin doğru şekilde eğitilebilmesi için boyutlandırma, normalizasyon ve veri artırma (data augmentation) işlemleri yapılır.

3. **Model Eğitimi**:
   - Model, TensorFlow veya PyTorch kullanılarak eğitilir. Eğitim verisi ile model, beyin tümörlerini doğru şekilde sınıflandırmak için optimize edilir.

4. **Model Değerlendirmesi**:
   - Eğitim tamamlandıktan sonra, model doğruluk, hassasiyet, ve hatalı pozitif/negatif oranları gibi metrikler ile değerlendirilir.

5. **Uygulama**:
   - Streamlit ile kullanıcı arayüzü geliştirilir. Kullanıcılar, MR görüntülerini yükleyerek tümör olup olmadığını anında öğrenebilirler.

## Kullanım Talimatları

1. Gerekli kütüphaneleri yüklemek için terminalde aşağıdaki komutu çalıştırın:
   ```bash
   pip install -r requirements.txt
   ```

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

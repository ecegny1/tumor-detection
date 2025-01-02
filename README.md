# TUMOR DETECTION ANALYSIS SYSTEM

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
![image](https://github.com/user-attachments/assets/e9cef57b-25dd-4846-9c8d-dd09a5800762)

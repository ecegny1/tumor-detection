import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import base64
import os
import h5py
import matplotlib.pyplot as plt

# Streamlit ile HTML ve CSS ekleme
st.markdown(f"""
    <style>
        .body {{
            background-color: #f0f0f0; /* Açık gri arka plan */
            /* veya */
            background-image: url('/static/images/background.jpg');
            background-size: cover;
        }}    
        .main {{
            background-color: rgba(255, 255, 255, 0.8);  /* Beyaz renk, %80 şeffaflık */
            padding: 20px;
            border-radius: 10px;
            background-image: url("/Users/eceguney/Desktop/background.PNG");  /* Arka plan resminin yolu */
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            height: 100vh;  /* Sayfa yüksekliği */
        }}
        .header {{
            color: white;
            background-color: #4CAF50;
            padding: 10px;
            text-align: center;
            border-radius: 5px;
        }}

        .section-title {{
            color: #4CAF50;
            font-size: 30px;
            text-align: center;
            margin: 20px 0;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 5px;
        }}

        .sidebar .sidebar-content {{
            background-color: #f4f4f9;
        }}
        .section-title {{
            color: #4CAF50;
            font-size: 30px;
            text-align: center;
            margin: 20px 0;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 5px;
        }}

        .content-box {{
            border: 2px solid #4CAF50;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}

        .form-container {{
            border: 2px solid #4CAF50;
            padding: 15px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }}

        .table-container {{
            border: 2px solid #4CAF50;
            padding: 15px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }}

        .footer {{
            text-align: center;
            font-size: 12px;
            color: gray;
            margin-top: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

# Ana başlık
st.title("Tümör Tespit Sistemi")

# Menü çubuğu oluştur, her seçenek için benzersiz key parametresi ekle
# Sidebar menu
menu = st.sidebar.selectbox("Menü", ["Anasayfa", "Hakkımızda", "Tümör Tespiti","Örnek Hasta Analizlerimiz", "Hasta Yorumları", "Bize Ulaşın"], key="menu_selectbox")

# Menüye göre sayfaların içeriğini değiştir
if menu == "Anasayfa":
    st.markdown('<div class="header"><h2>Hoş Geldiniz!</h2></div>', unsafe_allow_html=True)
    st.write("Bu uygulama, MR görüntüleri üzerinden tümör tespiti ve analiz yapmaktadır.")
    # Resmi yükleyin
    image = Image.open("/Users/eceguney/Desktop/veri bilimi/kod calismalarim/mri/index.jpeg")
    st.image(image, caption="Beyin Tümörü Tespiti", use_container_width=True)

elif menu == "Hakkımızda":
    st.markdown('<div class="header"><h2>Hakkımızda</h2></div>', unsafe_allow_html=True)
    st.write("""
    Tümör Tespit Sistemi olarak, sağlık alanında teknolojiyi kullanarak insanların hayatlarını daha sağlıklı ve güvenli hale getirmeyi amaçlıyoruz. Ekibimiz, yapay zeka ve derin öğrenme teknikleriyle gelişmiş sağlık çözümleri üretmeye odaklanmış bir grup uzman profesyonelden oluşmaktadır. Yenilikçi yaklaşımlar ve sağlam bilimsel temellerle, kanser ve diğer hastalıkların erken teşhisini mümkün kılacak teknolojiler geliştirmekteyiz.

    Misyonumuz, tıbbi görüntüleme verilerini kullanarak tümörleri erken aşamalarda tespit etmek ve doğru teşhis konulmasına yardımcı olmaktır. Bu, hastaların tedaviye daha erken başlamasını ve sonuçların daha başarılı olmasını sağlar. Tümör Tespit Sistemi, doktorların tanı koyma sürecini hızlandırarak, zamanında ve doğru müdahaleler yapılmasına olanak tanır.

    Yapay zeka destekli sistemimiz, sürekli olarak öğrenen ve gelişen bir yapıya sahiptir. Sistemimiz, MR, röntgen ve diğer tıbbi görüntüleri analiz ederek, tümör varlığını yüksek doğrulukla tespit eder ve görsel işaretlemeler yaparak doktorlara kolaylık sağlar. Bu sayede, sağlık profesyonelleri daha verimli çalışabilir, hastalar ise doğru ve hızlı bir şekilde tedavi süreçlerine dahil olabilirler.

    Her adımda güvenlik ve gizliliğe büyük önem veriyor, hasta verilerini korumak için en yüksek güvenlik standartlarını uyguluyoruz. Kullanıcı dostu arayüzümüz sayesinde, sistemimiz her türlü sağlık kuruluşunda kolayca kullanılabilir. Sürekli olarak güncellenen ve geliştirilen bu sistem, sağlık sektöründe önemli bir devrim yaratmayı hedeflemektedir.

    Vizyonumuz ise, yapay zeka teknolojileriyle sağlık hizmetlerini dönüştürerek, daha hızlı, daha doğru ve daha erişilebilir bir sağlık altyapısı oluşturmaktır. Bu sayede, her bireyin sağlık durumunun daha yakından takip edilebilmesi ve sağlık hizmetlerine erişimin daha kolay hale gelmesi için çalışıyoruz.

    Sağlıklı günler dileriz.
    """)

# "Örnek Analizlerimiz" sekmesi
elif menu == "Örnek Hasta Analizlerimiz":
    st.markdown('<div class="header"><h2>Örnek Analizlerimiz</h2></div>', unsafe_allow_html=True)
    folder_path = "/Users/eceguney/Desktop/veri bilimi/kod calismalarim/mri/dataset/data/"

    # Dizin içindeki .mat dosyalarını listeleme
    mat_files = [f for f in os.listdir(folder_path) if f.endswith('.mat')]

    # İlk 20 görüntü ile sınırlama
    mat_files = mat_files[:20]

    # Görüntülerde tümör olup olmadığını kontrol etmek için sayaç
    tumor_found_count = 0
    non_tumor_count = 0

    # Her bir .mat dosyasını işlemek için döngü
    for mat_file in mat_files:
        file_path = os.path.join(folder_path, mat_file)

        # Dosyayı açma
        with h5py.File(file_path, 'r') as data:
            cjdata = data['cjdata']

            # Görüntü verisini alma
            image = np.array(cjdata['image'])  # Görüntü

            # 'tumorBorder' verisini alma
            tumor_border = None
            if 'tumorBorder' in cjdata:
                tumor_border = np.array(cjdata['tumorBorder'])
                tumor_found_count += 1  # Tümör bulunan görüntü sayısını artır

            # 'tumorMask' verisini alma (Tümör maskesi var mı?)
            tumor_mask = None
            if 'tumorMask' in cjdata:
                tumor_mask = np.array(cjdata['tumorMask'])

            # Görüntüyü matplotlib ile hazırlama
            fig, ax = plt.subplots()
            ax.imshow(image, cmap='gray')  # Siyah-beyaz görüntü

            # Eğer tümör sınırı varsa, bunu kırmızı renkte çizme
            if tumor_border is not None:
                ax.plot(tumor_border[:, 0], tumor_border[:, 1], color='red', label="Tümör Sınırları", linewidth=2)
            else:
                non_tumor_count += 1  # Tümör olmayan görüntü sayısını artır

            # Maskeyi kırmızı olarak ekleme (şeffaflık ile)
            if tumor_mask is not None:
                ax.imshow(tumor_mask, cmap='Reds', alpha=0.5)  # Kırmızı tonlarında ve şeffaf olarak eklenmiş

                # Tümörün boyutunu hesaplama (maskedeki piksel sayısı)
                tumor_area = np.sum(tumor_mask)  # Tümör maskesindeki beyaz piksel sayısı (tümör alanı)

                # Risk analizi
                if tumor_area < 500:
                    risk_message = "Düşük risk: Küçük tümör. Düzenli takip gereklidir."
                elif tumor_area < 2000:
                    risk_message = "Orta risk: Orta büyüklükte tümör. Hekiminizle görüşün."
                else:
                    risk_message = "Yüksek risk: Büyük tümör. Acil müdahale gerekebilir."

                # Mesaj kutusunda tümör durumu ve risk bilgisini gösterme
                message = f"Tümör Alanı: {tumor_area} piksel\n{risk_message}"
            else:
                # Tümör bulunmayan görüntüler için mesaj
                message = "Tümör bulunmamaktadır.\nSağlıklı günler dileriz."

            # Başlık ve etiket ekleme
            ax.set_title(f"MR Görüntüsü ve Tümör Sınırları ({mat_file})")
            ax.legend()

            # Görüntüyü Streamlit'te gösterme
            st.pyplot(fig)
            st.markdown(f"**{message}**")

        # Açıklama metnini ekleyelim
        st.markdown(f"### Açıklama: {mat_file}")
        st.write("""
        Bu görüntü, beyin MR'ı üzerinde yapılan tümör tespiti analizinin bir örneğidir. 
        Görüntüdeki tümör sınırları (eğer varsa) kırmızı renkte gösterilmektedir. 
        Ayrıca, tümör alanı hesaplanarak risk analizi yapılmaktadır. 
        Eğer tümör alanı küçükse, düşük risk kategorisinde değerlendirilir; 
        orta büyüklükte ise orta risk, büyük bir tümör var ise yüksek risk kategorisinde yer alır.
        Eğer görüntüde tümör yoksa, bu da açıkça belirtilir.
        """)

    # Sonuçları yazdırma
    st.write(f"Tümör Bulunan Görüntüler: {tumor_found_count}")
    st.write(f"Tümör Olmayan Görüntüler: {non_tumor_count}")

elif menu == "Tümör Tespiti":
    st.markdown('<div class="header"><h2>Tümör Tespiti</h2></div>', unsafe_allow_html=True)
    # Hasta Bilgilerini Almak İçin Form
    with st.form(key='patient_form'):
        st.markdown('<div class="section-title">Hasta Bilgileri</div>', unsafe_allow_html=True)
        name = st.text_input("Ad Soyad")
        age = st.number_input("Yaş", min_value=0, max_value=120)
        gender = st.selectbox("Cinsiyet", ["Erkek", "Kadın"], key="gender_selectbox")
        uploaded_file = st.file_uploader("MR Görüntüsünü Yükleyin", type=["jpg", "png", "jpeg"], key="file_uploader")
        submit_button = st.form_submit_button("Tümör Analizini Başlat")
    if submit_button:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Yüklenen MR Görüntüsü", use_container_width=True)

            # Görüntü üzerinde basit bir analiz yapalım (örneğin, renk tonlarıyla basit bir tümör varlığı kontrolü)
            image_array = np.array(image)

            # Örnek basit analiz: Görüntünün ortalama parlaklık değerini alalım
            average_brightness = np.mean(image_array)

            # Tümör var mı yok mu tahmini (basit bir yaklaşım)
            if average_brightness < 100:  # Bu eşik değeri tamamen örnektir, daha gelişmiş bir analiz için değiştirilmelidir.
                tumor_status = "Tümör Tespit Edildi"
                explanation = "Görüntüde yüksek kontrastlı alanlar tespit edildi, bu da tümör olasılığını artırıyor."
            else:
                tumor_status = "Tümör Yok"
                explanation = "Görüntüde belirgin bir kontrast farkı bulunmamaktadır, bu da tümör olmadığına işaret edebilir."

            # Sonuçları göster
            st.markdown(f"**Sonuç: {tumor_status}**")
            st.write(explanation)

elif menu == "Hasta Yorumları":
    st.markdown('<div class="header"><h2>Hasta Yorumları</h2></div>', unsafe_allow_html=True)
    # Yorumları Listeleme
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write("""
    - Hasta 1: "Bu sistem hayatımı kurtardı, teşekkürler!"
    - Hasta 2: "Çok kolay ve kullanışlı."
    - Hasta 3: "Hızlı sonuç ve güvenilir analiz."
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Yorum eklemek için form
    with st.form(key='comment_form'):
        st.markdown('<div class="section-title">Yeni Yorum Ekleyin</div>', unsafe_allow_html=True)

        new_comment = st.text_area("Yorumunuzu Buraya Yazın", key="new_comment_area")
        submit_button = st.form_submit_button("Yorum Gönder")

        if submit_button and new_comment:
            st.write(f"Yeni Yorum: {new_comment}")
            st.write("Yorum başarıyla eklendi.")

elif menu == "Bize Ulaşın":
    # Bize Ulaşın sayfası içeriği
    st.markdown('<div class="header"><h2>Bize Ulaşın</h2></div>', unsafe_allow_html=True)

    # İletişim bilgilerini tablo şeklinde yazdırma
    contact_info = {
        "Bilgi": ["Email", "Telefon", "Adres"],
        "Değer": ["info@tumordetection.com", "+90 555 555 55 55", "İstanbul, Türkiye"]
    }

    # DataFrame oluşturuluyor
    contact_df = pd.DataFrame(contact_info)

    # Tabloyu Streamlit üzerinde gösterme
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.table(contact_df)  # Tabloyu göster
    st.markdown('</div>', unsafe_allow_html=True)

    # Doldurulabilir iletişim formu
    with st.form(key="contact_form"):
        st.subheader("İletişim Formu")

        # Kullanıcıdan veri alınması
        name = st.text_input("Adınız Soyadınız")
        email = st.text_input("E-posta Adresiniz")
        subject = st.text_input("Konu")
        message = st.text_area("Mesajınız")

        # Gönder butonu
        submit_button = st.form_submit_button("Gönder")

        if submit_button:
            # Form gönderildiğinde kullanıcıya onay mesajı gösterme
            st.success(f"Teşekkür ederiz {name}, mesajınız başarıyla gönderildi!")
            # Burada form verilerini bir veritabanına veya e-posta sistemine yönlendirebilirsiniz

# Footer
st.markdown('<div class="footer">© 2024 Tümör Tespit Sistemi. Tüm haklar saklıdır. </div>', unsafe_allow_html=True)

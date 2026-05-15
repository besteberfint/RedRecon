# 🔍 RedRecon

**RedRecon**, hedef bir alan adının (domain) saldırı yüzeyini haritalandırmak için geliştirilmiş, **Passive OSINT** tabanlı bir subdomain keşif aracıdır.

Bu araç, hedef sisteme doğrudan herhangi bir paket göndermeden yalnızca **Certificate Transparency (Sertifika Şeffaflığı)** kayıtlarını analiz ederek gizli kalmış alt alan adlarını tespit eder.

---

## ✨ Öne Çıkan Özellikler

- 🕵️ **Tamamen Pasif**  
  Hedef sunucuda iz bırakmaz ve log kayıtlarına takılmaz.

- 🧩 **Modüler Mimari**  
  Temiz kod yapısı sayesinde kolayca geliştirilebilir ve yeni özellikler eklenebilir.

- ⚡ **Hızlı Analiz**  
  JSON parsing kullanarak saniyeler içinde binlerce kaydı tarayabilir.

- 🌐 **OSINT Tabanlı Keşif**  
  Açık kaynak istihbaratı kullanarak hedef sistem hakkında bilgi toplar.

---

## 🚀 Kurulum ve Kullanım

Projeyi çalıştırmak için aşağıdaki adımları takip edin.

### 1️⃣ Projeyi Klonlayın

```bash
git clone https://github.com/besteberfint/RedRecon.git
cd RedRecon
```

### 2️⃣ Gerekli Kütüphaneleri Yükleyin

Bu araç, dış kaynaklardan veri çekmek için `requests` kütüphanesini kullanır.

```bash
pip install requests
```

### 3️⃣ Aracı Çalıştırın

#### Temel Kullanım

```bash
python main.py -d google.com
```

#### Yardım Menüsünü Görüntüleme

```bash
python main.py --help
```

---

## 🛠️ Teknik Detaylar

RedRecon, Certificate Transparency loglarını analiz ederek hedef domain’e ait alt alan adlarını keşfeder.

- HTTP istekleri için `requests` kütüphanesi kullanılır.
- Gelen veriler JSON formatında işlenir.
- Araç, hedef sisteme aktif istek göndermediği için tamamen pasif keşif yaklaşımı uygular.
- Modüler yapı sayesinde farklı veri kaynakları kolayca entegre edilebilir.

---

## ⚠️ Yasal Uyarı

Bu araç yalnızca eğitim, araştırma ve etik siber güvenlik çalışmaları amacıyla geliştirilmiştir.

Yetkisiz sistemler üzerinde yapılacak kullanımlar yasal sorumluluk doğurabilir. Geliştirici, kötü amaçlı kullanımlardan sorumlu tutulamaz.

---

## 👨‍💻 Geliştirici

**Beste Berfin TOPALOĞLU**
# IP Range Scanner

Proyek ini terdiri dari dua script Python untuk:

1. **Generate_IP** – Membuat daftar IP dalam range tertentu dan menyimpannya ke file `.txt` per batch (max 8 MB per file).
2. **Scanning** – Melakukan scanning ke setiap IP (HTTP) untuk mengecek apakah responnya memiliki **status code 200**.

## 📂 Struktur Proyek

```
.
├── Generate_IP.py        # Script untuk membuat daftar IP
├── Scanning.py           # Script untuk scanning IP
├── requirements.txt      # Daftar dependensi
├── README.md             # Dokumentasi proyek
└── ip_chunks_xx/         # Folder output hasil Generate_IP (xx = prefix IP)
```

---

## 📦 Instalasi

Pastikan Python 3.8+ sudah terpasang, lalu install dependensi:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
aiohttp
colorama
```

---

## 🚀 Cara Penggunaan

### 1. Generate Daftar IP
Jalankan script `Generate_IP` untuk membuat file daftar IP berdasarkan prefix yang diinput.

```bash
python Generate_IP.py
```

**Contoh input:**
```
Enter IP prefix (1–223): 18
```

Hasil akan tersimpan di folder:
```
ip_chunks_18/
```
Isi file akan berupa daftar IP seperti:
```
http://18.0.0.1:80
http://18.0.0.2:80
...
```

---

### 2. Scanning IP
Setelah daftar IP dibuat, jalankan script `Scanning.py` untuk mengecek status HTTP (200 OK).

```bash
python Scanning.py
```

**Contoh input:**
```
📂 Masukkan nama folder IP (contoh: ip_chunks_18): ip_chunks_18
```

Script akan:
- Menampilkan status setiap IP (`200 OK`, kode lain, atau error)
- Menyimpan IP dengan **status code 200** ke `success.txt`

---

## ⚙️ Pengaturan
Beberapa variabel penting di `Scanning.py`:
- `BATCH_SIZE` → Jumlah IP per batch (default 10,000)
- Timeout request: 5 detik
- Hanya menyimpan IP dengan status **200 OK**

---

## ⚠️ Disclaimer
Script ini hanya untuk **keperluan legal**, seperti:
- Pengujian jaringan internal
- Audit keamanan sistem yang Anda miliki atau mendapat izin resmi

Penggunaan untuk scanning jaringan publik tanpa izin **melanggar hukum** di banyak negara.

---

## 📜 Lisensi
MIT License © 2025

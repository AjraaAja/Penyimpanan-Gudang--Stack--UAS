# 📦 Sistem Manajemen Gudang (Stack LIFO)

Aplikasi simulasi sistem manajemen gudang berbasis web menggunakan **Python** dan **Streamlit**. Proyek ini menerapkan struktur data **Stack (Tumpukan)** yang dibangun secara manual menggunakan konsep **Linked List (Node)** untuk memastikan efisiensi memori dan memberikan pemahaman mendalam tentang cara kerja alokasi memori.

---

## 🏗️ Penjelasan Struktur Data

Aplikasi ini tidak menggunakan tipe data *List* bawaan Python (seperti `[]`), melainkan membangun struktur datanya sendiri dari nol menggunakan dua komponen utama:

### 1. Konsep LIFO (Last In, First Out)
Sistem ini menggunakan metode **Stack**. Analoginya seperti tumpukan kardus di gudang. Kardus yang ditaruh paling akhir (di atas tumpukan) adalah kardus pertama yang harus diambil jika kita ingin mengosongkan gudang.
* **Push (Insert):** Menaruh barang baru di puncak tumpukan.
* **Pop (Delete):** Mengambil barang dari puncak tumpukan.

### 2. Implementasi Linked List (Class Node)
Setiap barang yang masuk ke gudang dibungkus dalam sebuah objek bernama `Node`.
* **`data`**: Menyimpan nama barang.
* **`next`**: Berfungsi sebagai penunjuk (*pointer*) ke barang yang ada di bawahnya.

Ketika sebuah barang di-*pop* (dihapus), penunjuk `next` akan diputus. Hal ini memungkinkan sistem pengumpulan sampah memori (*Garbage Collector*) pada Python untuk langsung membersihkan memori barang tersebut, sehingga program berjalan sangat efisien.

--
## 📂 Struktur Berkas (Project Structure)

Pembuatan kode memisahkan antarmuka pengguna (UI) dan logika dasar secara tegas (*Separation of Concerns*):

* `logic.py` : Berisi *Blueprint* atau logika murni struktur data (`Class Node` dan `Class WarehouseStack`). Tidak ada kode antarmuka di sini.
* `app.py` : Berisi kode *Frontend* menggunakan Streamlit untuk interaksi pengguna secara *real-time*.
* `warehouse_data.json` : Berkas penyimpanan data (*database* lokal) yang terbuat secara otomatis untuk mencegah hilangnya data saat halaman dimuat ulang (*refresh*).

📥 Clone Proyek
Untuk mendapatkan salinan proyek ini ke komputer lokal, gunakan perintah berikut pada Terminal atau Command Prompt (CMD):
Bash
git clone https://github.com/AjraaAja/Penyimpanan-Gudang--Stack--UAS.git
Kemudian masuk ke direktori proyek:
Bash
cd Penyimpanan-Gudang--Stack--UAS
Setelah itu, instal dependensi yang diperlukan dan jalankan aplikasi menggunakan Streamlit:
Bash
pip install streamlit
streamlit run app.py
Atau
jalankan perintah berikut untuk mengunduh kode program ini ke komputermu:
bash
git clone [https://github.com/username-github-kalian/nama-repositori.git](https://github.com/username-github-kalian/nama-repositori.git)
cd nama-repositori
(Catatan: Jangan lupa ubah URL di atas dengan link repositori GitHub kalian yang sebenarnya).


## 🚀 Cara Instalasi dan Menjalankan Program

Untuk menjalankan aplikasi ini di komputer lokal, ikuti langkah-langkah sederhana berikut:

### Persiapan Prasyarat
Pastikan komputer kamu sudah terinstal **Python**. Jika belum, unduh dan instal dari [python.org](https://www.python.org/).

### 1. Instalasi Streamlit
Buka Terminal atau Command Prompt (CMD), lalu jalankan perintah berikut untuk menginstal pustaka antarmuka web Streamlit:
```bash
pip install streamlit

2. Menjalankan Aplikasi
Buka Terminal / CMD.

Arahkan direktori (gunakan perintah cd) ke folder tempat kamu menyimpan berkas app.py dan logic.py.

Jalankan perintah berikut:

Bash
streamlit run app.py

Membuka Aplikasi
Setelah perintah dijalankan, peramban web (browser) akan otomatis terbuka dan menampilkan aplikasi di alamat lokal

💡 Fitur Utama
Pemisahan Logika & UI: Mencegah kode berantakan (spaghetti code).

Visualisasi Real-Time: Penambahan dan pengurangan barang langsung terlihat di layar tanpa delay.

Persistensi Data (Anti-Hilang): Data gudang otomatis tersimpan di .json. Jika browser tertutup atau di-refresh tidak sengaja, tumpukan barang tetap aman dan kembali seperti semula.

Fitur Pencarian: Mampu mencari posisi spesifik suatu barang di dalam tumpukan yang besar.

🤝 Kontribusi pada Proyek
Proyek Sistem Manajemen Gudang (Stack LIFO) ini dikembangkan secara kolaboratif dengan pembagian tugas sebagai berikut:
Nama
Kontribusi
Azzumardhi Azzra
Merancang dan mengimplementasikan logika utama struktur data Stack berbasis Linked List pada logic.py, serta mengembangkan mekanisme persistensi data menggunakan warehouse_data.json.
Abdillah Az Jauzaqi
Mengembangkan antarmuka pengguna (frontend) berbasis Streamlit pada app.py, termasuk visualisasi data, formulir interaksi, dan pengelolaan tampilan aplikasi secara real-time.
Setiap anggota berkontribusi sesuai dengan tanggung jawabnya untuk menghasilkan aplikasi yang menerapkan konsep Last In, First Out (LIFO) secara efektif serta memberikan pengalaman penggunaan yang interaktif dan mudah dipahami.

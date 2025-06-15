# 🍽️ Food Recommendation AI Chatbot 🤖

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## Deskripsi Proyek

Proyek ini adalah implementasi sebuah **Chatbot AI (Artificial Intelligence) interaktif** yang dirancang untuk memberikan rekomendasi dan informasi seputar makanan. Dibangun sebagai demonstrasi konsep dasar AI untuk tugas kuliah, chatbot ini mampu berinteraksi dengan pengguna melalui antarmuka web yang sederhana namun fungsional.

Chatbot ini menonjolkan aspek **AI Simbolik** dengan pendekatan **Sistem Berbasis Aturan (Rule-Based System)** dan **Sistem Pakar (Expert System)**, di mana pengetahuannya dieksternalisasi dan logikanya dirancang secara eksplisit.

## Fitur Utama

* **Rekomendasi Makanan Berdasarkan Kategori:** Merekomendasikan makanan berdasarkan kategori seperti manis, pedas, sehat, ringan, atau berat.
* **Rekomendasi Makanan Khas Daerah:** Menyajikan daftar makanan khas dari berbagai daerah di seluruh Indonesia.
* **Saran Menu Harian:** Memberikan ide menu makanan untuk pagi, siang, dan malam.
* **Informasi Kalori & Gizi:** Menjelaskan jenis makanan berdasarkan kandungan gizi (tinggi kalori, tinggi protein, rendah kalori, tinggi serat).
* **Pemrosesan Bahasa Alami (NLP) Dasar:** Mampu "memahami" niat pengguna dari berbagai variasi pertanyaan melalui analisis kata kunci dan pola kalimat.
* **Antarmuka Pengguna Interaktif:** Disajikan dalam bentuk aplikasi web lokal yang responsif dan mudah digunakan.

## Konsep AI yang Diimplementasikan

Proyek ini menjadi studi kasus yang sangat baik untuk memahami dasar-dasar AI melalui konsep-konsep berikut:

1.  **Representasi Pengetahuan:** Informasi tentang makanan, kategori, dan saran disimpan dalam **file teks eksternal (.txt)**. Ini menunjukkan bagaimana pengetahuan dapat diorganisir dan diakses oleh sistem AI, memisahkan data dari logika inti aplikasi.
2.  **Pemrosesan Bahasa Alami (NLP) Dasar:** Chatbot menggunakan teknik **normalisasi teks** (mengubah input ke huruf kecil) dan **Regular Expressions (Regex)** untuk **pencocokan pola** dan **identifikasi niat (intent recognition)**. Ini adalah langkah fundamental dalam memungkinkan mesin berinteraksi dengan bahasa manusia.
3.  **Inferensi Berbasis Aturan:** Sistem ini membuat "keputusan" dan memberikan respons berdasarkan serangkaian **aturan `IF-THEN` yang telah ditentukan secara eksplisit**. Ini adalah inti dari sistem pakar, di mana logika penalaran didasarkan pada pengetahuan yang telah dikodekan.
4.  **Generasi Respon Sederhana:** Bot menghasilkan teks respons yang relevan dan bervariasi (menggunakan elemen acak) sebagai tanggapan terhadap pertanyaan pengguna.

## Tools dan Teknologi

* **Bahasa Pemrograman:** [Python](https://www.python.org/) (versi 3.x)
* **Framework Aplikasi Web:** [Streamlit](https://streamlit.io/)
* **Library NLP/Teks:** `re` (Regular Expressions)
* **Library Utilitas:** `random`, `os`
* **Manajemen Data:** File `.txt` eksternal untuk basis pengetahuan.
* **Lingkungan Pengembangan:** [Visual Studio Code (VS Code)](https://code.visualstudio.com/)

## Struktur Proyek
├── chatbot_makanan_final.py  # Kode utama aplikasi chatbot Streamlit
├── kategori_makanan.txt      # Data kategori makanan (manis, pedas, dll.)
├── makanan_daerah.txt        # Data makanan khas daerah
├── saran_menu_harian.txt     # Data saran menu harian
├── info_gizi.txt             # Data informasi kalori dan gizi
├── general_responses.txt     # Data respons umum (salam, pamit)
└── README.md                 # File deskripsi proyek (ini sendiri)


## Cara Menjalankan Aplikasi (Lokal)

Ikuti langkah-langkah di bawah ini untuk menjalankan chatbot di komputer Anda:

1.  **Clone Repository Ini:**
    Buka Terminal atau Command Prompt Anda, lalu ketik:
    ```bash
    git clone [https://github.com/NamaUserGitHubAnda/NamaRepoAnda.git](https://github.com/NamaUserGitHubAnda/NamaRepoAnda.git)
    cd NamaRepoAnda
    ```
    *(Ganti `NamaUserGitHubAnda/NamaRepoAnda` dengan alamat repo Anda)*

2.  **Instal Python 3.x (jika belum):**
    Unduh dari [python.org](https://www.python.org/downloads/). Pastikan untuk mencentang "Add Python to PATH" saat instalasi.

3.  **Instal Visual Studio Code (VS Code) (opsional, tapi direkomendasikan):**
    Unduh dari [code.visualstudio.com](https://code.visualstudio.com/download).

4.  **Instal Dependensi Python:**
    Buka Terminal atau Command Prompt Anda (atau Terminal di VS Code). Navigasikan ke direktori proyek (`cd NamaRepoAnda`). Kemudian, instal Streamlit:
    ```bash
    pip install streamlit
    ```

5.  **Jalankan Aplikasi Streamlit:**
    Di Terminal/Command Prompt yang sama, jalankan perintah berikut:
    ```bash
    streamlit run chatbot_makanan_final.py
    ```

6.  **Akses Aplikasi:**
    Aplikasi akan otomatis terbuka di *web browser* Anda (biasanya di `http://localhost:8501`). Jika tidak, buka URL tersebut secara manual.

## Contoh Interaksi

Anda bisa mencoba berbagai pertanyaan berikut:

* `Rekomendasi makanan pedas dong`
* `Hari ini makan apa ya?`
* `Rekomen makanan yang tinggi kalori`
* `Makanan khas Jogja apa?`
* `Halo`
* `Terima kasih`

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
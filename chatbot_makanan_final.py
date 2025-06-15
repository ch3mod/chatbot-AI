# chatbot_makanan_final.py

# --- 1. Impor Library ---
import streamlit as st
import random
import re
import os

# --- 2. Fungsi untuk Membaca Data dari File TXT ---
def load_data_from_txt(filepath):
    """Membaca data key:value dari file TXT."""
    data = {}
    if not os.path.exists(filepath):
        st.error(f"Error: File data tidak ditemukan di {filepath}. Pastikan file TXT ada di folder yang sama.")
        return data

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip() 
            if not line or line.startswith('#'):
                continue
            
            parts = line.split(':', 1)
            if len(parts) == 2:
                key = parts[0].strip()
                values_str = parts[1].strip()
                values_list = [v.strip() for v in values_str.split(',')]
                data[key] = values_list
    return data

def load_all_knowledge_base():
    """Menggabungkan data dari semua file TXT ke dalam satu basis pengetahuan."""
    knowledge_base = {}

    # Load Kategori Makanan
    kategori_data = load_data_from_txt('kategori_makanan.txt')
    # Khusus untuk "khas daerah", kita perlu memisahkan key-nya (daerah)
    daerah_data = load_data_from_txt('makanan_daerah.txt')
    
    # Membangun struktur kategori_makanan yang benar
    knowledge_base["kategori_makanan"] = {
        k: v for k, v in kategori_data.items() # Tambahkan kategori umum
    }
    knowledge_base["kategori_makanan"]["khas daerah"] = {
        k: v for k, v in daerah_data.items() # Tambahkan sub-kategori daerah
    }

    # Load Saran Menu Harian
    knowledge_base["saran_menu_harian"] = load_data_from_txt('saran_menu_harian.txt')

    # Load Info Gizi
    knowledge_base["info_gizi"] = load_data_from_txt('info_gizi.txt')

    # Load Respon Umum
    general_responses = load_data_from_txt('general_responses.txt')
    knowledge_base["salam"] = general_responses.get("salam", ["Halo!"]) # Default jika tidak ada
    knowledge_base["pamit"] = general_responses.get("pamit", ["Sampai jumpa!"]) # Default jika tidak ada

    return knowledge_base

# Panggil fungsi untuk memuat semua data ke dalam data_pengetahuan
data_pengetahuan = load_all_knowledge_base()

# --- 3. Logika Utama Chatbot (Fungsi proses_query) ---
def proses_query(query):
    query_lower = query.lower()

    # Fitur 1: Rekomendasi Makanan Berdasarkan Kategori (Manis, Pedas, Sehat, dll.)
    for kategori, daftar_makanan in data_pengetahuan["kategori_makanan"].items():
        if kategori == "khas daerah":
            continue
        
        if re.search(r'\b(?:rekomendasi|cari|makanan|mau|apa)\s*(?:makanan)?\s*(?:jenis|yang)?\s*' + re.escape(kategori) + r'\b(?: dong|apa)?', query_lower) or \
           re.search(r'\b' + re.escape(kategori) + r'\b.*\b(?:rekomendasi|dong|apa|makanan)\b', query_lower):
            
            rekomendasi = random.sample(daftar_makanan, min(3, len(daftar_makanan)))
            return f"Coba deh {', '.join(rekomendasi)}."

    # Fitur 2: Rekomendasi Makanan Khas Daerah
    match_daerah = re.search(r'\b(?:makanan khas|kuliner|apa makanan|makanan dari|asal)\s*([a-z]+)\b', query_lower)
    if match_daerah:
        daerah_dicari = match_daerah.group(1)
        if daerah_dicari in data_pengetahuan["kategori_makanan"]["khas daerah"]:
            rekomendasi_daerah = data_pengetahuan["kategori_makanan"]["khas daerah"][daerah_dicari]
            return f"Makanan khas {daerah_dicari.capitalize()} antara lain: {', '.join(rekomendasi_daerah)}."
        else:
            return f"Maaf, saya belum punya data makanan khas untuk daerah **{daerah_dicari.capitalize()}**. Coba tanyakan daerah lain seperti Jogja, Bandung, atau Padang."

    # Fitur 3: Saran Menu Harian
    if "hari ini makan apa" in query_lower or "makan apa ya" in query_lower or "menu hari ini" in query_lower or "makan apa sekarang" in query_lower:
        pagi = random.choice(data_pengetahuan["saran_menu_harian"]["pagi"])
        siang = random.choice(data_pengetahuan["saran_menu_harian"]["siang"])
        malam = random.choice(data_pengetahuan["saran_menu_harian"]["malam"])
        return f"Gimana kalau pagi ini {pagi}, siang {siang}, dan malam {malam}?"

    # Fitur 4: Info Kalori atau Gizi
    for jenis_gizi, daftar_item in data_pengetahuan["info_gizi"].items():
        if re.search(r'\b(?:rekomendasi|info|cari|makanan yang|apa makanan|apa itu)\s*(?:yang)?\s*' + re.escape(jenis_gizi) + r'\b', query_lower):
            return f"{jenis_gizi.capitalize()} bisa didapat dari: {', '.join(daftar_item)}. Dan lain-lain."

    # Respon Umum: Salam Pembuka dan Penutup
    if any(kata in query_lower for kata in ["halo", "hai", "hi", "selamat", "pagi", "siang", "malam", "assalamualaikum"]):
        return random.choice(data_pengetahuan["salam"])
    
    if any(kata in query_lower for kata in ["terima kasih", "makasih", "bye", "sampai jumpa", "dadah", "wassalamualaikum"]):
        return random.choice(data_pengetahuan["pamit"])

    # Respon Default: Jika tidak ada pola yang cocok
    return "Maaf, saya belum memahami pertanyaan Anda. Saya hanya bisa memberikan informasi tentang:\n" \
           "- **Rekomendasi Makanan** berdasarkan kategori (manis, pedas, sehat, ringan, berat)\n" \
           "- **Saran Menu Harian**\n" \
           "- **Info Gizi** (tinggi kalori/protein, rendah kalori, tinggi serat)\n" \
           "- **Makanan Khas Daerah** (Jogja, Bandung, Surabaya, Padang, Medan, Jakarta, Semarang, Malang)\n"\
           "Coba tanyakan dengan contoh seperti: 'Rekomendasi makanan pedas dong' atau 'Makanan khas Bandung apa?'"

# --- 4. Antarmuka Pengguna dengan Streamlit (UI) ---
# Bagian ini sama seperti sebelumnya, tidak perlu diubah kecuali Anda mau menambahkan elemen UI lain.

st.title("🍽️ Chatbot Rekomendasi Makanan 🤖")
st.markdown("---")

st.write("Halo! Saya chatbot yang siap bantu kamu mencari informasi dan rekomendasi makanan.")
st.write("Silakan ajukan pertanyaanmu di bawah ini. Contoh:")
st.markdown("""
* **Rekomendasi Kategori:** `rekomendasi makanan pedas dong`
* **Saran Menu Harian:** `Hari ini makan apa ya?`
* **Info Gizi:** `Rekomen makanan yang tinggi kalori`
* **Makanan Khas Daerah:** `Makanan khas Jogja apa?`
""")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ketik pertanyaan Anda di sini...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = proses_query(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

if st.button("Mulai Chat Baru"):
    st.session_state.messages = []
    st.rerun()

st.markdown("---")
st.caption("Dibuat untuk Tugas AI Mahasiswa | Angkatan 2025")
import streamlit as st
from logic import WarehouseStack

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Gudang LIFO Persisten", page_icon="🏢", layout="wide")

# --- INISIALISASI SESSION STATE ---
# Jika user melakukan refresh (F5), session_state kosong. 
# Baris di bawah akan membuat objek baru, dan objek tersebut otomatis membaca file JSON yang tersimpan.
if 'warehouse' not in st.session_state:
    st.session_state.warehouse = WarehouseStack()

# --- HEADER TAMPILAN ---
st.title("🏢 Sistem Gudang LIFO (Anti-Loss Data)")
st.markdown("Data tetap aman tersimpan meskipun halaman browser Anda **direfresh (F5)**.")
st.divider()

# --- LAYOUT HALAMAN ---
col_kontrol, col_visual = st.columns([1, 2])

# KOLOM KIRI: Form Input dan Manipulasi Data
with col_kontrol:
    st.header("⚙️ Kontrol Data")
    
    # 1. INSERT DATA (FORM)
    with st.form("insert_form", clear_on_submit=True):
        st.subheader("📥 Insert (Push)")
        new_item = st.text_input("Nama Barang:", placeholder="Ketik nama barang...")
        submit_insert = st.form_submit_button("Tambah ke Tumpukan", use_container_width=True)
        
        if submit_insert:
            if new_item.strip():
                st.session_state.warehouse.push(new_item.strip())
                st.success(f"'{new_item}' berhasil disimpan secara permanen!")
                st.rerun()
            else:
                st.error("Input tidak boleh kosong!")

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. DELETE DATA
    st.subheader("📤 Delete (Pop)")
    if st.button("Ambil Barang Paling Atas", use_container_width=True, type="primary"):
        popped = st.session_state.warehouse.pop()
        if popped:
            st.success(f"Berhasil mengambil '{popped}'!")
            st.rerun()
        else:
            st.warning("Gudang kosong! Tidak ada data yang bisa di-pop.")

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. TRAVERSAL / SEARCH DATA
    st.subheader("🔍 Search Data")
    search_query = st.text_input("Cari Barang:", placeholder="Nama barang yang dicari...")
    if st.button("Cari Posisi", use_container_width=True):
        if search_query.strip():
            pos = st.session_state.warehouse.search(search_query.strip())
            if pos != -1:
                st.info(f"Barang '{search_query}' ditemukan di urutan ke-{pos} dari atas.")
            else:
                st.error(f"Barang '{search_query}' tidak ditemukan di dalam tumpukan.")
        else:
            st.warning("Masukkan nama barang untuk mencari.")


# KOLOM KANAN: Visualisasi Real-Time
with col_visual:
    st.header("📊 Visualisasi Gudang (Real-Time)")
    
    current_size = st.session_state.warehouse.size()
    top_item = st.session_state.warehouse.peek() or "Gudang Kosong"
    stack_data = st.session_state.warehouse.get_all()
    
    # Indikator Cepat (Metrics)
    m1, m2 = st.columns(2)
    m1.metric("Total Node (Barang)", f"{current_size} Unit")
    m2.metric("Head Node (Paling Atas)", top_item)
    
    st.markdown("### 🗄️ Tumpukan Saat Ini")
    
    if not stack_data:
        st.info("Visualisasi kosong. Silakan insert barang melalui form di samping kiri.")
    else:
        # Merender tampilan dinamis
        with st.container(border=True):
            for i, item in enumerate(stack_data):
                if i == 0:
                    st.success(f"**TOP (Keluar Pertama)** ➔ {item}", icon="🟢")
                elif i == len(stack_data) - 1:
                    st.markdown(f"📦 {item} *(Dasar Gudang)*")
                else:
                    st.markdown(f"📦 {item}")
                
                if i < len(stack_data) - 1:
                    st.divider()
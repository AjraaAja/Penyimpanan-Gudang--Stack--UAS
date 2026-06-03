import json
import os

class Node:
    """Class untuk merepresentasikan satu entitas (barang) dalam memori."""
    def __init__(self, data):
        self.data = data
        self.next = None

class WarehouseStack:
    """Class Stack manual menggunakan konsep Linked List dengan fitur Auto-Save."""
    def __init__(self, storage_file="warehouse_data.json"):
        self.top = None
        self._size = 0
        self.storage_file = storage_file
        # Otomatis muat data lama jika file penyimpanan ditemukan
        self.load_from_json()

    def is_empty(self):
        return self.top is None

    def push(self, data):
        """Metode Insert: Menambahkan barang di atas tumpukan (Head)."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        self.save_to_json()  # Simpan setiap kali ada perubahan

    def pop(self):
        """Metode Delete: Mengambil dan menghapus barang dari atas tumpukan."""
        if self.is_empty():
            return None
        
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        
        popped_node.next = None
        self.save_to_json()  # Simpan setiap kali ada perubahan
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        return self._size

    def search(self, target_data):
        """Metode Traversal/Search: Mencari posisi barang dari atas ke bawah."""
        current = self.top
        position = 1
        while current is not None:
            if current.data.lower() == target_data.lower():
                return position
            current = current.next
            position += 1
        return -1

    def get_all(self):
        """Metode Traversal: Mengumpulkan semua data untuk visualisasi UI."""
        elements = []
        current = self.top
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements

    def save_to_json(self):
        """Menyimpan seluruh isi stack ke file JSON untuk persistensi data saat refresh."""
        # Kumpulkan data menjadi list biasa untuk kebutuhan serialisasi JSON
        data_list = self.get_all()
        # Karena get_all mengambil dari TOP ke BOTTOM, kita balik (reverse) 
        # agar saat dimuat ulang urutan push-nya tetap sama dari bawah.
        data_list.reverse() 
        
        with open(self.storage_file, "w") as f:
            json.dump(data_list, f)

    def load_from_json(self):
        """Memuat data dari file JSON jika file tersebut tersedia."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data_list = json.load(f)
                
                # Reset stack terlebih dahulu sebelum memuat data
                self.top = None
                self._size = 0
                
                # Masukkan kembali data ke dalam struktur Node
                for item in data_list:
                    # Memanggil struktur push internal tanpa memicu save_to_json berulang
                    new_node = Node(item)
                    new_node.next = self.top
                    self.top = new_node
                    self._size += 1
            except Exception:
                # Jika file korup atau gagal dibaca, inisialisasi sebagai stack kosong
                self.top = None
                self._size = 0
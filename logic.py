class Node:
    """Class untuk merepresentasikan satu entitas (barang) dalam memori."""
    def __init__(self, data):
        self.data = data
        self.next = None

class WarehouseStack:
    """Class Stack manual menggunakan konsep Linked List (tanpa list bawaan Python)."""
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        """Metode Insert: Menambahkan barang di atas tumpukan (Head)."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Metode Delete: Mengambil dan menghapus barang dari atas tumpukan."""
        if self.is_empty():
            return None
        
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        
        # Menghapus referensi untuk efisiensi memori
        popped_node.next = None
        return popped_node.data

    def peek(self):
        """Melihat data paling atas tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        """Mengembalikan jumlah total barang saat ini."""
        return self._size

    def search(self, target_data):
        """Metode Traversal/Search: Mencari posisi barang dari atas ke bawah."""
        current = self.top
        position = 1
        
        while current is not None:
            # Pencarian dibuat tidak case-sensitive
            if current.data.lower() == target_data.lower():
                return position
            current = current.next
            position += 1
            
        return -1  # Mengembalikan -1 jika barang tidak ditemukan

    def get_all(self):
        """Metode Traversal: Mengumpulkan semua data untuk visualisasi UI."""
        elements = []
        current = self.top
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements
import tkinter as tk
from tkinter import messagebox

# ==================== DATA GEJALA ====================
daftar_gejala = [
    ("G01", "Apakah komputer tidak mau menyala sama sekali?"),
    ("G02", "Apakah komputer sering restart sendiri?"),
    ("G03", "Apakah layar muncul blue screen?"),
    ("G04", "Apakah ada bunyi beep saat booting?"),
    ("G05", "Apakah komputer cepat panas?"),
    ("G06", "Apakah kipas komputer berisik?"),
    ("G07", "Apakah komputer mati mendadak saat dipakai?"),
    ("G08", "Apakah layar monitor tidak menampilkan gambar?"),
    ("G09", "Apakah layar bergaris-garis atau kacau?"),
    ("G10", "Apakah harddisk tidak terdeteksi?"),
    ("G11", "Apakah komputer loading sangat lambat?"),
    ("G12", "Apakah file sering corrupt atau hilang?"),
]

# ==================== BASIS PENGETAHUAN ====================
pengetahuan = {
    "RAM Rusak": {
        "gejala": ["G02", "G03", "G04"],
        "solusi": "Bersihkan pin RAM dengan penghapus, lalu pasang kembali."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["G01", "G02", "G07"],
        "solusi": "Periksa kabel power, coba dengan PSU lain, ganti jika perlu."
    },
    "Overheat (Prosesor Kepanasan)": {
        "gejala": ["G05", "G06", "G07"],
        "solusi": "Bersihkan debu di kipas dan heatsink, ganti thermal paste."
    },
    "VGA Bermasalah": {
        "gejala": ["G08", "G09", "G03"],
        "solusi": "Bersihkan pin VGA, pasang ulang, atau ganti VGA baru."
    },
    "Harddisk Corrupt": {
        "gejala": ["G10", "G11", "G12"],
        "solusi": "Backup data penting, jalankan chkdsk, ganti harddisk jika rusak."
    }
}

# ==================== FUNGSI INFERENSI ====================
def cari_kerusakan(gejala_user):
    # Cari kerusakan dengan jumlah gejala cocok terbanyak
    kerusakan_terbaik = None
    jumlah_cocok_terbaik = 0
    
    for nama, data in pengetahuan.items():
        cocok = 0
        for g in gejala_user:
            if g in data["gejala"]:
                cocok += 1
        
        if cocok > jumlah_cocok_terbaik and cocok >= 2:
            jumlah_cocok_terbaik = cocok
            kerusakan_terbaik = nama
    
    return kerusakan_terbaik

# ==================== KELAS APLIKASI ====================
class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Komputer")
        self.root.geometry("500x380")
        self.root.configure(bg="#e8e8e8")
        
        # State
        self.index_pertanyaan = 0
        self.gejala_user = []
        self.sesi_aktif = False
        
        self.buat_widget()
        
    def buat_widget(self):
        # Judul
        judul = tk.Label(
            self.root,
            text="SISTEM PAKAR DIAGNOSA KOMPUTER",
            font=("Arial", 14, "bold"),
            bg="#e8e8e8"
        )
        judul.pack(pady=15)
        
        # Frame pertanyaan
        self.frame_pertanyaan = tk.Frame(
            self.root,
            bg="white",
            relief="groove",
            bd=2,
            padx=15,
            pady=30
        )
        self.frame_pertanyaan.pack(padx=20, pady=10, fill="both", expand=True)
        
        self.label_pertanyaan = tk.Label(
            self.frame_pertanyaan,
            text="",
            font=("Arial", 11),
            bg="white",
            wraplength=420,
            justify="center"
        )
        self.label_pertanyaan.pack(expand=True)
        
        self.label_progress = tk.Label(
            self.root,
            text="",
            font=("Arial", 9),
            bg="#e8e8e8",
            fg="gray"
        )
        self.label_progress.pack()
        
        # Frame tombol
        frame_tombol = tk.Frame(self.root, bg="#e8e8e8")
        frame_tombol.pack(pady=15)
        
        self.btn_ya = tk.Button(
            frame_tombol,
            text="YA",
            font=("Arial", 10, "bold"),
            bg="#2ecc71",
            fg="white",
            width=10,
            command=self.jawab_ya
        )
        
        self.btn_tidak = tk.Button(
            frame_tombol,
            text="TIDAK",
            font=("Arial", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            width=10,
            command=self.jawab_tidak
        )
        
        self.btn_mulai = tk.Button(
            self.root,
            text="MULAI DIAGNOSA",
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=5,
            command=self.mulai
        )
        self.btn_mulai.pack(pady=10)
        
    def mulai(self):
        self.index_pertanyaan = 0
        self.gejala_user = []
        self.sesi_aktif = True
        
        self.btn_mulai.pack_forget()
        self.btn_ya.pack(side="left", padx=5)
        self.btn_tidak.pack(side="right", padx=5)
        
        self.tampil_pertanyaan()
        
    def tampil_pertanyaan(self):
        if self.index_pertanyaan < len(daftar_gejala):
            kode, pertanyaan = daftar_gejala[self.index_pertanyaan]
            self.label_pertanyaan.config(text=pertanyaan)
            self.label_progress.config(
                text=f"Pertanyaan {self.index_pertanyaan + 1} dari {len(daftar_gejala)}"
            )
        else:
            self.selesai()
    
    def jawab_ya(self):
        if self.sesi_aktif:
            kode = daftar_gejala[self.index_pertanyaan][0]
            self.gejala_user.append(kode)
            self.index_pertanyaan += 1
            self.tampil_pertanyaan()
    
    def jawab_tidak(self):
        if self.sesi_aktif:
            self.index_pertanyaan += 1
            self.tampil_pertanyaan()
    
    def selesai(self):
        self.sesi_aktif = False
        
        self.btn_ya.pack_forget()
        self.btn_tidak.pack_forget()
        
        # Cari kerusakan
        kerusakan = cari_kerusakan(self.gejala_user)
        
        # Tampilkan hasil
        self.tampil_hasil(kerusakan)
        
        self.btn_mulai.pack(pady=10)
    
    def tampil_hasil(self, kerusakan):
        # Buat window hasil
        window_hasil = tk.Toplevel(self.root)
        window_hasil.title("Hasil Diagnosa")
        window_hasil.geometry("450x350")
        window_hasil.configure(bg="#f0f0f0")
        
        # Judul
        judul = tk.Label(
            window_hasil,
            text="HASIL DIAGNOSA",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0"
        )
        judul.pack(pady=15)
        
        # Frame isi
        frame_isi = tk.Frame(window_hasil, bg="white", relief="groove", bd=1)
        frame_isi.pack(fill="both", expand=True, padx=20, pady=10)
        
        if kerusakan is None:
            # Tidak ada kerusakan
            label_hasil = tk.Label(
                frame_isi,
                text="TIDAK DITEMUKAN KERUSAKAN",
                font=("Arial", 12, "bold"),
                bg="white",
                fg="#e74c3c"
            )
            label_hasil.pack(pady=20)
            
            label_saran = tk.Label(
                frame_isi,
                text="Bawa komputer ke teknisi untuk pengecekan lebih lanjut.",
                font=("Arial", 10),
                bg="white",
                wraplength=350
            )
            label_saran.pack(pady=10)
        else:
            # Ada kerusakan
            label_hasil = tk.Label(
                frame_isi,
                text=kerusakan,
                font=("Arial", 12, "bold"),
                bg="white",
                fg="#2c3e50"
            )
            label_hasil.pack(pady=20)
            
            label_solusi = tk.Label(
                frame_isi,
                text=f"SOLUSI:\n{pengetahuan[kerusakan]['solusi']}",
                font=("Arial", 10),
                bg="white",
                justify="left",
                wraplength=380
            )
            label_solusi.pack(pady=10)
        
        # Tombol tutup
        btn_tutup = tk.Button(
            window_hasil,
            text="Tutup",
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            padx=15,
            command=window_hasil.destroy
        )
        btn_tutup.pack(pady=15)
        
        # Reset tampilan utama
        self.label_pertanyaan.config(text="Klik Mulai Diagnosa untuk memulai")
        self.label_progress.config(text="")

# ==================== MAIN ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPakar(root)
    root.mainloop()

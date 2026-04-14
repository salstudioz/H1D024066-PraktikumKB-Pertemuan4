
# Sistem Pakar Diagnosa Kerusakan Komputer/Laptop

Sistem ini merupakan aplikasi sederhana berbasis *rule-based expert system* untuk membantu mendiagnosa kerusakan pada komputer atau laptop berdasarkan gejala yang dialami pengguna.

Program dibuat menggunakan Python dengan antarmuka GUI dari Tkinter, serta menggunakan metode tanya jawab (YA/TIDAK).

---

## Deskripsi Singkat

Pengguna akan menjawab beberapa pertanyaan terkait gejala yang muncul pada komputer. Berdasarkan jawaban tersebut, sistem akan mencocokkan dengan knowledge base dan menampilkan hasil diagnosa berupa satu jenis kerusakan yang paling sesuai beserta solusinya.

---

## Cara Kerja Sistem

### 1. Knowledge Base

Sistem memiliki 5 jenis kerusakan, masing-masing memiliki beberapa gejala dan solusi:

* **RAM Rusak**
  Gejala: G02, G03, G04
  Solusi: Bersihkan pin RAM dengan penghapus, lalu pasang kembali

* **PSU Lemah**
  Gejala: G01, G02, G07
  Solusi: Cek kabel power, coba PSU lain, ganti jika perlu

* **Overheat**
  Gejala: G05, G06, G07
  Solusi: Bersihkan kipas dan heatsink, ganti thermal paste

* **VGA Bermasalah**
  Gejala: G08, G09, G03
  Solusi: Bersihkan dan pasang ulang VGA, atau ganti

* **Harddisk Corrupt**
  Gejala: G10, G11, G12
  Solusi: Backup data, jalankan chkdsk, ganti harddisk jika rusak

---

### 2. Proses Tanya Jawab

* Sistem menampilkan 12 pertanyaan secara berurutan
* Pengguna memilih:

  * YA → gejala dicatat
  * TIDAK → dilewati
* Semua pertanyaan harus dijawab

---

### 3. Mesin Inferensi

Sistem menggunakan pencocokan jumlah gejala tanpa if-else panjang.

Aturan:

* Minimal 2 gejala harus cocok
* Dipilih kerusakan dengan jumlah kecocokan terbanyak
* Jika tidak memenuhi, maka dianggap tidak ditemukan kerusakan

Contoh fungsi:

```python
def cari_kerusakan(gejala_user):
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
```

---

### 4. Hasil Diagnosa

Jika ditemukan:

```
HASIL DIAGNOSA

RAM Rusak

SOLUSI:
Bersihkan pin RAM dengan penghapus, lalu pasang kembali.
```

Jika tidak ditemukan:

```
TIDAK DITEMUKAN KERUSAKAN

Bawa komputer ke teknisi untuk pengecekan lebih lanjut.
```

---

## Cara Menjalankan Program

Pastikan Python sudah terinstal, kemudian jalankan:

```bash
python tugas.py
```

---

## Cara Menggunakan

1. Klik tombol **MULAI DIAGNOSA**
2. Jawab semua pertanyaan dengan YA atau TIDAK
3. Setelah selesai, hasil diagnosa akan ditampilkan
4. Klik **Tutup** untuk kembali ke menu utama
5. Ulangi jika ingin mencoba lagi

---

## Daftar Gejala

* G01: Komputer tidak menyala
* G02: Komputer sering restart
* G03: Layar blue screen
* G04: Bunyi beep saat booting
* G05: Komputer cepat panas
* G06: Kipas berisik
* G07: Komputer mati mendadak
* G08: Monitor tidak menampilkan gambar
* G09: Layar bergaris
* G10: Harddisk tidak terdeteksi
* G11: Loading sangat lambat
* G12: File sering corrupt atau hilang

---

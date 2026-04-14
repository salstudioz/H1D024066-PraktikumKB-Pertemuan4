# malaria.py
# Penentuan penyakit berdasarkan gejala (tanpa interaksi pengguna)

# Database gejala untuk seseorang (misalnya 'steph')
gejala_steph = set()   # menyimpan gejala yang dimiliki steph

# Aturan penyakit
def penyakit(orang):
    """Mengembalikan daftar penyakit yang mungkin diderita orang berdasarkan gejalanya"""
    hasil = []
    g = gejala_steph if orang == "steph" else set()
    if {"nyeri_otot", "muntah", "kejang"}.issubset(g):
        hasil.append("Malaria Tertiana")
    if {"nyeri_otot", "menggigil", "tidak_enak_badan"}.issubset(g):
        hasil.append("Malaria Quartana")
    if {"keringat_dingin", "sakit_kepala", "mimisan", "mual"}.issubset(g):
        hasil.append("Malaria Tropika")
    if {"menggigil", "tidak_enak_badan", "demam", "mimisan", "mual"}.issubset(g):
        hasil.append("Malaria Pernisiosa")
    return hasil

# Simulasi percobaan (sesuai langkah di modul)
if __name__ == "__main__":
    print("=== Diagnosa Malaria (Simulasi) ===")
    print("1. Query awal (belum ada gejala):")
    print(f"   Penyakit Steph: {penyakit('steph')}")

    # assertz
    gejala_steph.update(["nyeri_otot", "menggigil", "tidak_enak_badan"])
    print("\n2. Setelah menambah nyeri_otot, menggigil, tidak_enak_badan:")
    print(f"   Penyakit Steph: {penyakit('steph')}")

    # retract nyeri_otot
    gejala_steph.discard("nyeri_otot")
    # assertz demam, mimisan, mual
    gejala_steph.update(["demam", "mimisan", "mual"])
    print("\n3. Setelah retract nyeri_otot, lalu tambah demam, mimisan, mual:")
    print(f"   Penyakit Steph: {penyakit('steph')}")
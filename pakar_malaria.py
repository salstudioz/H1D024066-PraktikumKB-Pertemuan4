# pakar_malaria.py
# Sistem pakar diagnosis malaria berbasis konsol (interaktif)

gejala_pos = set()
gejala_neg = set()

def pertanyaan(g):
    """Cetak pertanyaan untuk gejala g"""
    pertanyaan_map = {
        "nyeri_otot": "Apakah Anda merasa nyeri otot?",
        "muntah": "Apakah Anda muntah-muntah?",
        "kejang": "Apakah Anda mengalami kejang-kejang?",
        "menggigil": "Apakah Anda sering menggigil?",
        "tidak_enak_badan": "Apakah Anda merasa tidak enak badan?",
        "keringat_dingin": "Apakah Anda mengalami keringat dingin?",
        "sakit_kepala": "Apakah Anda sering sakit kepala?",
        "mimisan": "Apakah Anda sering mimisan?",
        "mual": "Apakah Anda merasa mual?",
        "demam": "Apakah Anda demam?"
    }
    print(pertanyaan_map.get(g, f"Apakah Anda mengalami {g}?"))

def diagnosa(g):
    """Tanyakan gejala g kepada user dan simpan jawaban"""
    pertanyaan(g)
    jawab = input("(y/t): ").strip().lower()
    if jawab == 'y':
        gejala_pos.add(g)
        return True
    else:
        gejala_neg.add(g)
        return False

def gejala(g):
    """Periksa status gejala: sudah positif, negatif, atau perlu ditanyakan"""
    if g in gejala_pos:
        return True
    if g in gejala_neg:
        return False
    # belum diketahui -> tanyakan
    return diagnosa(g)

def terdeteksi(nama_penyakit):
    print(f"Anda terdeteksi penyakit {nama_penyakit}")

def penyakit():
    """Evaluasi semua aturan penyakit, cetak hasil"""
    if gejala("nyeri_otot") and gejala("muntah") and gejala("kejang"):
        terdeteksi("Malaria Tertiana")
        return True
    if gejala("nyeri_otot") and gejala("menggigil") and gejala("tidak_enak_badan"):
        terdeteksi("Malaria Quartana")
        return True
    if gejala("keringat_dingin") and gejala("sakit_kepala") and gejala("mimisan") and gejala("mual"):
        terdeteksi("Malaria Tropika")
        return True
    if gejala("menggigil") and gejala("tidak_enak_badan") and gejala("demam") and gejala("mimisan") and gejala("mual"):
        terdeteksi("Malaria Pernisiosa")
        return True
    print("Tidak terdeteksi penyakit.")
    return False

def clear_db():
    """Bersihkan database gejala positif dan negatif"""
    gejala_pos.clear()
    gejala_neg.clear()

def main():
    while True:
        clear_db()
        print("\n" + "="*40)
        print("DIAGNOSA PENYAKIT MALARIA")
        print("="*40)
        penyakit()
        ulang = input("\nINGIN MENGULANG? (y/t): ").strip().lower()
        if ulang != 'y':
            break

if __name__ == "__main__":
    main()
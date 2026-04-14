# silsilah.py
# Sistem pakar sederhana untuk hubungan keluarga

# Fakta: parent(orang_tua, anak)
parent = [
    ("lya", "bima"),
    ("lya", "satria"),
    ("bima", "david"),
    ("bima", "emma"),
    ("satria", "yunita"),
    ("satria", "grace")
]

# Aturan
def sibling(X, Y):
    """X adalah saudara kandung Y jika mereka memiliki orang tua yang sama dan X != Y"""
    for Z, _ in parent:
        if (Z, X) in parent and (Z, Y) in parent and X != Y:
            return True
    return False

def grandparent(X, Y):
    """X adalah kakek/nenek dari Y jika X adalah orang tua dari Z dan Z adalah orang tua dari Y"""
    for Z, _ in parent:
        if (X, Z) in parent and (Z, Y) in parent:
            return True
    return False

def ancestor(X, Y):
    """X adalah leluhur Y jika X adalah orang tua Y, atau X adalah orang tua dari Z dan Z leluhur Y"""
    if (X, Y) in parent:
        return True
    for Z, _ in parent:
        if (X, Z) in parent and ancestor(Z, Y):
            return True
    return False

# Query contoh (seperti di modul)
if __name__ == "__main__":
    print("=== Silsilah Keluarga ===")
    print(f"Anak dari Bima   : {[child for p, child in parent if p == 'bima']}")
    print(f"Cucu dari Alya   : {[child for p, child in parent if grandparent('alya', child)]}")
    print(f"Apakah Bima dan Satria saudara? {sibling('bima', 'satria')}")
    print(f"Leluhur Emma     : {[p for p, _ in parent if ancestor(p, 'emma')]}")
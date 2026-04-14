# pakar_malaria_gui.py
# Sistem pakar diagnosis malaria dengan antarmuka Tkinter (tanpa Prolog)

import tkinter as tk
from tkinter import ttk, messagebox

# Basis pengetahuan: daftar penyakit dan gejala yang diperlukan
PENYAKIT_GEJALA = {
    "Malaria Tertiana": ["nyeri_otot", "muntah", "kejang"],
    "Malaria Quartana": ["nyeri_otot", "menggigil", "tidak_enak_badan"],
    "Malaria Tropika": ["keringat_dingin", "sakit_kepala", "mimisan", "mual"],
    "Malaria Pernisiosa": ["menggigil", "tidak_enak_badan", "demam", "mimisan", "mual"]
}

# Teks pertanyaan untuk setiap gejala
PERTANYAAN = {
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

class MalariaExpertGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosis Penyakit Malaria")
        self.root.geometry("500x350")

        # Variabel untuk menyimpan jawaban pengguna
        self.jawaban = {}          # {gejala: True/False}
        self.penyakit_list = list(PENYAKIT_GEJALA.keys())
        self.current_idx = 0       # penyakit ke berapa yang sedang diperiksa
        self.current_gejala_list = []
        self.current_gejala_idx = 0

        # Widget
        mainframe = ttk.Frame(root, padding="10")
        mainframe.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Aplikasi Diagnosa Penyakit Malaria",
                  font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Label(mainframe, text="Pertanyaan:").grid(row=1, column=0, sticky=tk.W)
        self.question_text = tk.Text(mainframe, height=4, width=50, state=tk.DISABLED, wrap=tk.WORD)
        self.question_text.grid(row=2, column=0, columnspan=3, pady=5)

        self.btn_no = ttk.Button(mainframe, text="Tidak", command=lambda: self.jawab(False), state=tk.DISABLED)
        self.btn_no.grid(row=3, column=1, padx=5, pady=10)
        self.btn_yes = ttk.Button(mainframe, text="Ya", command=lambda: self.jawab(True), state=tk.DISABLED)
        self.btn_yes.grid(row=3, column=2, padx=5, pady=10)

        self.btn_start = ttk.Button(mainframe, text="Mulai Diagnosa", command=self.mulai_diagnosa)
        self.btn_start.grid(row=4, column=1, columnspan=2, pady=10)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def mulai_diagnosa(self):
        """Reset dan mulai diagnosa"""
        self.jawaban.clear()
        self.current_idx = 0
        self.current_gejala_list = PENYAKIT_GEJALA[self.penyakit_list[0]]
        self.current_gejala_idx = 0

        self.btn_start.config(state=tk.DISABLED)
        self.btn_yes.config(state=tk.NORMAL)
        self.btn_no.config(state=tk.NORMAL)

        self.tanya_gejala_berikutnya()

    def tanya_gejala_berikutnya(self):
        """Tampilkan pertanyaan untuk gejala saat ini"""
        if self.current_idx >= len(self.penyakit_list):
            self.selesai_diagnosa()
            return

        penyakit = self.penyakit_list[self.current_idx]
        gejala_list = PENYAKIT_GEJALA[penyakit]

        if self.current_gejala_idx >= len(gejala_list):
            # Semua gejala penyakit ini sudah dijawab, cek apakah memenuhi
            if self.cekok_penyakit(penyakit):
                return  # sudah ditemukan, berhenti
            else:
                # lanjut ke penyakit berikutnya
                self.current_idx += 1
                if self.current_idx < len(self.penyakit_list):
                    self.current_gejala_list = PENYAKIT_GEJALA[self.penyakit_list[self.current_idx]]
                    self.current_gejala_idx = 0
                    self.tanya_gejala_berikutnya()
                else:
                    self.selesai_diagnosa()
            return

        gejala = gejala_list[self.current_gejala_idx]
        if gejala in self.jawaban:
            # Sudah pernah dijawab (bisa dari penyakit sebelumnya)
            self.current_gejala_idx += 1
            self.tanya_gejala_berikutnya()
            return

        # Tampilkan pertanyaan
        teks = PERTANYAAN.get(gejala, f"Apakah Anda mengalami {gejala}?")
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(tk.END, teks)
        self.question_text.config(state=tk.DISABLED)

        # Simpan gejala yang sedang ditanyakan untuk diproses di jawab()
        self.current_gejala = gejala

    def jawab(self, value):
        """Simpan jawaban dan lanjut ke gejala berikutnya"""
        self.jawaban[self.current_gejala] = value
        self.current_gejala_idx += 1
        self.tanya_gejala_berikutnya()

    def cekok_penyakit(self, penyakit):
        """Periksa apakah semua gejala penyakit terpenuhi (jawaban True)"""
        gejala_yg_diperlukan = PENYAKIT_GEJALA[penyakit]
        for g in gejala_yg_diperlukan:
            if self.jawaban.get(g, False) != True:
                return False
        # Terpenuhi -> diagnosa
        messagebox.showinfo("Hasil Diagnosa", f"Anda terdeteksi penyakit {penyakit}")
        self.selesai_diagnosa()
        return True

    def selesai_diagnosa(self):
        """Akhiri sesi diagnosa, tanyakan apakah ingin mengulang"""
        self.btn_start.config(state=tk.NORMAL)
        self.btn_yes.config(state=tk.DISABLED)
        self.btn_no.config(state=tk.DISABLED)
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(tk.END, "Diagnosa selesai. Klik 'Mulai Diagnosa' untuk memulai lagi.")
        self.question_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MalariaExpertGUI(root)
    root.mainloop()
import tkinter as tk
from tkinter import filedialog, ttk
import time
class TranslatorSystem():
    def __init__(self):
        pass

Translator = TranslatorSystem()
def main():
    def select_pdf():
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            file_label.config(text=f"📄 Dosya: {file_path.split('/')[-1]}")
            size_label.config(text="📦 Boyut: 12GB")
            words_label.config(text="📝 Kelime: 190")
            lang_label.config(text="🌍 Dil: A Dili")

    def translate_pdf():
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "✅ ÇEVRİLMİŞ PDF YAZILARI\n\n(Burada çeviri sonucu gösterilecek)")

    root = tk.Tk()
    root.title("PDF Çeviri Aracı")
    root.geometry("650x450")

    # Style
    style = ttk.Style(root)
    style.theme_use("clam")  # clam, alt, default, vista

    # Üst Menü Butonları
    menu_frame = ttk.Frame(root, padding=5)
    menu_frame.pack(fill="x")

    ttk.Button(menu_frame, text="📂 PDF SEÇ", command=select_pdf).pack(side="left", padx=5)
    ttk.Button(menu_frame, text="⚙️ AYARLAR").pack(side="left", padx=5)
    ttk.Button(menu_frame, text="💾 ÇEVİRİYİ PDF' AKTAR").pack(side="left", padx=5)

    # Bilgi Alanı
    info_frame = ttk.LabelFrame(root, text="📑 PDF Bilgileri", padding=10)
    info_frame.pack(fill="x", padx=10, pady=5)

    file_label = ttk.Label(info_frame, text="📄 Dosya: -")
    file_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")

    size_label = ttk.Label(info_frame, text="📦 Boyut: -")
    size_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")

    words_label = ttk.Label(info_frame, text="📝 Kelime: -")
    words_label.grid(row=0, column=1, padx=15, pady=2, sticky="w")

    lang_label = ttk.Label(info_frame, text="🌍 Dil: -")
    lang_label.grid(row=1, column=1, padx=15, pady=2, sticky="w")

    settings_label = ttk.Label(info_frame, text="⚙️ Ayarlar: Türkçe -> İngilizce")
    settings_label.grid(row=0, column=2, padx=10, pady=2, sticky="w")

    ttk.Button(info_frame, text="🚀 ÇEVİR", command=translate_pdf).grid(row=1, column=2, padx=10, pady=2)

    # Çeviri Çıktısı
    output_frame = ttk.LabelFrame(root, text="📖 Çeviri Sonucu", padding=10)
    output_frame.pack(fill="both", expand=True, padx=10, pady=5)

    output_text = tk.Text(output_frame, wrap="word", height=12, font=("Segoe UI", 10))
    output_text.pack(fill="both", expand=True)

    # Yükleme Çubuğu
    progress_frame = ttk.Frame(root, padding=5)
    progress_frame.pack(fill="x")


    progress = ttk.Progressbar(progress_frame, mode="determinate")
    progress.pack(fill="x", padx=5, pady=5)

    root.mainloop()




if __name__ == '__main__':
    main()
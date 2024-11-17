import tkinter as tk
from tkinter import messagebox


class NotatkiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zarządzanie Notatkami")

        self.notatki = []

        self.text_area = tk.Text(root, height=15, width=50)
        self.text_area.pack(pady=10)

        self.add_button = tk.Button(root, text="Dodaj Notatkę", command=self.dodaj_notatke)
        self.add_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Pokaż Notatki", command=self.pokaz_notatki)
        self.show_button.pack(pady=5)

        # Wyczyść notatki przycisk
        self.show_button = tk.Button(root, text="Wyczyść Notatki", command=self.wyczysc_notatki)
        self.show_button.pack(pady=5)

    def dodaj_notatke(self):
        notatka = self.text_area.get("1.0", tk.END).strip()
        if notatka:
            self.notatki.append(notatka)
            self.text_area.delete("1.0", tk.END)
            messagebox.showinfo("Sukces", "Notatka dodana!")
        else:
            messagebox.showwarning("Błąd", "Nie można dodać pustej notatki!")

    def pokaz_notatki(self):
        if not self.notatki:
            messagebox.showinfo("Notatki", "Brak zapisanych notatek.")
        else:
            notatki_text = "\n".join(self.notatki)
            messagebox.showinfo("Notatki", notatki_text)

    def wyczysc_notatki(self):
        if not self.notatki:
            messagebox.showinfo("Notatki", "Brak notatek do wyczyszczenia.")
        else:
            self.notatki.clear()
            messagebox.showinfo("Notatki", "Wyczyszczono notatki!!!!!!!!!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotatkiApp(root)
    root.mainloop()
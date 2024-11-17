import tkinter as tk
from tkinter import messagebox


class NotatkiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zarządzanie Notatkami")
        self.root.geometry("400x400")

        # Lista przechowująca notatki
        self.notatki = []

        # Pole tekstowe do wpisywania notatek
        self.text_area = tk.Text(self.root, height=10, width=40, wrap="word")
        self.text_area.pack(pady=10)

        # Przycisk: Dodaj notatkę
        self.add_button = tk.Button(
            self.root, text="Dodaj Notatkę", command=self.dodaj_notatke, bg="#4CAF50", fg="white"
        )
        self.add_button.pack(pady=5, ipadx=10)

        # Przycisk: Pokaż notatki
        self.show_button = tk.Button(
            self.root, text="Pokaż Notatki", command=self.pokaz_notatki, bg="#008CBA", fg="white"
        )
        self.show_button.pack(pady=5, ipadx=10)

        # Przycisk: Wyczyść notatki
        self.clear_button = tk.Button(
            self.root, text="Wyczyść Notatki", command=self.wyczysc_notatki, bg="#f44336", fg="white"
        )
        self.clear_button.pack(pady=5, ipadx=10)

    def dodaj_notatke(self):
        """Dodaje nową notatkę z pola tekstowego do listy notatek."""
        notatka = self.text_area.get("1.0", tk.END).strip()
        if not notatka:
            self._pokaz_komunikat("Błąd", "Nie można dodać pustej notatki!", typ="warning")
            return

        self.notatki.append(notatka)
        self.text_area.delete("1.0", tk.END)
        self._pokaz_komunikat("Sukces", "Notatka została dodana!")

    def pokaz_notatki(self):
        """Wyświetla wszystkie zapisane notatki w oknie dialogowym."""
        if not self.notatki:
            self._pokaz_komunikat("Informacja", "Brak zapisanych notatek.")
            return

        notatki_text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(self.notatki)])
        self._pokaz_komunikat("Twoje Notatki", notatki_text)

    def wyczysc_notatki(self):
        """Czyści listę notatek."""
        if not self.notatki:
            self._pokaz_komunikat("Informacja", "Brak notatek do wyczyszczenia.")
            return

        self.notatki.clear()
        self._pokaz_komunikat("Sukces", "Wszystkie notatki zostały wyczyszczone.")

    def _pokaz_komunikat(self, tytul, wiadomosc, typ="info"):
        """Pokazuje okno dialogowe z odpowiednim komunikatem."""
        if typ == "warning":
            messagebox.showwarning(tytul, wiadomosc)
        elif typ == "error":
            messagebox.showerror(tytul, wiadomosc)
        else:
            messagebox.showinfo(tytul, wiadomosc)


if __name__ == "__main__":
    root = tk.Tk()
    app = NotatkiApp(root)
    root.mainloop()

import pytest
from notatki_app import NotatkiApp
import tkinter as tk


@pytest.fixture
def app():
    root = tk.Tk()
    app_instance = NotatkiApp(root)
    yield app_instance
    root.destroy()


def test_dodaj_notatke(app):
    app.text_area.insert("1.0", "Testowa notatka")
    app.dodaj_notatke()
    assert len(app.notatki) == 1


def test_dodaj_pusta_notatke(app):
    app.dodaj_notatke()
    assert len(app.notatki) == 0



def test_dodaj_wiele_notatek(app):
    app.text_area.insert("1.0", "Notatka 1")
    app.dodaj_notatke()
    app.text_area.insert("1.0", "Notatka 2")
    app.dodaj_notatke()
    assert len(app.notatki) == 2


def test_pokaz_brak_notatek(app):
    app.pokaz_notatki()  # Sprawdzamy, czy nie generuje błędu


def test_notatka_zawiera_tekst(app):
    app.text_area.insert("1.0", "Test")
    app.dodaj_notatke()
    assert "Test" in app.notatki


def test_dodaj_wielokrotne_notatki(app):
    for i in range(10):
        app.text_area.insert("1.0", f"Notatka {i}")
        app.dodaj_notatke()
    assert len(app.notatki) == 10


def test_dodaj_notatki_kolejność(app):
    app.text_area.insert("1.0", "Notatka A")
    app.dodaj_notatke()
    app.text_area.insert("1.0", "Notatka B")
    app.dodaj_notatke()
    assert app.notatki[0] == "Notatka A"
    assert app.notatki[1] == "Notatka B"


def test_notatki_są_unikalne(app):
    app.text_area.insert("1.0", "Notatka unikalna")
    app.dodaj_notatke()
    app.text_area.insert("1.0", "Notatka unikalna")
    app.dodaj_notatke()
    assert len(app.notatki) == 2


def test_dodawanie_notatek_i_wyczyszczenie(app):
    app.text_area.insert("1.0", "Notatka do wyczyszczenia")
    app.dodaj_notatke()
    app.text_area.delete("1.0", tk.END)
    assert len(app.notatki) == 1


def test_dodaj_notatke_z_roznych_zrodel(app):
    for i in range(3):
        app.text_area.insert("1.0", f"Notatka {i}")
        app.dodaj_notatke()
    assert app.notatki[-1] == "Notatka 2"  # Ostatnia powinna być "Notatka 2"


def test_brak_notatek_w_aplikacji(app):
    assert app.notatki == []


def test_dodaj_notatke_z_roznych_typow(app):
    app.text_area.insert("1.0", "Notatka tekstowa")
    app.dodaj_notatke()

    app.text_area.insert("1.0", "12345")
    app.dodaj_notatke()

    app.text_area.insert("1.0", "!@#$%^&*()")
    app.dodaj_notatke()

    assert len(app.notatki) == 3


def test_dodawanie_notatek_i_wyczyszczenie(app):
    app.text_area.insert("1.0", "Notatka do wyczyszczenia")
    app.dodaj_notatke()
    app.wyczysc_notatki()
    assert len(app.notatki) == 0


def test_dodawanie_pustych_notatek_wielokrotnie(app):
    for _ in range(5):
        app.dodaj_notatke()
    app.wyczysc_notatki()
    assert len(app.notatki) == 0


def test_ustawienie_notatki_i_wyczyszczenie(app):
    app.text_area.insert("1.0", "Notatka do ustawienia")
    app.dodaj_notatke()
    app.wyczysc_notatki()
    assert app.text_area.get("1.0", tk.END).strip() == ""
    assert len(app.notatki) == 0

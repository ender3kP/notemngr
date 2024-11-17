import pytest
from unittest.mock import MagicMock
from notatki_app import NotatkiApp


@pytest.fixture
def app(monkeypatch):
    # Mockowanie tkinter.Tk
    mock_root = MagicMock()
    monkeypatch.setattr("tkinter.Tk", lambda: mock_root)
    app_instance = NotatkiApp(mock_root)
    return app_instance


def test_dodaj_notatke(app):
    app.text_area.insert = MagicMock()
    app.text_area.get = MagicMock(return_value="Testowa notatka")
    app.dodaj_notatke()
    assert len(app.notatki) == 1


def test_dodaj_pusta_notatke(app):
    app.text_area.get = MagicMock(return_value="")
    app.dodaj_notatke()
    assert len(app.notatki) == 0


def test_dodaj_wiele_notatek(app):
    for i in range(3):
        app.text_area.get = MagicMock(return_value=f"Notatka {i}")
        app.dodaj_notatke()
    assert len(app.notatki) == 3
    assert app.notatki == ["Notatka 0", "Notatka 1", "Notatka 2"]


def test_pokaz_brak_notatek(app):
    app.notatki = []
    app.pokaz_notatki = MagicMock()
    app.pokaz_notatki()
    app.pokaz_notatki.assert_called_once()


def test_notatka_zawiera_tekst(app):
    app.text_area.get = MagicMock(return_value="Test")
    app.dodaj_notatke()
    assert "Test" in app.notatki


def test_dodaj_notatki_kolejność(app):
    app.text_area.get = MagicMock(side_effect=["Notatka A", "Notatka B"])
    app.dodaj_notatke()
    app.dodaj_notatke()
    assert app.notatki == ["Notatka A", "Notatka B"]


def test_dodawanie_i_wyczyszczenie_notatek(app):
    app.text_area.get = MagicMock(return_value="Notatka do usunięcia")
    app.dodaj_notatke()
    app.wyczysc_notatki()
    assert len(app.notatki) == 0


def test_notatki_unikalne(app):
    app.text_area.get = MagicMock(return_value="Powtarzająca się notatka")
    app.dodaj_notatke()
    app.dodaj_notatke()
    assert len(app.notatki) == 2  # Każda notatka jest traktowana osobno


def test_wyczyszczenie_tekstowego_pola(app):
    app.text_area.get = MagicMock(return_value="Notatka")
    app.dodaj_notatke()
    app.text_area.delete = MagicMock()
    app.wyczysc_notatki()
    app.text_area.delete.assert_called_once_with("1.0", "end")
    assert len(app.notatki) == 0

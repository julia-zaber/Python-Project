# Skrypt JWST - zdjęcia 

Ten skrypt Pythona jest przeznaczony do analizy i wizualizacji danych astronomicznych z wykorzystaniem bibliotek Astropy i JWST (James Webb Space Telescope).
## Wymagane Biblioteki

- `os`
- `shutil`
- `inspect`
- `numpy`
- `scipy.signal`
- `astropy`
- `jwst`
- `matplotlib`

## Działanie kodu 

### Funkcje Pomocnicze

- `create_image`: Funkcja generuje obraz w formie czarno białej 
- `create_slit_image`: Funkcja generuje obraz w formie kolorowej  
## Pobieranie i Wczytywanie Danych

Skrypt korzysta z przykładowych plików danych astronomicznych dostępnych pod podanymi adresami URL.

### Analiza Danych

- Skrypt wczytuje dane astronomiczne z plików i generuje obrazy.
- Wyświetla informacje na temat struktury

### Wizualizacja Danych

- Dane astronomiczne są wizualizowane w formie obrazów za pomocą funkcji `create_image` i `create_slit_image`.

## Uruchamianie Skryptu

1. Pobierz repozytorium
2. Upewnij się, że pobrano wszystkie potrzebne biblioteki 


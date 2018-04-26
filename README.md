# EskaStreamGrabber
Skrypt do pobierania linków do streamów radia Eska Rock i innych, wraz z aktualnymi tokenami. Dzięki temu możesz uruchomić te radia używając własnych aplikacji. Domyślnie Radio Eska pozwala na streamowanie stacji tylko i wyłącznie na własnych dedykowanych aplikacjach mobilnych i poprzez przeglądarke internetową na ich stronie web.
Skrypt napisałem dla własnych celów (uruchamianie Eski przy pomocy jednego klawisza na pilocie), ale zapraszam innych do używania go :)
 
 ## Funkcje:
- pobiera aktualny stream link i zapisuje w uniwersalnym pliku m3u, umozliwiając integrację skryptu z kazdym odtwarzaczem i innymi skryptami,
- **integracja z odtwarzaczem multimediów Kodi,**
- skrypt łatwy w edytowaniu, bardzo łatwo można dodać inne ulubione stacje Eska.

## Użytkowanie skryptu:
Skrypt wymaga zainstalowanego Pythona 2.7 oraz podania jednego argumentu z wybraną stacją. 
- Domyślne: `EskaStreamGrabber.py -nazwa_stacji`. Zostanie stworzony plik nazwa_stacji.m3u
- Poprzez Kodi: `runscript(/lokacja/skryptu/EskaStreamGrabber.py, -nazwa_stacji)`, zostanie stworzony plik nazwa_stacji.m3u a sama stacja zostanie odtworzona z wygenerowanego pliku.

## Wspierane Stacje:
- Eska ROCK
- Eska ROCK Kultowa Godzina
- Eska ROCK Hot Rock
- Eska ROCK Alternative
- Eska ROCK Polska

# KCK RSS Reader - GUI

<div style="text-align: center;">Czytnik źródeł RSS</div>

**Autor**: Adam Lisowski, *grupa PS5, 105602*

## Opis projektu

Aplikacja "KCK RSS Reader" jest prostą aplikacją służącą do przeglądania i czytania wiadomości z różnych źródeł zdefiniowanych przez użytkownika. Przez wyeliminowanie reklam i niepotrzebnych elementów na stronach, użytkownik może zapoznać się z wiadomościami ze swoich ulubionych źródeł bez rozproszeń.

## Funkcjonalności aplikacji

- Wczytywanie wiadomości z wybranych źródeł
- Lista wiadomości
- Wyświetlanie tekstu wiadomości bez reklam
- Sortowanie wiadomości z różnych źródeł według daty
- Możliwość wyboru czcionki i rozmiaru tekstu zgodnie z preferencjami użytkownika

## Instrukcja instalacji

Aby zainstalować program, należy najpierw zainstalować wymagane biblioteki:

```shell script
pip install py-cui wx #lub
pip3 install py-cui wx
```

Następnie należy go uruchomić w katalogu komendą:

```shell script
python main.py #lub
python3 main.py
```

## Instrukcja konfiguracji

W pliku `sources.txt` znajdują się źródła RSS. W każdej linii znajduje się osobne źródło w postaci linku XML. Dodawanie i usuwanie listy źródeł odbywa się poprzed edycję tego pliku.

## Instrukcja użytkownika

Po uruchomieniu programu wczytywana jest lista źródeł artykułów i z każdego są wczytywane artykuły. Są one następnie sortowane według daty publikacji.

Po wczytaniu wiadomości uruchomiony zostaje interfejs graficzny z jedną kolumną. Zawiera ona listę wczytanych wiadomości, posortowanych zgodnie z datą ich publikacji. Po liście nawigować można przy pomocy rolki myszki lub klawiszy góra/dół na klawiaturze.

W oknie głównym aplikacji, w menu "Fonts" można wybrać czcionkę i jej rozmiar wyświetlania w oknie artykułu. Po rozwinięciu tego menu uzyskujemy dostęp do 6 różnych czcionek i 3 dostępnych wielkości. Zmiana odbywa się poprzez kliknięcie wybranej opcji.

Aby wybrać artykuł, należy kliknąć dwukrotnie lewym przyciskiem myszy na danym tytule lub też wcisnąć klawisz Enter na klawiaturze.. Ukaże się wtedy osobne okienko z artykułem. Jeżeli artykuł nie mieści się na ekranie, można go przewijać używając do tego rolki myszy lub klawiszy góra/dół na klawiaturze.

Zamknięcie programu odbywa się poprzez zamknięcie głównego okna z listą przy użyciu albo systemowej ikonki X w rogu ekranu, lub poprzed wybór opcji `Exit` w menu aplikacji dostępnym w lewym górnym rogu. W tymże menu można również zobaczyć krótki opis programu. 

## Wnioski

Stworzenie interfejsu graficznego przy użyciu odpowiednich bibliotek nie jest zadaniem trudnym w języku Python, chociaż w porównaniu do wcześniej stworzonego interfejsu tekstowego jest on trudniejszy do wykonania, zaprojektowania i wymaga większego nakładu pracy

Python pozwala na bardzo łatwe tworzenie aplikacji z interfejsem graficznym dzięki obecności różnych bibliotek - od bardzo rozbudowanego Qt, poprzez natywnie wspierany Tkinter, użyty w projekcie WxPython (który jest wrapperem na WxWidgets), PySimpleGUI, Kivy, PySide2 (pochodna Qt), PyGUI, PyForms czy Libavg. Możliwości każdej z bibliotek są bardzo duże i każdy programista mógłby wybrać co mu bardziej odpowiada. Co więcej, duża część z nich (jak Qt, WxPython czy Kivy) pozwalają na pisanie multiplatformowych interfejsów graficznych z użyciem tego samego kodu na inne systemy operacyjne.

## Samoocena

Uważam, że program "**KCK RSS Reader**" jest bardzo prostym programem, który spełnia swoje główne założenie - wyświetlanie wiadomości ze źródeł RSS pozbawionych reklam i innych rozpraszających elementów ze stron. Interfejs jest czytelny, potrafi zaadaptować się do różnych wielkości terminala systemowego i jest też stosunkowo prosty w obsłudze.


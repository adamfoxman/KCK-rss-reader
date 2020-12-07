# KCK RSS Reader

<div style="text-align: center;">Czytnik źródeł RSS</div>

## Opis projektu

Aplikacja "KCK RSS Reader" jest prostą aplikacją służącą do przeglądania i czytania wiadomości z różnych źródeł zdefiniowanych przez użytkownika. Przez wyeliminowanie reklam i niepotrzebnych elementów na stronach, użytkownik może zapoznać się z wiadomościami ze swoich ulubionych źródeł bez rozproszeń.

## Funkcjonalności aplikacji

- Wczytywanie wiadomości z wybranych źródeł
- Lista wiadomości
- Wyświetlanie tekstu wiadomości bez reklam
- Sortowanie wiadomości z różnych źródeł według daty

## Instrukcja instalacji

Aby zainstalować program, należy najpierw zainstalować wymagane biblioteki:

```shell script
pip install py-cui feedparser newspaper3k #lub
pip3 install py-cui feedparser newspaper3k
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

Po wczytaniu wiadomości uruchomiony zostaje interfejs tekstowy z dwoma kolumnami. W lewej kolumnie znajduje się lista tytułów wczytanych artykułów, a po prawej - pusta przestrzeń na wybrany artykuł.

Aby wybrać artykuł, należy najpierw wejść w tryb wyboru artykułu wciskając `Enter`. Artykuł można wybrać strzałkami góra/dół lub klikając myszką. Aby otworzyć artykuł, należy ponownie wcisnąć `Enter`. Artykuł pojawi się wtedy w prawym panelu.

Jeżeli artykuł nie mieści się na ekranie, można go przewijać przechodząc do trybu czytania artykułu - najpierw należy wyjść z listy artykułów klawiszem `Esc`, wybrać strzałkami lub myszką artykuł i wcisnąć `Enter`. Przewijanie odbywa się klawiszami góra/dół. Podobnie wygląda wychodzenie z trybu czytania artykułu i przejście do trybu wyboru artykułu.

Zamknięcie programu odbywa się klawiszem `q`.

Instrukcja użytkowania programu znajduje się zawsze na dole okna - widać tam możliwe akcje do wykonania.
# Komunikacja
Komunikacja z tablicami odbywa za pośrednictwem standardu RS-485. Szybkość transmisji należy ustawić na 9600 bps. Numer wyświetlacza ustawiany jest DIP switchami będącymi w środku wyświetlacza, w większości wyświetlaczy są łatwo dostępne po zdjęciu gumowej zaślepki.<br>
# Format wiadomości
Wiadomość składa się z: 16  bajtów sterujących, określających sposób wyświetlania tekstu, ciągu bajtów zawierających wyświetlany tekst, sumy kontrolnej obliczanej jako suma wszystkich bajtów modulo 256. Wszystkie wartości, zarówno bajty sterujące, tekst, jak i suma
kontrolna, są kodowane jako hex w standardzie CP852. Cała wiadomość znajduje się pomiędzy bajtami `02` i `03`.

Znaczenie poszczególnych bajtów sterujących:
1. Numer wyświetlacza
2. Number wyświetlacza
3. Długość wiadomości
4. Długość wiadomości
5. Separator
6. (nie wiadomo)
7. Wybór linijki wyświetlania pierwszej lub drugiej - 0 lub 1 (czyli w CP852 30 lub 31)
8. Wybór trybu położenia tekstu (0 - do lewej, 1 - do środka, 2 - do prawej)(czyli w CP852 30, 31 lub 32)
9. Separator
10. Wybór fontu (fonty opisane są w dalszej części pliku)
11. Pozycja tekstu idąc od lewej - razy 16 pikseli
12. Pozycja tekstu idąc o lewej - razy 1 piksel
13. Granica ograniczająca tekst od prawej - razy 16 pikseli
14. Granica ograniczająca tekst od prawej - razy 1 piksel
15. Ilość przewinięć tekstu - razy 16
16. Ilość przewinięć tekstu - razy 1

Specyficzne właściwości:
- Chcąc wyświetlić dwie rzeczy na raz w dwóch linijkach lub obok siebie, wysyłając dwie wiadomości jedna po sobie powinno się zachować drobny odstęp czasowy. Dla krótszych wiadomości wystarczy 0.05 sekundy, dla dłuższych bywa to za mało i potrzeba 0.1 sekundy (wartości orientacyjne, można próbować z mniejszymi).
- Wartość numeru wyświetlacza w wiadomości jest uzyskiwana w specyficzny sposób opisany [tutaj](https://github.com/HiszpanInk/rg-screens-things/issues/1)
- Wartość długości tekstu to liczba znaków +12.
- Wyświetlając tekst w dwóch linijkach (fonty od 2 w górę) należy wybrać linijkę pierwszą (0).
- Chcąc ustawić tekst na stałe należy bajty 15 i 16 ustawić na 0.
- Duże tablice (pseudoautobusowe) z uwagi na wersję oprogramowania nie posiadają możliwości przewijania tekstu zajmującego dwie linie.

Rozdzielczości tablic:
- Mała/Mała ze znakiem WC: 96x16
- Duża: 88x16
- Zewnętrzne: 96x32 lub 120x32

Przykład 1:
```
#   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
02 35 33 36 35 38 30 30 31 37 32 30 30 36 30 30 31 98 6D 69 65 73 7A 6E 79 20 62 61 72 64 7A 6F 20 62 61 72 64 7A 6F 20 64 88 75 67 69 20 74 65 6B 73 74 20 74 79 70 75 20 6C 6F 72 65 6D 20 69 70 73 75 6D 20 64 6F 6C 6F 72 20 73 69 74 20 61 6D 65 74 20 63 7A 79 20 6C 65 63 69 20 7A 20 6E 61 6D 69 20 70 69 6C 6F 74 3F 43 32 03
```
Wiadomość wyświetlona zostanie na wyświetlaczu o numerze 20 (35 33), wiadomość ma długość (36 35 czyli 0x65 czyli 101-12=89) 89 znaków, wyświetlana będzie na pierwszej linijce (30), będzie wycentrowana (31), użyty zostanie font nr 5 (34), wiadomość będzie wyświetlana od lewej krawędzi tablicy (30 30, czyli 0px), aż do prawej krawędzi (36 30, czyli 96 px, jest to szerokość tablic małych i części zewnętrznych), i tekst zostanie przescrollowany jeden raz (30 31). Wyświetlony zostanie tekst "śmieszny bardzo bardzo długi tekst typu lorem ipsum dolor sit amet czy leci z nami pilot?", a obliczona suma kontrolna wynosi 0xC2.

Przykład 2:
```
#   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
02 35 33 30 46 38 30 30 30 37 34 35 30 36 30 30 30 32 37 31 44 36 03
```
Wiadomość wyświetlona zostanie na wyświetlaczu o numerze 20 (35 33), wiadomość ma długość (30 46 czyli 0x0F czyli 15-12=3) 3 znaki, wyświetlana będzie na pierwszej linijce (30), będzie wyrównany do lewej (30), użyty zostanie font nr 3 (34), wiadomość będzie wyświetlana 80px od lewej krawędzi tablicy (35 30, czyli 0x50 czyli 80), do prawej krawędzi (36 30, czyli 96 px, jest to szerokość tablic małych i części zewnętrznych), i tekst zostanie ustawiony na stałe (30 30). Wyświetlane zostanie "271" i obliczona suma kontrolna wynosi 0xD6.
# Communication
Communication with the displays uses the RS-485 standard. The transmission speed must be set to 9600 bps.
The display number is configured using  DIP switches located inside the display, in most models they are easily accessible after removing a rubber cap.<br>
# Message format
Message consists of 16 bytes which control which set how the message is displayed, bytes containg text to display and control sum from the whole message (calculated by summing the whole message and then taking a remainder from division of the sum by 256). Control values are encoded as hex values in CP852 (including control sum), the text is also encoded in CP852. Whole of message is between of bytes '02' and '03'. Meaning of control bytes:
1.  Display number
2.  Display number
3.  Message length
4.  Message length
5.  Separator
6.  (unknown)
7.  Line selection (0 - first line, 1 - second line; CP852: 30 or 31)
8.  Text alignment (0 -- left, 1 - center, 2 - right; CP852: 30, 31,
    32)
9.  Separator
10. Font selection (fonts described later)
11. Text position from the left - ×16 pixels
12. Text position from the left - ×1 pixel
13. Right text boundary - ×16 pixels
14. Right text boundary - ×1 pixel
15. Number of scroll repetitions - ×16
16. Number of scroll repetitions - ×1

Specific details:
-   When displaying two messages at the same time (two lines or
    side-by-side), a short delay is needed between transmissions. Typically 0.05 s works for short messages, while 0.1 s maybe needed for longer ones.
-   Display number is calculated in a specific way described [here](https://github.com/HiszpanInk/rg-screens-things/issues/1).
-   Text length is equal to the number of characters plus 12.
-   For two-line fonts (3--7), the selected line must be the first one(30).
-   To display text permanently (without scrolling), set bytes 15 and 16 to 0.
-   Large displays (pseudo-bus type) cannot scroll two-line text due to older firmware.

Displays resolution:
- Small/small with WC sign: 96x16
- Big: 88x16
- Outside: 96x32 lub 120x32

Example 1:
```
#   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
02 35 33 36 35 38 30 30 31 37 32 30 30 36 30 30 31 98 6D 69 65 73 7A 6E 79 20 62 61 72 64 7A 6F 20 62 61 72 64 7A 6F 20 64 88 75 67 69 20 74 65 6B 73 74 20 74 79 70 75 20 6C 6F 72 65 6D 20 69 70 73 75 6D 20 64 6F 6C 6F 72 20 73 69 74 20 61 6D 65 74 20 63 7A 79 20 6C 65 63 69 20 7A 20 6E 61 6D 69 20 70 69 6C 6F 74 3F 43 32 03
```
Message will be shown on display number 20 (35 33), message length is (36 35 meaning 0x65 meaning 101-12=89) is 89 characters, it will be shown on the first line (30), text will be aligned to the center (31), font number 5 will be used (34), message will be shown from the left border of the display (30 30, meaning 0px), to the right border of the display (36 30 meaning 96px which is width of small and some outside displays), text will be scroll once (30 31). Displayed text will be "śmieszny bardzo bardzo długi tekst typu lorem ipsum dolor sit amet czy leci z nami pilot?" and calculated control sum equals 0xC2.

Example 2:
```
#   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
02 35 33 30 46 38 30 30 30 37 34 35 30 36 30 30 30 32 37 31 44 36 03
```
Message will be shown on display number 20 (35 33), message length is (30 46 meaning 0x0F meaning 15-12=3) is 3 characters, it will be shown on the first line (30), text will be aligned to the left (30), font number 3 will be used (34), message will be shown 80 px from the left border of the display (35 30 meaning 0x50 meaning 80px), to the right border of the display (36 30 meaning 96px), and text will be set permanently and not scrolled (30 30). Displayed text will be "271" and calculated control sum equals 0xD6.

# Fonty
## Font 1 (wartość pozycji 30)
Font na jedną linijkę, małe litery w wiadomości to zmniejszone wielkie
![](/images/font-1.png "Font 1")
## Font 2 (wartość pozycji 31)
Font na jedną linijkę, wielkie litery, cyfry, znaki specjalne pogrubione. Małe litery wyświetlane jako małe i ale na całą wysokość linijki
![](/images/font-2.png "Font 2")
## Font 3 (wartość pozycji 32)
Font na dwie linijki, wielkie litery, cyfry, znaki pogrubione, małe litery cienkie
![](/images/font-3.png "Font 3")
## Font 4 (wartość pozycji 33)
Font na dwie linijki, dwie linijki na środku, tylko do cyfr (znaki wychodzą jako 0), wyświetlane jako cienkie
![](/images/font-4.png "Font 4")
## Font 5 (wartość pozycji 34)
Font na dwie linijki, dwie linijki na środku, tylko do cyfr, wyświetlane na większą wysokość
![](/images/font-5.png "Font 5")
## Font 6 (wartość pozycji 35)
Font na dwie linijki, pogrubione wielkie i małe, wyższy od fontu 3
![](/images/font-6.png "Font 6")
## Font 7 (wartość pozycji 36)
Font na dwie linijki, pogrubione wielkie i małe, na całą wysokość tablicy
![](/images/font-7.png "Font 7")

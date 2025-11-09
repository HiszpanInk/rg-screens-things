# Repozytorium z plikami dot. sterowników R&G

Opis zawartości:
- Folder ze-sterownika - dumpy komunikacji ze sterownika do wyświetlaczy wraz z programem w Pythonie do dekodowania na tekst (z pliku input.txt do output.txt, po prostu odkodowuje wszystko jako tekst CP852)
- Folder przydatne - wszelkie notatki i pomoce jakie zostały stworzone w trakcie kombinowania z wyświetlaczami
- wyslij_tekst.py - prosty program do wysyłania tekstu do wyświetlacza, automatycznie oblicza długość tekstu do pewnej długości, sumę kontrolną oraz konwertuje tekst na CP852 i wysyła, ręcznie należy zmieniać pozostałe wartości (są one jednak opisane) w tym szczególnie port do komunikacji

Content description:
- Folder ze-sterownika - dumps of communcation from controller to the screens with a Python program to decode it to text (it just takes hex from file input.txt, decodes it as CP852 and puts it into output.txt)
- Folder przydatne - any notes and helps which were created during tinkering with the displays
- wyslij_tekst.py - simple Python program to send text to the screens, it automatically calculates text length value (to the certain point), control sum, converts text into CP852 and send it, the other values have to be changed manually (they are described in a comment in Polish), including COM port
---
Podziękowania dla <b>Mitsumiego✨</b> za Jego pracę i wkład w analizę wiadomości i udostępnienie swoich notatek które są umieszczone w folderze przydatne, podziękowania dla <b>LirekPL</b> za Jego pracę przy analizowaniu wiadomości i dostarczenie wyświetlaczy oraz sterownika <br><br>
Thanks to <b>Mitsumi✨</b> for His work in analysing the messages and providing scans of His notes that are included in Przydatne folder, thanks to <b>LirekPL</b> for His work in analysing the messages and providing the screens and the controller

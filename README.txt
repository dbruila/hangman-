	Celem tej gry jest poszerzenie słownictwa angielskich słów. W tej grze musimy 
odgadnąć słowo. Wszystkie litery słowa są zamienione na podkreślenia. 
Dzięki takiej układance możemy nauczyć się nowych słów, a także zapamiętaćich pisownię.

Wykaz realizowanych zdań:
	1. Tworzenie okna dialogowego Tkinter;
	2. Twozenie przyciskow (play, rules, edit word’s file);
	3. Tworzenie listy słów (funkcje do odczytania słów z pliku i wybierania losowego
	słowa);
	4. Wyświetlenie słowa na ekranie;
	5. Tworzenie listy nieznanych liter (zamieniamy je na podkreślenia);
	6. Tworzenie przycisków z literami;
	7. Sprawdzenie poprawność odpowiedzi;
	8. Rysowanie obrazku;
	9. Zapis/usuwania/edycja pliku ze słowami;

Opis zrealizowanych funkcji:
	1. def newGame() – wybiera randomowe słowo z pliku, zamienia litery na
	podkreślenia, wyświetla przyciski z literami oraz przycisk do rozpoczęcia
	nowej gry;
	2. def guess() – po naciśnięciu na przycisk z litera blokuje go oraz sprawdza czy
	są taka litera w słowie oraz zamienia podkreślenia na literę lub rysuje cześć
	malunku, jeżeli nie ma takiej litery w słowie, wyświetla komunikat o
	wygraniu/przegraniu;
	3. def one(), def two(), def three(), def four(), def five(), def six(), def seven(), def
	eight() – funkcji do malowania częsci rysunku;
	4. def rules() – tworzy nowe okno i wyświetla zasady gry;
	5. def start() – wyczyszcza okno tkinter;
	6. def restart_program() – ponownie uruchamia grę;
	7. def newWord() – tworzy okno z komponentami do zmiany słów w pliku;
	8. def openF() – otworzy plik i wyświetla słowa;
	9. def saveF() – zapisuje zmiany w pliku ze słowami;
	10. def saveChange() – pyta użytkownika czy chce zapisać zmiany w plikie ze
	słowami;
Opis sposobu instalacji
	1. Należy ściągnąć wszyskie pliki z hangman-python;
	2. Dalej wystarczy uruchomić plik game.py
+++
date = "2015-01-01T00:00:00+01:00"
permalink = "/Projekt_nowego_silnika_forum/"
title = "Projekt nowego silnika forum"
kategorie = [ "serwis",]

+++

*To jest [moja](/atopedia/Wikipedysta:Wahwah "wikilink") strona robocza*

Lista funkcji
-------------

### Zgodność z phpBB

*Zgodność z phpBB. Zgodność z phpBB. Zgodność z phpBB.*

-   bbcode (formatowanie, linki, obrazki)
-   fora prywatne (grupy użytkowników, uprawnienia), lub alternatywnie szepty (jak w Vanilli)
-   moderacja, czyli:
    -   edycja postów
    -   dzielenie wątków
    -   łączenie wątków
-   zakładanie kont
    -   wpisanie literek z obrazka przy zakładaniu konta (Czy jesteś człowiekiem? Przepraszamy, ale musimy to iedzieć.)
    -   bez aktywacji strona użytkownika nie pokazuje się (anty-spam)
    -   odebranie maila z aktywacją, kliknięcie na link z maila
-   zmiana e-maila
    -   aktywacja e-mailem jak przy zakładaniu konta
-   avatary 80×80
-   cytowanie
-   stare linki mają cały czas działać

### Funkcje, których nie ma w phpBB

-   Prosta i skuteczna wyszukiwarka
-   Tagowanie wątków, każdy użytkownik taguje “sobie”, czyli niezależnie od innych użytkowników.
-   Rankowanie postów: przy każdym poście jest ikona "dobry post" i "zły post" z ew. określeniem, dlaczego zły: nie na temat, kłótliwy, nieprawda, lub dlaczego dobry: ciekawy, dogłębny, śmieszny
-   textile dla chętnych (bbcode domyślne)
-   Poprawka listy nieczytanych postów. W phpBB resetuje się przy każdej sesji. Tego resetowania ma nie być. Post jest przeczytany wtedy, kiedy jest przeczytany. Może raczej wątek, a nie post. Całość wymaga trzymania w bazie danych wiersza w tabeli dla każdej kombinacji wątek-użytkownik.

### Mechanizmy socjalne

-   Posty które będą zbierać ujemne punkty będą domyślnie zwinięte i na szaro
-   Najciekawsze nowe wątki (czyli wysoko oceniane). Oceniane są posty. Można więc brać sumę z tych postów, które są oceniane na plus. Posty na minus można ignorować, bo i tak są zwinięte.
-   Chmura tagów (dyskutujemy o), pewnie z jakiegoś okresu, np. ostatnie 30 dani

Dodatkowe widoki:

-   Moje wątki
    -   Założone przez użytkownika
    -   W których użytkownik zabrał głos
    -   Które sobie zaznaczył (gwiazdka?)
-   Nieprzeczytane posty (tak naprawdę, wątki)

Open Source Web Design
----------------------

Przeglądając dostępne szablony...

-   Business, portal
    -   [Internet Services](http://www.oswd.org/design/preview/id/2876)
    -   [Internet Market](http://www.oswd.org/design/preview/id/2860)
-   [Mountains](http://www.oswd.org/design/preview/id/2828)
-   [Andreas02](http://www.oswd.org/design/preview/id/2204/)
-   Sinorca 2.0, ugly colors, but I like the layout [1](http://www.oswd.org/design/preview/id/1165/) [2](http://www.oswd.org/design/preview/id/1794)
-   [Calypso](http://www.oswd.org/design/preview/id/1705)
-   Trendy? [Revival.2](http://www.oswd.org/design/preview/id/2993/)
-   wow, cliean, simple [Blue Haze](http://www.oswd.org/design/preview/id/1152/)
-   clean, simple, but narrow [Deliciously Blue](http://www.oswd.org/design/preview/id/2634)
-   Another quite narrow [3](http://www.oswd.org/design/preview/id/2552)
-   [Plain 2.0](http://www.oswd.org/design/preview/id/2434)
-   ignore the trends [andreas08](http://www.oswd.org/design/preview/id/2427)
-   [Terje Winter](http://www.oswd.org/design/preview/id/2855)
-   simple, beautiful: [Leaves 1.0](http://www.oswd.org/design/preview/id/2429)

+++
author = "Wahwah"
categories = ["Forum", "Portal", "Techniczne"]
date = "2006-12-04"
layout = "post"
title = "Ewolucja, nie rewolucja"
url = "/2006/12/04/ewolucja-nie-rewolucja/"

+++

Jakiś czas temu rozważałem napisanie własnego silnika forum, w podejściu _rewolucyjnym_. Gdybym był młodszy, pewnie bym tak zrobił. Przesiedziałbym kilka tygodni dniami i nocami, implementując całe forum od zera, łącznie z zakładaniem kont, administracją, i całą masą rzeczy, która jest już zrobiona i działa. Na koniec wyrzuciłbym całe istniejące forum, na to miejsce wstawił nową wersję, wzbudzając zachwyt u niektórych użytkowników i popłoch u innych.

<!--more-->Lat mi jednak wciąż przybywa. Robię się leniwy. Nie mam już ochoty na kilka tygodni pracy dniami i nocami. Dlatego zamiast pisząc całkowicie nowy silnik, będę powoli dobudowywał nowe części naszego serwisu, nie psując istniejących.

Zamiast budować wszystko od nowa, _„bo tym razem zrobię to porządnie”_, próbując stworzyć „teorię wszystkiego”, rozwiązuję konkretne problemy.

Na pierwszy ogień poszli [polecani lekarze][1]. Wszyscy ci, którzy na forum prosili o to, aby im kogoś polecić, mogą teraz wygodnie przeszukać naszą bazę lekarzy. Aplikacja była dość prosta, w miarę gładko udało mi się zrobić tak żeby można było się logować przy pomocy loginów i haseł z forum. Odpaliłem całość w kilka dni. Duża satysfakcja.

Następną aplikacją będą ceny leków. Co te apteki potrafią wyprawiać z cenami Protopiku, to w głowie się nie mieści. Mamy co prawda [stronę na której można sobie obejrzeć ceny Protopiku][2] w różnych aptekach, ale jest ona dość niewygodna w użyciu. Ani nie da się jej wygodnie czytać, ani wygodnie edytować. Dlatego następny fragment aplikacji to będzą właśnie apteki i ceny Protopiku, łatwe w przeglądaniu i łatwe we wprowadzaniu.

To nie koniec problemów. Kolejna rzecz to dziwna niechęć Google&#8217;a do indeksowania forum. Atopedia jest pięknie zaindeksowana i pokazuje się bardzo wysoko w wynikach. A forum nie. Nie wiem dlaczego tak jest. Brzydkie linki ze znakami zapytania? A może ogólna niechęć do for? Co by to nie było, fakt faktem: forum zawiera dużo treści, a Google wcale nie chce tej treści przyswajać.

I tutaj właśnie jest kolejny pomysł. Mogę dość szybko napisać _przeglądarkę_ forum, czyli fragment strony, która będzie służyła tylko i wyłącznie do _czytania_ forum. Strona ta będzie pobierała treść bezpośrednio z forum, czyli tu i tam będą dokładnie te same posty, dokładnie tam samo zorganizowane. Różnica będzie polegała na tym, że przeglądarka będzie przygotowana w sposób przyjazny dla Google. Wtedy jest szansa, że nasza ulubiona wyszukiwarka zaindeksuje wreszcie wszystko to co napisaliśmy na forum i będzie się to pojawiać w wynikach wyszukiwania.

Patrząc teraz na swoje przemyślenia, dochodzę do wniosku że wybór jest oczywisty. Użytkownicy będą mieli cały czas to co mieli dotychczas, na samym forum nic się nie zmieni. Różnica będzie taka, że jeżeli będą czegoś potrzebowali, np. znaleźć lekarza lub tanią aptekę, będą mieli przygotowane w tym celu specjalne miejsca. Ja z kolei mogę dodawać powoli fragmenty funkcjonalności, nie modyfikując niczego, do czego są przyzwyczajeni nasi użytkownicy.

Ewolucja to metoda łagodna zarówno dla użytkowników jak i dla mnie.

 [1]: http://www.atopowe.pl/lekarze/
 [2]: http://www.atopowe-zapalenie.pl/atopedia/Gdzie_kupi%C4%87_Protopic
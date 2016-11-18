+++
author = "Wahwah"
kategorie = ["Portal", "Techniczne"]
date = "2008-11-28"
layout = "post"
title = "Linki do Centralnego Rejestru Lekarzy"
url = "/2008/11/28/linki-do-centralnego-rejestru-lekarzy/"

+++

Niedawno uruchomiłem logowanie do [działu z lekarzami][1]. Logowanie nie działało od czasu aktualizacji naszego forum z phpBB 2 na phpBB 3. Nowsza wersja phpBB inaczej zapamiętuje hasła, i moduł służący do sprawdzania haseł po prostu przestał pasować. Aktualizacja wymagała trochę pracy, m.in. przepisania kawałka kodu z PHP do Pythona. Przy okazji wydzieliłem z naszego kodu fragment który może służyć do bardziej ogólnych zastosowań i nazwałem go [django-phpbb][2].

Wczoraj dodałem nową funkcję do działu z lekarzami: skrót do sprawdzania danych lekarza w Centralnym Rejestrze Lekarzy.

<!--more-->

Teraz, kiedy wchodzi się na stronę z informacjami o konkretnym lekarzu, widać przycisk, który odeśle nas do Rejestru. Najpierw dostajemy do zaakceptowania warunki korzystania, i kod do wpisania (kod ma utrudnić maszynowe wyciąganie danych z Rejestru).

Warunki korzystania są sformułowane tak:

> Centralny Rejestr Lekarzy jest prowadzony i udostępniony przez Naczelną Izbę Lekarską jako źródło informacji o lekarzach i lekarzach dentystach posiadających prawo wykonywania zawodu w Polsce. Celem Rejestru jest:
  
> 1. udostępnienie pacjentom, na użytek własny, informacji o lekarzu lub lekarzu dentyście którego porady mogą zasięgnąć,
  
> 2. udostępnienie lekarzom informacji o lekarzach w celach związanych z prowadzonym leczeniem pacjenta (np. konsultacje).
> 
> Rejestr ani żadne dane w nim zawarte nie mogą być, bez zawarcia stosownej umowy z Naczelną Izbą Lekarską, pobierane, publikowane, sprzedawane, kopiowane w całości ani w części w celach innych niż wymienione w pkt 1 2.
> 
> W razie stwierdzenia faktu, że użytkownik korzysta z Rejestru w sposób lub w zakresie niezgodnym z w/wym warunkami, Naczelna Izba Lekarska zastrzega możliwość niezwłocznego zablokowania dostępu do Rejestru dla tego użytkownika.
> 
> Naczelna Izba Lekarska dokłada wszelkich niezbędnych starań do zapewnienia dokładności i aktualności danych zawartych w Rejestrze. Z uwagi na fakt gromadzenia danych pochodzących od wszystkich okręgowych izb lekarskich oraz mogące wystąpić w procesie przesyłania danych błędy i opóźnienia, Naczelna Izba Lekarska nie gwarantuje dokładności ani aktualności danych zawartych w Rejestrze.
> 
> Dane zawarte w Rejestrze udostępniane mają charakter wyłącznie informacyjny.

Jeżeli dobrze rozumiem, oznacza to że rejestr jest po to, żeby można było sobie sprawdzić stan rejestru na użytek własny, natomiast jakiekolwiek inne wykorzystanie wymaga pisemnej umowy z Naczelną Izbą Lekarską.

Po zaakceptowaniu warunków korzystania i wpisaniu kodu dostaniemy informacje takie jak numer prawa wykonywania zawodu, numer seryjny dokumentu uprawniającego, numer wpisu w rejestrze oraz aktualny status, np. „lekarz wykonujący zawód (bez ograniczeń)”.

Dane te nie są umieszczone w naszym serwisie; znajdują się one na stronie Okręgowej Izby Lekarskiej, a nasz serwis udostępnia tylko linki.

 [1]: http://www.atopowe.pl/lekarze/
 [2]: http://code.google.com/p/django-phpbb/
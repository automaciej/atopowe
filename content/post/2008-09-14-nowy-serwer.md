+++
author = "Wahwah"
categories = ["Techniczne"]
date = "2008-09-14"
layout = "post"
tags = ["hosting"]
title = "Nowy serwer!"
url = "/2008/09/14/nowy-serwer/"

+++

Przeniosłem nas na nowy serwer. Dla ciekawskich, kilka historycznych informacji o wędrówkach naszego serwisu.

  1. Pierwszy był serwer firmowy, czyli maszyna którą administrowałem w ramach pracy. Oczywiście wszystko za zgodą szefa. Bardzo wygodnie jest, kiedy ma się pełny dostęp administracyjny do serwera. Innymi słowy, kiedy ma się roota. Ale wszystko co dobre, kiedyś się kończy.
  2. Dreamhost. Tani hosting, niesamowicie dużo miejsca. Obsługuje [Django][1]. Niestety, fizycznie znajdujący się bardzo daleko od Polski, co powodowało że strony otwierały się bardzo powoli.
  3. Irlandzki register365. Strony zaczęły otwierać się zdecydowanie szybciej niż z Dreamhosta. Niestety, pisali że obsługują Django, ale kiedy przyszło co do czego, okazało się że wcale nie obsługują! W związku z tym serwowałem [dział polecanych lekarzy][2] z domowego laptopa stojącego na zwykłym DSLu, który się często zrywał i dział ten często nie działał.
  4. Instancja [Xen][3]. Kolega z pracy wynajmuje w maszynę stojącą w jednym datacenter w Niemczech. Założył na niej kilka instancji Xen, czyli serwerów wirtualnych, współdzielących ten sam kawałek metalu. Znów mam roota, i co za tym idzie, pełną swobodę w konfiurowaniu serwera. Również prędkość otwierania się stron powinna być duża, bo maszyna jest mocna i mało obciążona.

UPDATE 2008-09-17: W poniedziałek i wtorek serwis działał bardzo powoli. Problemem okazał się [błąd w Xen][4], który polegał na ignorowaniu ustawienia MTU przez interfejs sieciowy Xen i jednoczesnym niedziałaniu PMTU discovery. Obejście problemu &#8211; jak się wie, gdzie on jest &#8211; jest na szczęście proste i serwis działa już z pełną prędkością.

 [1]: http://www.djangoproject.com/
 [2]: http://www.atopowe.pl/lekarze/
 [3]: http://pl.wikipedia.org/wiki/Xen
 [4]: https://bugs.launchpad.net/ubuntu/+source/linux/+bug/238573
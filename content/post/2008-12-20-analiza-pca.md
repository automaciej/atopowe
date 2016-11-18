+++
author = "Wahwah"
kategorie = ["Forum"]
date = "2008-12-20"
layout = "post"
title = "Analiza PCA"
url = "/2008/12/20/analiza-pca/"

+++

Niedawno dla zabawy zrobiłem analizę zawartości forum pod kątem tego, kto używa jakich słów jak często w spoich postach. Każdy użytkownik to punkt w wielowymiarowej przestrzeni, w której każde słowo jest jednym wymiarem. Potem użyłem PCA (Principal Component Analysis) żeby „spłaszczyć” tę przestrzeń do dwóch wymiarów i zrobić wykres. Musiałem zrobić PDF (a nie PNG), bo wykres jest bardzo duży i są na nim małe literki, inaczej by się to wszystko nie zmieściło.

<!--more-->

<div id="attachment_378" style="width: 310px" class="wp-caption alignnone">
  <a href="http://www.atopowe-zapalenie.pl/mediawiki/images/a/a0/Atopowe-pca-2008-12-400-wymiarow.pdf"><img class="size-medium wp-image-378" title="Analiza forum przy pomocy PCA" src="http://blog.atopowe.pl/wp-content/uploads/2008/12/atopowe-pca-300x175.png" alt="Analiza forum przy pomocy PCA" width="300" height="175" /></a>
  
  <p class="wp-caption-text">
    Analiza forum przy pomocy PCA
  </p>
</div>

PCA to Principal Component Analysis, czyli „analiza podstawowych składników”. Polega ona na tym, żeby z kilku pozornie niezależnych sygnałów odtworzyć ukryty, podstawowy sygnał. Na przykład powiedzmy, że osoby które często używają słowa „iż”, używają również słowa „zaś”. (Przykład jest wymyślony.) Skoro więc cecha „używanie iż” współwystępuje z „używaniem zaś”, być może wcale nie mamy do czynienia z dwoma osobnymi cechami, tylko z jedną, która manifestuje się na dwa sposoby. PCA pozwala na odtworzenie tej oryginalnej cechy i dostarczenie wzoru, który pozwala przeliczyć dwa osobne sygnały na jeden.

Na wykresie czerwone strzałki oznaczają słowa kluczowe. Strzałki pokazujące z grubsza w jednym kierunku oznaczają że są to słowa skorelowane ze sobą. Niektóre słowa na wykresie to tylko elementy stylu, takie jak „właśnie”, „miałam”, czy „mój” albo „proszę”. Inne wskazują na konkretne tematy, na przykład „mleka” albo „dziecku”. Inne wskazują na uczestnictwo w konkretnych wątkach, np. „oświadczam”.

Ciekawe jest to, że większość strzałek jest skierowanych w jednym kierunku, a większość nicków jest na dole, czyli tam gdzie strzałki _nie_ wskazują. Podejrzewam że jest to wynik wzięcia pod uwagę tylko 400 słów w analizie. Osoby w górnej części wykresu to te, które używają tych często spotykanych słów, a te na dole to tzw. [długi ogon][1], czyli osoby które tych najczęściej spotykanych nie używają, ale i tak jest ich więcej. Skoro jednak jednymi z często używanych słów są „alergolog” i „dermatolog”, słowa te są na górze, a wiele osób jest na dole, to znaczy że sporo osób rozmawia na jakieś inne tematy. Być może są to offtopikowicze, a być może tematów związanych z AZS jest o wiele więcej i wcale nie muszą być to rozmowy o alergologach czy dermatologach.

W ramach zabawy towarzyskiej, proponuję coś takiego: zobaczcie, gdzie na wykresie jest Wasz nick. Potem zobaczcie jakie nicki są w okolicy, a potem użyjcie [opcji wyszukiwania użytkowników][2] żeby znaleźć te osoby na forum i zobaczyć o czym piszą. Może trafi się osoba która ma podobne zainteresowania, a której nie znacie, bo akurat wypowiadała się w innych wątkach?

### Problemy jakie napotkałem

  * Nie da się na jednym wykresie umieścić 3500 nicków, bo się po prostu nie mieszczą. Wybrałem użytkowników którzy mają conajmniej 10 postów, jest ich 485.
  * Mój komputer nie był w stanie obrobić 350 tysięcy słów (nie wszystkie „słowa” to prawdziwe słowa z języka polskiego, niektóre to literówki, albo identyfikatory, liczby, fragmenty linków, etc.). Musiałem obciąć dane do pierwszych 2000 najpopularniejszych słów przy obróbce wstępnej.
  * Metoda PCA pozwala na zredukowanie liczby wymiarów, ale nie więcej niż jest punktów danych. Nie można wziąć pod uwagę więcej słów kluczowych niż jest użytkowników. Przeanalizowałem więc 400 najpopularniejszych słów kluczowych.
  * Polskie litery. Nie widać ich. Naprawiłbym gdybym miał więcej czasu.

### FAQ

  * _Po co zrobiłeś ten wykres?_
  
    Po nic szczególnego, dla zabawy. Trochę też po to, żeby odświeżyć moje supermoce analityczno-statystyczne, które od dwóch lat stały odłogiem.
  * _Czy coś wynika z tego wykresu?
  
_ Nie. Potraktuj to jako zabawę towarzyską.
  * _Co to jest PCA?
  
_ Przecież napisałem wyżej&#8230;
  * _A nie było lepszej metody od PCA?
  
_ Owszem, była, nazywa się ICA. Podejrzewam że będzie lepsza, ale jest trudniejsza w użyciu.
  * _Jakieś inne metody?
  
_ Myślałem jeszcze o k-means, ale nie mam dobrego pomysłu na zaprezentowanie wyników. A tak poza tym to jestem otwarty na sugestie.
  * _Z kiedy są dane?
  
_ Użyłem migawki forum z 23 listopada 2008.
  * _Co zajęło najwięcej czasu?
  
_ Jak zwykle, przygotowanie danych do formatu, który może zostać obrobiony przez metodę statystyczną.
  * _Czy wziąłeś pod uwagę odmianę słów w języku polskim?
  
_ Nie, zupełnie nie. „Krowa” i „krowie” to wedle mojej analizy dwa różne słowa.
  * _Gdzie jest mój nick na wykresie?
  
_ Spróbuj użyć opcji wyszukiwania w programie który wyświetla PDFy.
  * _Czy nie uważasz że śmiesznie wyszło, że słowo „alveo” jest tuż obok twojego nicka, a odrobinę w lewo jest Greg?_
  
    Uważam! Ironia statystyki&#8230;

**[atopowe-pca-2008-12-400-wymiarow.pdf][3]**

 [1]: http://pl.wikipedia.org/wiki/D%C5%82ugi_ogon
 [2]: http://www.atopowe-zapalenie.pl/forum/memberlist.php?mode=searchuser
 [3]: http://www.atopowe-zapalenie.pl/mediawiki/images/a/a0/Atopowe-pca-2008-12-400-wymiarow.pdf
# Atopowe.pl

To co wcześniej było na MediaWiki i Wordpressie, teraz jest serwowane ze
statycznych plików HTML, nie ma na serwerze żadnej bazy danych. Treść jest
przechowywana i edytowana w formacie Markdown, a pliki HTML generuje się przy
pomocy programu [hugo](http://gohugo.io/).

## Wymagane pliki

Oprócz tego co jest w tym repozytorium, potrzebne są:

*   jQuery
*   Bootstrap https://getbootstrap.com/
*   Font Awesome http://fontawesome.io/
*   Social buttons https://lipis.github.io/bootstrap-social/

Biblioteki należy umieścić w katalogu static, w podkatalogach:

    static/css
    static/fonts
    static/js

## Istniejące problemy

*   Jest dużo (!) zepsutych / niedziałających linków.
*   Na serwerze są pliki których nie ma tutaj w repozytorium. Potrzebne jest
    przejrzenie wszystkiego co jest na serwerze, dodanie do repozytorium tego co
    potrzebne, skasowanie reszty.
*   Jest sporo pustych stron, które są tylko przekierowaniami i powinny zostać
    zamienione na prawdziwe przekierowania.
*   Nawigacja po stronie jest niejasna. Potrzebna jest jasna ścieżka nawigacji
    dla osoby która wylądowała na stronie, i niczego nie wie o AZS.

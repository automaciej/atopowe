+++
author = "Wahwah"
date = "2016-04-23T11:44:28+01:00"
title = "Reorganizacja serwisu atopowe.pl"
lastmod = "2016-11-20T13:29:15+00:00"
description = "W kwietniu 2016 r. stare forum zostanie wyłączone, a treść przeniesiona w nowe miejsca, które nie będą od nas wymagały aktywnego utrzymywania."
image = "/images/archive.jpg"

+++

![](/images/archive.jpg "Archive, Carolina Prysyazhnyuk, source: https://flic.kr/p/qBVcyE")

[Przenosimy treść serwisu w inne miejsca][reddit-opis], które mają już
istniejącą infrastrukturę i nie będą wymagały od nas wysiłku przy utrzymywaniu.

*   Atopedia:

    Instalacja MediaWiki zostanie zamieniona na pliki HTML. Stare URLe pozostaną
    dostępne, z minimalnymi różnicami.

*   Forum:

    1. Przełączę forum w tryb tylko do odczytu &mdash; nie będzie można już pisać na
       atopowe.pl/forum. (spróbuję zamienić je na pliki statyczne)
    1. Umieszczę linki do [/r/atopowezapalenieskory][reddit].
    1. Poproszę obecnych moderatorów o pomoc z utrzymywaniem porządku na subie.

*   Blog:

    Zamienię instalację wordpress na statyczne pliki HTML.

*   domeny atopowe.pl i atopowe-zapalenie.pl:

    Na domeny na razie nie konkretnych planów.

&mdash;wahwah

-------

*   Aktualizacja 2016-04-24: Atopedia, forum i blog są już w postaci archiwum i plików
    statycznych. Teraz można je przenieść na normalny hosting, pod warunkiem że
    będzie tam Apache i możliwość używania plików .htaccess i mod_rewrite, bo
    jest to potrzebne do archiwum forum.

*   Aktualizacja 2016-11-16: Po migracji było sporo problemów. Strona główna
    była brzydka, nie można było wyświetlić plików z jednej kategorii,
    niedziałające linki wewnętrzne (kilkało się na jakiś link na Atopedii, i on
    prowadził do nieistniejącego adresy). Część problemów jest już rozwiązana,
    ale jeszcze nie wszystkie.

*   Aktualizacja 2016-11-17: Wszystkie wewnętrzne linki działają, i wszystkie
    obrazki działają. Pozostało przejrzenie pod względem organizacji materiału,
    i usunięcie niepotrzebnych stron.

*   Aktualizacja 2016-11-20: Zredukowałem liczbę artykułów / podstron. Na blogu
    z 217 do 86 wpisów (czyli o 60%), na Atopedii z oryginalnych 634 artykułów
    do 203 (nie licząc ulotek i kosmetyków). Dodałem też menu po prawej stronie
    wszystkich podstron, dzięki czemu będzie łatwiej przejść do innego artykułu.
    Na razie wyliczyłem artykuły z kategorii "podstawowe wiadomości" z
    założeniem, że jest to dla osób nowych na stronie.

[reddit-opis]: https://www.reddit.com/r/atopowezapalenieskory/comments/4fb20l/reddit_i_wiki_plan_reorganizacji_atopowepl/
[reddit]: https://www.reddit.com/r/atopowezapalenieskory/
[github]: https://github.com/automatthias/atopowe-hugo

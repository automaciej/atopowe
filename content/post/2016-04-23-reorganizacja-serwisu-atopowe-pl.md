+++
author = "Wahwah"
date = "2016-04-23T11:44:28+01:00"
title = "Reorganizacja serwisu atopowe.pl"
description = """
W kwietniu 2016 r. stare forum zostanie wyłączone, a treść przeniesiona \
w nowe miejsca, które nie będą od nas wymagały aktywnego utrzymywania."""
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

[reddit-opis]: https://www.reddit.com/r/atopowezapalenieskory/comments/4fb20l/reddit_i_wiki_plan_reorganizacji_atopowepl/
[reddit]: https://www.reddit.com/r/atopowezapalenieskory/
[github]: https://github.com/automatthias/atopowe-hugo

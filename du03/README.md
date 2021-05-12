# Domácí úkol č. 3 - vyhledávač cest

## Zadání
Napište aplikaci pro vyhledávání cesty v dané síti komunikací. Aplikace dostane
jako vstup síť komunikací (vhodný formát si zvolte a zdokumentujte) a umožní nad touto sítí
vyhledávat cesty mezi počátečním a cílovým bodem.

Počáteční a cílový bod budou zadány pomocí souřadnic v souřadnicovém systému
WGS-84, program najde k zadanému počátečnímu a cílovému bodu vždy nejbližší bod
na síti a mezi těmito body najde po síti nejkratší cestu, kde jako metriku délky
považujeme vzdálenost v metrech. Tuto cestu pak uloží jako GeoJSON nebo ji
zobrazí v grafickém rozhraní.

### Varianty
Aplikace může mít 2 varianty - konzolovou a grafickou. V případě konzolové je
minimální funkční rozhraní specifikováno jako:
```<jmeno_skriptu.py> --net <vstupni_soubor> --out <vystupni_soubor> --from <lat> <lon> --to <lat> <lon> ```
Jednotlivé parametry příkazové řádky mohou být libovolně přeuspořádány.

V případě grafické bude rozhraní v QML, název vstupního souboru může být
definován jako konstanta ve zdrojovém kódu, počáteční a koncový bod se bude
vybírat kliknutím do mapového pole a nalezená cesta se zobrazí na mapě (není
potřeba ji ukládat jako GeoJSON).

### Dokumentace 
K aplikaci dodejte stručnou uživatelskou a vývojářskou dokumentaci a objektový
návrh, ve kterém popíšete architekturu aplikace - které modely drží jaká data a
jak jsou spolu propojeny a jak spolu interagují. Propojení můžete znázornit i
graficky (např. pomocí UML např. v nástroji Dia). Zdokumentujte také postup
zpracování vstupních dat sítě pro vyhledávání.

## Doporučení
Platí doporučení pro předchozí úkoly, navíc by se vám mohly hodit následující
odkazy:
 - [Jak zobrazovat cestu v
   QML](https://stackoverflow.com/questions/48071952/qml-how-to-change-mappolyline-path-from-c) + [zdroják pro C++](https://github.com/eyllanesc/stackoverflow/tree/master/questions/48071952)
 - [Knihovna Click](https://click.palletsprojects.com/en/8.0.x/)

## Odevzdávání
Odevzdávat budete zdrojové soubory a soubor(y) s dokumentací. Odevzdávejte
ideálně přes GitHub nebo podobnou službu, případně je možné poslat i vše
zabalené v zipu.

Deadline na odevzdání je týden před tím, než budete chtít zápočet, o prázdninách
2 týdny. Každému, kdo mi pošle úkol, odpovím, že jsem ho přijal. Pokud
neodpovím, urgujte.

Samozřejmě můžete odevzdávat úkol vícekrát a já vám k němu budu průběžně dávat
zpětnou vazbu a náměty k vylepšení. Pokud budete chtít vědět, kolik byste za
danou variantu dostali bodů, prosím explicitně to napište.

## Bodování
  * 3 b za konzolovou variantu
  * 3 b za grafickou variantu
  * 2 b za kvalitu kódu
  * 2 b za dokumentaci

## Bonusové body

### Uvažování převýšení (2 b)
Program kromě sítě načte i bitmapu s nadmořskými výškami a jednotlivým vrcholům
sítě přiřadí jejich nadmořskou výšku. Při vyhledávání cesty pak délku hrany mezi
dvěma vrcholy upraví podle následujícího vzorce: 
 - hrana je do kopce: `upravena_delka = delka + up_coeff*(vyska_konce - vyska_zacatku)`
 - hrana je z kopce: `upravena_delka = delka + down_coeff*(vyska_konce - vyska_zacatku)`

Koeficienty `up_coeff` a `down_coeff` jsou v konzolové aplikaci určeny pomocí
parametrů `--up <up_coeff>` a `--down <down_coeff>` příkazové řádky. Pokud
nejsou parametry určeny, berou se jako nulové, tedy s převýšením se nepočítá. V
grafické aplikaci se zadávají do k tomu určených textových polí a po stisknutí
potvrzovacího tlačítka dojde k upravení sítě, aby respektovala aktuálně
nastavené hodnoty. 

Bitmapa s nadmořskými výškami se u konzolové verze zadává pomocí argumentu
`--heights <jmeno_souboru>`, v grafické verzi může být jméno souboru definované
jako konstanta ve zdrojáku.


### Načítání sítě v GUI pomocí dialogu (1 b)
Místo pevně zadaného jména souboru se zdrojovými daty sítě je tento soubor možné
vybrat v grafickém rozhraní pomocí standardního dialogu (viz [dokumentace
QML](https://doc.qt.io/qt-5/qml-qtquick-dialogs-filedialog.html)). Pokud
aplikace podporuje výpočet převýšení, pak by pro splnění tohoto bonusu měla být
i bitmapa načítána pomocí standardního dialogu.

### Více alternativních cest (3 b)
Kromě nejkratší cesty najde aplikace i druhou a třetí nejkratší cestu. V
konzolové verzi ji přidá do výstupního GeoJSONu a vhodně je označí v atributech,
v grafické verzi je zobrazí graficky odlišně na mapě.

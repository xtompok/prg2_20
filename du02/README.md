# Řády vodních toků

## Zadání
Napište aplikaci, která z dat DIBAVOD spočítá řády jednotlivých toků a součet
délek toků pro každý řád.

Zdrojová data můžete stáhnout z [webu projektu
DIBAVOD](https://www.dibavod.cz/index.php?id=27), použijte datovou sadu A02. 

Výstupem by měl být soubor ve formátu GeoJSON obsahující všechny prvky se všemi
atributy jako ve vstupním souboru, navíc s přidaným atributem `RAD_TOKU`, který
bude obsahovat informaci o řádu daného toku. Navíc program vypíše součet délek
toků v daném řádu pro každý řád, který se v datech vyskytuje a součet délek
toků, které jsou nedosažitelné ze vstupních povodí (viz níže).

Aplikace bude jako vstup brát soubor se vstupními daty (formát si zvolte z
běžně používaných geoformátů) a soubor, ve kterém budou uvedeny řády toků, od
kterých se budou další toky odvozovat. Tok určujte pomocí `TOK_ID`, formát
souboru si zvolte. V základní variantě programu uvažujte pouze povodí Labe, Odry
a Moravy.

### Dokumentace
K aplikaci dodejte stručnou uživatelskou a vývojářskou dokumentaci. V
dokumentaci popište, jakým způsobem jsou geodata převáděna na interní formát a
jakým způsobem probíhá přiřazování řádu toků. Také uveďte, v jakém formátu
očekáváte vstupní data.

## Doporučení
Zkuste se nejprve rozmyslet, jakým způsobem bude aplikace fungovat, jak bude
zpracovávat data, jak si je bude ukládat a jak bude počítat řády toků. Tento
návrh mi pošlete, já vám ho okomentuji a pak se teprve pusťte do programování.
Pokud si s tímto návrhem nebudete vědět rady, ozvěte se a domluvíme se na
konzultaci.

Pokud se vám něco nebude dařit, zkonzultujte to s ostatními ve skupině, pokud si
stále nebudete vědět rady, nebojte se ozvat, rád vám pomohu.

## Odevzdání
Odevzdávat budete zdrojové soubory a soubor(y) s dokumentací. Odevzdávejte
ideálně přes GitHub nebo podobnou službu, případně je možné poslat i vše
zabalené v zipu.

Deadline na odevzdání je 9. 5. 2021 v 8.03. Úkoly odeslané po deadlinu budou
brány jako neodevzdané. Pokud odevzdáte úkol vícekrát, budu hodnotit poslední
odevzdání před deadlinem.  Každému, kdo mi pošle úkol, odpovím, že jsem ho
přijal a že se mi podařilo zip rozbalit. Pokud neodpovím, urgujte.

### Předčasné odevzdání
Pokud odevzdáte úkol dopředu, zkusím se na něj podívat a napsat vám případné
nedostatky. Tato možnost není garantovaná, ale budu se snažit odbavovat úkoly co
nejrychleji. Zaručuji vám pouze to, že na úkoly se budu dívat v tom pořadí, v
jakém mi budou doručeny. Rovněž nezaručuji, že najdu v programu všechny chyby
napoprvé, tudíž pokud si nějaké nevšimnu, není to garance, že máte program
správně, závazné je pouze hodnocení po deadlinu. Pokud budete odevzdávat přes
GitHub, chyby vám vystavím jako Issue.

## Bodování
  * 5 b za funkční aplikaci
  * 3 b za kvalitu kódu
  * 2 b za dokumentaci

## Bonusové body

### Více povodí (1 b)
Mimo povodí Labe, Odry a Moravy uvažujte ještě alespoň 10 dalších toků, které z
ČR odtékají, aniž by byly na území ČR součástí nějakého z výše uvedených povodí.
Tyto toky přidejte do vstupního souboru spolu s jejich řádem.

### Výpis nedosažitelných toků (1 b)
Vypište jména všech pojmenovaných toků, jimž nebyl určen řád, protože jsou z
daných vstupních povodí nedosažitelné na území ČR.

### Výpis nedoažitelných toků vytékajících z ČR (2 b)
Vypište jména všech pojmenovaných toků, jimž nebyl určen řád, protože jsou z
daných vstupních povodí nedosažitelné na území ČR a z území ČR vytékají (tedy se
nevlévají do jiného nedosažitelného toku. Jako poznávací znamení berte, že
takový tok na žádném konci nenavazuje na jiný tok.


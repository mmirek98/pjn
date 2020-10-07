# Przetwarzanie języka naturalnego
# Laboratorium 1: prawo Zipfa

1. Skopiować zawartość niniejszego repozytorium
na dysk lokalny.

    ```
    git clone https://github.com/PK-PJN/laboratorium01.git
    cd laboratorium01
    ```

2. Zainstalować zewnętrzne biblioteki Pythona:
`matplotlib` do tworzenia wykresów i `morfeusz2`
do analizy morfologicznej tekstów polskich: patrz
[instrukcje instalacji Morfeusza](http://morfeusz.sgjp.pl/download/).

    ```
    pip install matplotlib
    ```

3. Pobrać z serwisu https://wolnelektury.pl dowolną książkę
w postaci pliku tekstowego i przypisać nazwę tego pliku
zmiennej `KSIĄŻKA` w pliku `zadanie.py`. Oto przykładowe
długie książki: *Don Kichot z La Manchy*, *O duchu praw*,
*Quo vadis*, *Pan Wołodyjowski*, *Pustelnia parmeńska*,
*Czerwone i czarne*, *Legenda Młodej Polski*, *Germinal*,
*20 000 mil podmorskiej żeglugi*, *Młyn na wzgórzu*.

4. W pliku `zadanie.py` uzupełnić funkcję `podaj_wyrazy()`
tak, żeby traktowała takie ciągi znaków, jak *biało-czerwona*,
*George’owi*, czy *7,7-dimetylobicyklo[2.2.1]heptan* jako
pojedyncze wyrazy. Nie przejmujemy się tym, że funkcja
usunie kropki, stanowiące część skrótów, na przykład
*np.*, *itd.*, *itp.* Wskazówki:

    * plik tekstowy o nazwie `nazwa_pliku` jest otwarty
    do odczytu jako zmienna o nazwie `plik` wewnątrz bloku
    kodu, który zaczyna się tak:

    ```python
        with open(nazwa_pliku, 'rt', encoding='utf-8') as plik:
    ```

    * najprościej jest wczytać całą zawartość pliku
    i podzielić ją na części zgodnie z „białymi znakami”,
    czyli znakami spacji, tabulacji i nowego wiersza:

    ```python
            for część in plik.read().split():
    ```

    * następnie od każdej części odrzucić początkowe
    i końcowe znaki przestankowe, korzystając z metody
    `.strip()`:

    ```python
                wyraz = część.strip(',.')
    ```

    * i kolejno przekazywać tak skrócone części do miejsca
    wywołania naszego generatora, o ile po skróceniu
    cokolwiek z nich zostało:

    ```python
                if wyraz != '':
                    yield wyraz
    ```

    * sprawdzić działanie funkcji `podaj_wyrazy()` przez
    wypisanie takich pierwszych i ostatnich znaków wyrazów,
    które nie są ani literami, ani cyframi:

    ```python
    def wypisz_skrajne_znaki_wyrazów(nazwa_pliku):
        znaki = collections.Counter()
        for wyraz in podaj_wyrazy(nazwa_pliku):
            znaki[wyraz[0]] += 1
            znaki[wyraz[-1]] += 1
        for znak, ile_wystąpień in znaki.most_common():
            if not znak.isalnum():
                print(znak, ile_wystąpień)
    ```

    * jeśli wywołanie funkcji `wypisz_skrajne_znaki_wyrazów(KSIĄŻKA)`
    wypisuje jakieś znaki, to należy dodać te znaki do napisu,
    który przekazujemy do metody `.strip()`, po czym powtórzyć
    niniejszy podpunkt;

    * do dalszych podzadań można przejść wtedy, gdy wywołanie
    funkcji `wypisz_skrajne_znaki_wyrazów(KSIĄŻKA)`
    nic nie wypisuje.

5. W funkcji `main()` dodać zliczanie wystąpień poszczególnych
wyrazów w kolekcji `wyrazy` typu `collections.Counter` oraz
zliczanie sumarycznej liczby wyrazów w zmiennej `długość_tekstu`
typu liczbowego. Następnie dodać wypisywanie 10 najczęstszych
wyrazów wraz z częstością ich wystąpień. Uwagi:

    * Przy wypisywaniu użyć metody `.most_common(10)`.

    * Zgodnie z
    [prawem Zipfa](https://pl.wikipedia.org/wiki/Prawo_Zipfa)
    iloczyn rangi wyrazów (czyli ich numerów na liście
    frekwencyjnej) i częstości ich występowania w tekście
    jest w przybliżeniu stały, np. jeśli najczęstszy wyraz
    stanowi 2% tekstu, to wyraz dziesiąty pod względem
    częstości stanowi 0,2% tekstu, wyraz setny — 0,02%
    tekstu itd. Zatem podwójnie logarytmiczny wykres
    częstości wyrazów jako funkcji ich rangi powinien
    się układać w linię prostą: pomnożeniu rangi wyrazu
    przez 10 (zwiększeniu logarytmu rangi o 1) powinien
    odpowiadać dziesięciokrotny spadek częstości tego
    wyrazu (zmniejszenie logarytmu częstości o 1).

    * Odstępstwa od prawa Zipfa zachodzą w rozkładzie
    tak zwanych *wyrazów funkcyjnych*: spójników,
    przyimków, partykuł itp., które zazwyczaj są
    najczęstszymi wyrazami języka.

6. W funkcji `main()` dodać rysowanie półlogarytmicznego
wykresu pokrycia tekstu przez wyrazy. *N*-ty element
tablicy `y` ma być równy sumie częstości wyrazów
od pierwszego do *N*-tego pod względem malejącej
częstości. Uwagi:

    * Kształt tego wykresu jest konsekwencją prawa Zipfa.

    * Jeśli wykres nie przypomina linii prostej, sprawdzić
    sposób wypełniania tablicy `y`. Suma częstości wyrazów
    od pierwszego do *N*-tego to nie to samo, co suma
    elementów `y[0:N]`.

7. Uzupełnić funkcję `jednoznaczna_forma_podstawowa()` tak,
aby zwracała ona:

    * Albo dany `wyraz`, jeśli nie znaleziono żadnej jego
    formy podstawowej.

    * Albo jedyną formę podstawową, która odpowiada danej
    wartości zmiennej `wyraz`.

    * Albo najkrótszą z form podstawowych, które odpowiadają
    danej wartości zmiennej `wyraz`, np. dla wyrazu `'dam'`
    funkcja ma zwrócić krótszą z form `'dać'` i `'dama'`.
    Gdy formy podstawowe mają jednakową długość, funkcja
    ma zwrócić pierwszą z nich w porządku leksykograficznym,
    np. dla wyrazu `'patrzę'` — pierwszą z form `'patrzeć'`
    i `'patrzyć'`. Wskazówki:

        * Funkcja `formy_podstawowe()` zwraca posortowaną listę.
        Dla naszych celów ważne jest to, że porządek jest
        niezmienny, a nieważne to, że np. `'b' < 'ą'`.

        * Wywołanie funkcji `len(napis)` zwraca długość
        napisu `napis`. Podobnie wywołanie funkcji
        `len(lista)` zwraca długość listy `lista`.

8. W funkcji `main()` dodać zliczanie form podstawowych wyrazów
i rysowanie wykresów częstości ich wystąpień oraz pokrycia
przez nie tekstu. Uwagi:

    * Jeśli wykresy nie przypominają linii prostych, tylko
    parabole, sprawdzić, czy wybrano dla nich skalę
    logarytmiczną na osi *x* i ewentualnie *y*.

    * Jeśli wykresy nie przypominają linii prostych, tylko
    są pogięte, sprawdzić sposób iterowania po kolekcji
    `formy`. Metoda `.values()` nie zwraca liczników
    w kolejności malejącej. Zamiast niej należy użyć metody
    `.most_common()`.

    * Jeśli wykresy nadal nie przypominają linii prostych,
    wypisać najczęstsze formy podstawowe. Jeśli są one
    podobne do `[('być', 41), ('móc', 32), ('znać', 32),...`,
    sprawdzić, skąd są pobierane formy. Kolekcja `wyrazy`
    to nie to samo, co generator `podaj_wyrazy(KSIĄŻKA)`.

9. W sprawozdaniu zamieścić uzupełnioną zawartość pliku
`zadanie.py`, tytuł wybranej książki, 10 najczęstszych
wyrazów w tej książce wraz z częstością ich wystąpień
oraz cztery wykresy, stworzone za pomocą programu.
Wykresy można zapisywać na dysku po kliknięciu ikony
dyskietki (pierwszej ikony od prawej strony na dole
okna z wykresem). Poniżej zasady składania sprawozdań
ze wszystkich laboratoriów:

    * Format PDF (plik o dowolnej nazwie).

    * Na początku dane twórcy.

    * Wgrywane na MS Teams w dziale Assignments.
    Proszę nie zapomnieć nacisnąć "turn in".

10. Zadanie nadobowiązkowe:

    * Skopiować plik `zadanie.py` do `zadanie_ang.py`.
    Kolejne podpunkty dotyczą pliku `zadanie_ang.py`.

    * Pobrać z serwisu https://www.gutenberg.org/ jakąś książkę
    w języku angielskim w postaci pliku tekstowego i przypisać
    nazwę tego pliku zmiennej `KSIĄŻKA`.

    * Jeśli wywołanie funkcji `wypisz_skrajne_znaki_wyrazów(KSIĄŻKA)`
    wypisuje jakieś znaki, to dodać te znaki do napisu, który
    przekazujemy do metody `.strip()` i powtórzyć niniejszy podpunkt.

    * Zainstalować `pystemmer` — zewnętrzną bibliotekę, która
    umożliwia usuwanie częstszych końcówek odmiany i derywacji
    z wyrazów angielskich:

    ```
    pip install pystemmer
    ```

    * Dopisać na początku pliku poniższe dwa wiersze:

    ```python
    import Stemmer
    STEMMER = Stemmer.Stemmer('english')
    ```

    * Tuż po nagłówku funkcji `jednoznaczna_forma_podstawowa(wyraz)`
    wpisać

    ```python
        return STEMMER.stemWord(wyraz)
    ```

    * Dołączyć do sprawozdania 10 najczęstszych wyrazów
    w wybranej angielskiej książce wraz z częstością
    ich wystąpień oraz zapisać na dysku i dołączyć
    do sprawozdania cztery wykresy uzyskane dla tej
    książki, analogiczne do czterech wykresów uzyskanych
    w sposób opisany powyżej dla polskiej książki.
    Proszę nie dołączać treści pliku `zadanie_ang.py`.

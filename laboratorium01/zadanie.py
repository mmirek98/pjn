#!/usr/bin/python3

"""Przetwarzanie języka naturalnego, laboratorium 1."""

import collections
import functools

import morfeusz2
import matplotlib.pyplot as plt


KSIĄŻKA = 'jadro_ciemnosci.txt';  # TU(3): wpisać nazwę pliku z tekstem książki.

# Chociaż biblioteki morfeusz2 używa się zwykle do analizowania
# dłuższych tekstów, my używamy jej tylko do analizowania
# pojedynczych wyrazów.
# Dzięki parametrowi praet='composite' formy czasu przeszłego
# i trybu przypuszczającego są analizowane jako jeden segment,
# a nie jako np. 'robił' + 'by' + 'm'.
MORFEUSZ = morfeusz2.Morfeusz(praet='composite')


def podaj_wyrazy(nazwa_pliku):
    # TU(4): uzupełnić zgodnie z instrukcją.
    with open(nazwa_pliku, 'rt', encoding='utf-8') as plik:
        for czesc in plik.read().split():
            wyraz = czesc.strip(',.—;?!…:„”()*&-–/')
            if wyraz != '':
                yield wyraz


def wypisz_skrajne_znaki_wyrazów(nazwa_pliku):
    znaki = collections.Counter()
    for wyraz in podaj_wyrazy(nazwa_pliku):
        znaki[wyraz[0]] += 1
        znaki[wyraz[-1]] += 1
    for znak, ile_wystapien in znaki.most_common():
        if not znak.isalnum():
            print(znak, ile_wystapien)
    # TU(4): uzupełnić zgodnie z instrukcją.


@functools.lru_cache(maxsize=None)
def formy_podstawowe(wyraz):
    formy = []
    for interpretacja in MORFEUSZ.analyse(wyraz):
        formy.append(interpretacja[2][1])
    return sorted(formy)


def jednoznaczna_forma_podstawowa(wyraz):
    formy = formy_podstawowe(wyraz)
    # TU(7): uzupełnić zgodnie z instrukcją.
    if len(formy) == 0:
        return wyraz
    else:
        return formy[0]
    return wyraz


def zlicz_wyrazy(nazwa_pliku):
    wyrazy = collections.Counter()
    długość_tekstu = 0
    for wyraz in podaj_wyrazy(nazwa_pliku):
        długość_tekstu += 1
        wyrazy[wyraz] += 1
    return (wyrazy, długość_tekstu)


def znajdz_formy_podstawowe(wyrazy):
    formy = collections.Counter()
    for wyraz, liczba_powtorzen in wyrazy.most_common():
        forma = jednoznaczna_forma_podstawowa(wyraz)
        formy[forma] += liczba_powtorzen
    return formy


def zadanie_5_wypisz_najczestsze_wyrazy(wyrazy, długość_tekstu):
    for wyraz in wyrazy.most_common(10):
        print(wyraz)
    print('sumaryczna liczba wyrazów: ', długość_tekstu)


def zadanie_5_stworz_wykres_czestosci_wyrazow(wyrazy, długość_tekstu):
    y = []
    for _, ile_wystąpień in wyrazy.most_common():
        y.append(ile_wystąpień / długość_tekstu)
    plt.xscale('log')
    plt.yscale('log')  
    plt.plot(y)
    plt.title(f'Częstość wystąpień {len(wyrazy)} wyrazów\nw książce {KSIĄŻKA}')
    plt.show()


def zadanie_6_stworz_wykres_pokrycia_wyrazow(wyrazy):
    plt.xscale('log')
    plt.yscale('linear')
    y = [0]
    for wyraz in wyrazy.most_common():
        i = len(y) - 1
        czestosc = wyraz[1] + y[i]
        y.append(czestosc)
    plt.plot(y)
    plt.title(f'Pokrycie tekstu przez {len(wyrazy)} wyrazów\nw książce {KSIĄŻKA}')
    plt.show()


def zadanie_8_stworz_wykres_czestosci_form_podstawowych(wyrazy, długość_tekstu):
    plt.xscale('log')
    plt.yscale('log')
    formy = znajdz_formy_podstawowe(wyrazy)

    y = [0]
    for _, ile_wystapien in formy.most_common():
        y.append(ile_wystapien / długość_tekstu)

    plt.title(f'Częstość wystąpień {len(formy)} form podstawowych\nw książce {KSIĄŻKA}')
    plt.plot(y)
    plt.show()


def zadanie_8_stworz_wykres_pokrycia_form_podstawowych(wyrazy):
    plt.xscale('log')
    plt.yscale('linear')
    formy = znajdz_formy_podstawowe(wyrazy)
    y = [0]
    for wyraz in formy.most_common():
        i = len(y) - 1
        czestosc = wyraz[1] + y[i]
        y.append(czestosc)

    plt.title(f'Pokrycie tekstu przez {len(formy)} form podstawowych\nw książce {KSIĄŻKA}')
    plt.plot(y)
    plt.show()


def main():
    wypisz_skrajne_znaki_wyrazów(KSIĄŻKA)

    # TU(5): zaprogramować zliczanie wystąpień poszczególnych
    # wyrazów w kolekcji `wyrazy` typu `collections.Counter`
    # oraz zliczanie sumarycznej liczby wyrazów w zmiennej
    # `długość_tekstu` typu liczbowego.
    wyrazy, długość_tekstu = zlicz_wyrazy(KSIĄŻKA)

    # TU(5): wypisać 10 najczęstszych wyrazów i ich częstość.
    zadanie_5_wypisz_najczestsze_wyrazy(wyrazy, długość_tekstu)


    # Rysujemy podwójnie logarytmiczny wykres częstości
    # wystąpień wyrazów, od najczęstszego do najrzadszych.
    zadanie_5_stworz_wykres_czestosci_wyrazow(wyrazy, długość_tekstu)

    # TU(6): narysować półlogarytmiczny wykres pokrycia tekstu
    # przez wyrazy. N-ty element tablicy `y` ma być równy sumie
    # częstości wyrazów od najczęstszego do N-tego pod względem
    # malejącej częstości.
    zadanie_6_stworz_wykres_pokrycia_wyrazow(wyrazy)

    # TU(8): zaprogramować zliczanie wystąpień form podstawowych
    # wyrazów w kolekcji `formy` typu `collections.Counter`
    # i rysowanie wykresów częstości ich wystąpień oraz pokrycia
    # przez nie tekstu.
    zadanie_8_stworz_wykres_czestosci_form_podstawowych(wyrazy, długość_tekstu)
    zadanie_8_stworz_wykres_pokrycia_form_podstawowych(wyrazy)


if __name__ == '__main__':
    main()

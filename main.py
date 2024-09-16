class Narzedzia:
    @staticmethod
    def licz_samogloski(tekst: str) -> int:
        samogloski = ['a','ą','e','ę','i','o','u','ó','y','A','Ą','E','Ę','I','O','U','Ó','Y']
        licznik = 0
        if tekst is None:
            return licznik

        for litera in tekst:
            if litera in samogloski:
                licznik += 1
        return licznik

    @staticmethod
    def usun_powtorzenia(tekst: str) -> str:
        if tekst is None or len(tekst) == 0:
            return ''
        wynik = ''
        for i in range(len(tekst)):
            if i == len(tekst) - 1:
                wynik += tekst[i]
            elif tekst[i] != tekst[i+1]:
                wynik += tekst[i]

        return wynik


if __name__ == '__main__':
    tekst = input("dodaj tekst")
    print(f'Liczba samoglosek: {Narzedzia.licz_samogloski(tekst)}')
    print(f'tekst bez powtorzen: {Narzedzia.usun_powtorzenia(tekst)}')

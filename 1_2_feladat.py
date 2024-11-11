nevek = []

folytat = True

def a():
    print("Kérlek adj meg neveket, ha nem szeretnél többet megadni üss egy ENTER-t.")
    while folytat:
        print(len(nevek))
        if len(nevek) >= 2:
            print("Nincs lehetőséged több név megadására!")
            break
        nev_hozzaadas = input("Név: ")
        nevek.append(nev_hozzaadas)

    print(", ".join(nevek)) 



def b():
    hanyadik = 1
    nev_szam = int(input("Kérlek add meg, hogy hány nevet szeretnél megadni! "))
    for i in range(nev_szam):
        nev = input(f"Kérlek add meg a(z) {hanyadik}. nevet! ")
        nevek.append(nev)
        hanyadik = hanyadik + 1
    print(", ". join(nevek))

b()

#2.1, 2.2 feladat házi
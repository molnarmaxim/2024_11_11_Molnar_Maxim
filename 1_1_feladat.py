nevek = []

folytat = True

print("Kérlek adj meg neveket, ha nem szeretnél többet megadni üss egy ENTER-t.")
while folytat:
    nev_hozzaadas = input("Név: ")
    if len(nevek) >= 3:
        print("Nincs lehetőséged több név megadására!")
        break
    nevek.append(nev_hozzaadas)

print(nevek) 
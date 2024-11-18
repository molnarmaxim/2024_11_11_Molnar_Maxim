szavak = []

print("Adj meg 'a' vagy 'A' betűvel kezdődő szavakat!")
print("Akkor ér véget a ciklus, ha üresen nyomsz Enter-t.")

while True:
    szo = input("Adj meg egy szót: ")
    if szo == "":
        print("Üres bevitel, a ciklus leáll.")
        break
    if szo[0].lower() == 'a':
        szavak.append(szo)
    else:
        print(f"A '{szo}' szó nem a-val vagy A-val kezdődik, nem tároljuk.")

print("\nA tárolt szavak:")
for szo in szavak:
    print(szo)

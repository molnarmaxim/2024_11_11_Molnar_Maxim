honapok = ['január',
           'február',
           'március',
           'április',
           'május',
           'június',
           'július',
           'augusztus',
           'szeptember',
           'október',
           'november',
           'december'
]

print(*honapok, sep=", ")

#lista hossza: len()
print(len(honapok))

#0. indexű elem kiírása
print(honapok[0])


#1. indexű elem kiírása
print(honapok[1])

#üres lista létrehozása
szamok = []
print(f"Számok lista tartalma: {szamok}")
#elem hozzáadása
for i in range(1, 11):
    szamok.append(i) #append-del hozzáadunk elemeket
print(f"Számok lista tartalma: {szamok}")

print(szamok[2])

#print(szamok[10]) #List index out of range error

#Utolsó elem kilistázása
print(szamok[-1]) 
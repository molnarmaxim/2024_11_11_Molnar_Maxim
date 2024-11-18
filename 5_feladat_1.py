szinek = ['piros', 'kék', 'zöld', 'sárga', 'lila', 'fekete', 'fehér']

szin_bekero = input('Kérlek adj meg egy színt! ')

# if szin_bekero in szinek:
#     print("Ez a szín már a listában van")
# else:
#     print("Ez a szín nincs a listában")
#     hozzadas = input(f"{szin_bekero} nevű színt hozzá szeretnéd adni?")
#     if hozzadas.lower() == "y":
#         szinek.append(szin_bekero)
#         print(f"{szin_bekero} szín hozzáadva")
#         print(", ". join(szinek))
#     else:
#         print("Szín nincs hozzáadva!")

if szin_bekero in szinek: 
    szinek.remove(szin_bekero)
else: print(f"Nincs a listában ilyen elem: {szin_bekero}")
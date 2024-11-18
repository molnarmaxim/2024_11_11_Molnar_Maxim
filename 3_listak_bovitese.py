nyelvek = ["Python", "C", "C++", "Java", "Python"]

nyelvek.append("Python")

nyelvek_masolat = nyelvek.copy()

nyelvek_honlapkesziteshez = ["HTML", "CSS", "JavaScript"]
nyelvek.extend(nyelvek_honlapkesziteshez)
print(nyelvek)

nyelvek.insert(1, 'Go')
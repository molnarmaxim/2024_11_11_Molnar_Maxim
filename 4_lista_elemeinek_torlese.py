nyelvek = ["Sigma", "Skibidi", "C++", "Python", "JavaScript", 'Kotlin', 'Vue', 'Java']

nyelvek.pop()
torolt_nyelv = nyelvek.pop()
print(f"Törölt nyelv: {torolt_nyelv}")
print(nyelvek)

nyelvek.pop(1)
print(nyelvek)

del nyelvek[1]
print(nyelvek)

nyelvek.remove('Python')
print(nyelvek)

nyelvek.clear()
print(nyelvek)
import string

with open("tekst.txt", "w") as fajl:
  for i in range(10):
    fajl.write(f"{i}, {string.ascii_uppercase[i]}")

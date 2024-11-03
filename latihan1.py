from random import random
n = int(input("Masukkan nilai n: "))

bilangan_acak = []

while len(bilangan_acak) < n:
    bilangan = random()
    if bilangan < 0.5:
        bilangan_acak.append(bilangan)
      
for angka in bilangan_acak:
    print(angka)

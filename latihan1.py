from random import random

n = int(input("Masukkan nilai N: "))

i = 1

while i <= n:
    bilangan_acak = random()
    
    if bilangan_acak < 0.5:
        print(f"data ke: {i} => {bilangan_acak}")
        i += 1

print("Selesai")

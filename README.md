# Praktikum-3 

Nama : Tiara Hayatul Khoir

Kelas : TI.24.A.5

NIM : 312410474

Mata Kuliah : Bahasa Pemrograman

## Latihan 1 | Penjelasan Alur Pemrograman
```Python
from random import random
```
Baris ini mengimpor fungsi `random()` dari modul `random`.
```Python
n = int(input("Masukkan nilai n: "))
```
Program meminta pengguna untuk memasukkan nilai `n`, yaitu jumlah bilangan acak yang ingin dihasilkan. Nilai yang dimasukkan oleh pengguna dikonversi menjadi tipe data integer.
```Python
bilangan_acak = []
```
Program menginisialisasi daftar kosong yang akan digunakan untuk menyimpan bilangan acak yang dihasilkan.
```Python
while len(bilangan_acak) < n:
    bilangan = random()
    if bilangan < 0.5:
        bilangan_acak.append(bilangan)
```
Loop `while` akan terus berjalan selama panjang daftar `bilangan_acak` kurang dari `n`.

Di dalam loop, fungsi `random()` digunakan untuk menghasilkan bilangan acak antara 0 dan 1.

Jika bilangan acak yang dihasilkan kurang dari 0.5, bilangan tersebut ditambahkan ke dalam daftar `bilangan_acak`.

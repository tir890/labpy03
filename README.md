# Praktikum-3 

Nama : Tiara Hayatul Khoir

Kelas : TI.24.A.5

NIM : 312410474

Mata Kuliah : Bahasa Pemrograman

## Latihan 1 | Penjelasan Alur Pemrograman
```Python
from random import random
```
Kode ini mengimpor fungsi `random` dari modul `random` di Python. Fungsi ini digunakan untuk menghasilkan bilangan acak antara 0 dan 1.
```Python
n = int(input("Masukkan nilai N: "))
```
Program meminta pengguna untuk memasukkan nilai `N`, yaitu jumlah bilangan acak yang ingin dibangkitkan. Nilai ini diubah menjadi integer agar bisa digunakan dalam perulangan nanti.
```Python
i = 1
```
Variabel `i` diinisialisasi dengan nilai `1`. Variabel ini berfungsi sebagai penghitung jumlah bilangan acak yang sudah dibangkitkan dan ditampilkan. Nantinya, variabel ini akan bertambah setiap kali program berhasil membangkitkan bilangan acak yang memenuhi syarat.
```Python
while i <= n:
```
Loop `while` dimulai dan akan terus berjalan selama `i` masih lebih kecil atau sama dengan `n`. Ini memastikan program membangkitkan `n` bilangan acak yang sesuai kriteria.
```Python
bilangan_acak = random()
```
Di dalam loop `while`, program memanggil fungsi `random()` untuk menghasilkan bilangan acak dan menyimpannya dalam variabel `bilangan_acak`.
```Python
if bilangan_acak < 0.5:
```
Baris ini memeriksa apakah `bilangan_acak` yang dibangkitkan kurang dari 0.5. Hanya bilangan acak yang kurang dari 0.5 yang akan diproses lebih lanjut.
```Python
print(f"data ke: {i} => {bilangan_acak}")
```
Jika syarat `bilangan_acak < 0.5` terpenuhi, program mencetak nilai bilangan_acak beserta indeks keberapa bilangan tersebut dibangkitkan `(i)`.
```Python
i += 1
```
Setelah bilangan acak yang valid ditampilkan, variabel i ditambah 1 agar perhitungan bilangan acak berikutnya sesuai dengan urutan yang diinginkan. Hal ini juga mendekatkan program ke kondisi berhenti while.
```Python
print("Selesai")
```
Setelah loop selesai (yaitu setelah `n` bilangan acak kurang dari 0.5 telah dibangkitkan dan ditampilkan), program mencetak "Selesai" untuk menunjukkan bahwa proses telah berakhir.

# Hasil Kode Program
![foto](https://github.com/tir890/foto/blob/7943a555c3945c20549c04d2ce88de152da6426b/Screenshot%202024-11-03%20142206.png)

## Latihan 2 | Penjelasan Alur Pemrograman







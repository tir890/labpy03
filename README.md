![image](https://github.com/user-attachments/assets/621e67e8-2ac5-4bd9-8091-c958cbe77d71)# Praktikum-3 

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

## Hasil Kode Program
![foto](https://github.com/tir890/foto/blob/7943a555c3945c20549c04d2ce88de152da6426b/Screenshot%202024-11-03%20142206.png)

## Latihan 2 | Penjelasan Alur Pemrograman
```Python
modal_awal = 100_000_000
```
Variabel `modal_awal` diset ke 100.000.000, yang merupakan modal awal.
```Python
laba_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]
```
List `laba_bulan` menyimpan persentase laba setiap bulan. Setiap angka dalam list ini merepresentasikan persentase laba bulan ke-1 hingga bulan ke-8 dalam bentuk desimal. Misalnya, `0.01` mewakili laba 1% dan `0.05` mewakili laba 5%.
```Python
modal = modal_awal
```
Variabel `modal` diset dengan nilai `modal_awal` (100.000.000) sebagai nilai awal yang akan bertambah sesuai dengan laba per bulan.
```Python
for i, persentase_laba in enumerate(laba_bulan):
    laba_bulan_ini = modal * persentase_laba
    modal += laba_bulan_ini
    print(f"laba bulan ke{i+1}: sebesar {persentase_laba*100}% -> Total modal: Rp{modal:,.0f}")
```
Kode ini menggunakan perulangan `for` dengan `enumerate` untuk mengakses setiap elemen dalam `laba_bulan` bersama indeksnya.

•	`i` adalah indeks bulan (dimulai dari 0, sehingga `i+1` akan memberi angka bulan yang sebenarnya).

•	`persentase_laba` adalah nilai persentase laba pada bulan tersebut.

•	`laba_bulan_ini = modal * persentase_laba` menghitung laba untuk bulan saat ini.

•	`modal += laba_bulan_ini` menambahkan laba bulan ini ke modal.

•	`print(f"laba bulan ke{i+1}: sebesar {persentase_laba*100}% -> Total modal: Rp{modal:,.0f}")` mencetak persentase laba dan total modal setelah laba ditambahkan.
```Python
print(f"\nTotal modal pada akhir bulan ke-8: Rp{modal:,.0f}")
```
Setelah perulangan selesai, total modal pada akhir bulan ke-8 dicetak.

## Hasil Kode Program
![foto](https://github.com/tir890/foto/blob/7f5aa233871ecb301642eb367f117a18a08878c2/Screenshot%202024-11-03%20152435.png)

## Latihan 3 | Penjelasan Alur Pemrograman
```Python
saldo = 1000000
```
Kode ini menginisialisasi variabel `saldo` dengan nilai awal sebesar 1.000.000. Ini akan menjadi jumlah uang yang tersedia untuk ditarik.
```Python
while True:
```
Kode ini memulai sebuah loop yang akan terus berjalan hingga dipecahkan dengan perintah `break`. Ini memungkinkan pengguna untuk melakukan beberapa penarikan tanpa harus memulai program dari awal.
```Python
print(f"\nSaldo saat ini: Rp{saldo}")
```
Pada setiap iterasi loop, saldo saat ini akan ditampilkan kepada pengguna.
```Python
print("1. Tarik Tunai")
print("2. Keluar")
```
Kode ini menampilkan dua pilihan menu kepada pengguna: untuk menarik uang atau keluar dari program.
```Python
pilihan = int(input("Pilih menu (1/2): "))
```
Pengguna diminta untuk memasukkan pilihan mereka (1 untuk menarik tunai atau 2 untuk keluar). Input ini diubah menjadi tipe integer.
```Python
if pilihan == 1:
    jumlah = int(input("Masukkan jumlah penarikan: Rp"))
    if jumlah <= saldo:
        saldo -= jumlah
        print(f"Penarikan berhasil. Sisa saldo Anda: Rp{saldo}")
    else:
        print("Saldo Anda tidak mencukupi!")
```
• Pengguna diminta untuk memasukkan jumlah uang yang ingin ditarik.
• Program memeriksa apakah jumlah penarikan kurang dari atau sama dengan saldo yang tersedia.
• Jika ya, saldo akan dikurangi dengan jumlah penarikan, dan pesan keberhasilan ditampilkan.
•	Jika tidak, pesan bahwa saldo tidak mencukupi ditampilkan.


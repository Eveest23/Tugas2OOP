from no1 import Bilangan
from no2 import PersegiPanjang
from no3 import Segitiga

while True:
    print("Menu Program:")
    print("1. Soal Nomor 1")
    print("2. Soal Nomor 2")
    print("3. Soal Nomor 3")

    pilihan = input("Masukkan pilihan anda(1-3): ")
    if pilihan == "1":
        n = int(input('Masukkan jumlah bilangan: '))
        bilangan = Bilangan(n)
        bilangan.tampil_bilangan()
        print("output disimpan di dalam file output.txt \n")
    elif pilihan == "2":
        p = int(input('Masukkan panjang persegi panjang: '))
        l = int(input('Masukkan lebar persegi panjang: '))
        persegiPanjang = PersegiPanjang(p, l)
        persegiPanjang.hitung_luas()
        print('Output disimpan di dalam file output.txt \n')
    elif pilihan == "3":
        alas = int(input('Masukkan alas segitiga: '))
        tinggi = int(input('Masukkan tinggi segitiga: '))
        segitiga = Segitiga(alas, tinggi)
        segitiga.hitung_luas()
        print('\nOutput disimpan di dalam file output.txt \n')
    else:
        print("Pilihan tidak ada")

    ulangi = input("Apakah anda ingin mengulangi program? (y/n): ")
    if ulangi.lower() != "y":
        break





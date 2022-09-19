#KELOMPOK D
#Nama Anggota:
#1. Dede Ridwan (H1A020033)
#2. Arsil Kultura Anzil (H1A20051)
#3. Muhammad Putra Yubiksana (H1A020059)

i = int(input("Masukan Nilai Anda: "))
if(i <= 60):
    print("Grade Nilai Anda C")
    print("Anda Belum Lulus")
elif(61 <= i < 80):
    print("Grade Nilai Anda B")
    print("Anda Sudah Lulus")
elif(i >= 80):
    print("Grade Nilai Anda A")
    print("Anda Lulus Dengan Hasil Memuaskan")
else:
    print("Anda Salah Memasukan Input")
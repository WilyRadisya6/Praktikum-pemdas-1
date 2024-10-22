#Program gaji bersih

#Proses input gaji pokok, dan total karyawan oleh user
gaji_pokok = int(input("Masukkan gaji pokok :"))
total_karyawan = int(input("Masukkan total karyawan"))

#Deklarasi
t=0.2
p=0.1

#Proses perhitungan
tunjangan = gaji_pokok*t 
pajak = gaji_pokok*p
gaji_bersih = gaji_pokok+tunjangan-pajak
total_gaji = gaji_bersih*total_karyawan

#output nilai total gaji, tunjangan dan pajak karyawan
print("total karyawan :",total_karyawan)
print("total gaji : Rp",total_gaji)
print("pajak per karyawan : Rp",pajak)
print("tunjangan per karyawan : Rp",tunjangan)

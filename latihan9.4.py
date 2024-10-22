nama_wily = "Wily"
umur_wily = 20
program_studi_wily = "Sistem Informasi"
jenis_kelamin_wily = "Laki-laki"
tinggi_wily = 170
kelas_wily = "SI-1A"
lulus_wily = False

nama_wily = "Wily"
umur_wily = 20
tinggi_wily =  170
kelas_wily = "SI-1A"
lulus_wily = True

print("Nama:", nama_wily)
print("umur:", umur_wily, "tahun")
print("Tinggi Badan:", tinggi_wily, "cm")
print("Program Studi:", program_studi_wily)
print("Kelas:", kelas_wily)
print("Jenis Kelamin:", jenis_kelamin_wily)

if lulus_wily:
    print("Status: Alumni")
else:
    print("Status: Mahasiswa aktif")
alas_wily = float(input("masukan alas jajaran genjang"))
tinggi_wily = float(input("masukan tinggi jajaran genjang"))
sisi_a_wily = float(input("masukan nilai sisi a: "))
sisi_b_wily = float(input("masukan nilai sisi b: "))

#Menghitung luas dan keliling jajaran genjang 
luas = (alas_wily * tinggi_wily) 
keliling = 2 * (sisi_a_wily + sisi_b_wily)

print("luas jajaran genjang adalah: ", luas, "cm")
print("keliling jajaran genjang adalah: ", keliling, "cm")
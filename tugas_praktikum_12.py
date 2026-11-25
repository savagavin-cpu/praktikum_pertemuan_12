import math

# menghitung luas persegi panjang 
def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil

# menghitung volume persegi panjang
def volume_persegi_panjang(panjang, lebar, tinggi):
    hasil = panjang * lebar * tinggi
    return hasil

# menghitung luas lingkaran
def luas_lingkaran(jari_jari, pi=math.pi):
    hasil = pi * (jari_jari ** 2)
    return hasil

# menghitung volume bola
def volume_bola(jari_jari, pi=math.pi):
    hasil = (4/3) * pi * (jari_jari ** 3)
    return hasil

# input output
print("=== PROGRAM MENGHITUNG BANGUN DATAR & RUANG ===")

# Input Persegi Panjang
print("\n1. Persegi Panjang / Balok")
p = float(input("Masukkan panjang : "))
l = float(input("Masukkan lebar   : "))
t = float(input("Masukkan tinggi  : "))

luas_pp = luas_persegi_panjang(p, l)
vol_pp = volume_persegi_panjang(p, l, t)

print(f"Hasil Luas Persegi Panjang   = {luas_pp}")
print(f"Hasil Volume Persegi Panjang = {vol_pp}")

# Input Lingkaran & Bola
print("\n2. Lingkaran & Bola")
r = float(input("Masukkan jari-jari : "))

luas_ling = luas_lingkaran(r)
vol_bola = volume_bola(r)

print(f"Hasil Luas Lingkaran = {luas_ling:.2f}")
print(f"Hasil Volume Bola    = {vol_bola:.2f}")

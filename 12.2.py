# Program 12.2 fungsi dengan argumen
#def nama_fungsi (argumen)
#    badan fungsi

def hello_world(nama):
    #fungsi hello world menerima
    print(f"selamat datang di dunia, {nama}")

hello_world("ucup")

def tambah(angka_1, angka_2):
    # fungsi tambah
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,8)
def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"selamat datang {peserta}")

kumpulan_mahasiswa = ["budi", "tono", "joko"]

say_hi(kumpulan_mahasiswa)
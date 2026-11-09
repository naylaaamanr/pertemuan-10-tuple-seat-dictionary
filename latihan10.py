# pertemuan-10-tuple-seat-dictionary
#latihan tuple, set, dan dictionary
#tuple
#no 1 a
mahasiswa =("Nayla Amanatur Rochmah", "2605060063","Teknologi Informasi")
#no 1 b
print("NIM : ",mahasiswa[1])
print("prodi : ",mahasiswa[2])
#no 1 c
#error terjadi karena tuple bersifat immutable, sehingga tidak bisa diubah
#no 1 d
nilai_angka = (10,4,3,2,4,10,7,5)
print("set nilai_angka : ",set(nilai_angka))

#Manipulasi dictionary
#no 2 a membuat dictionary
data_mahasiswa = {
    "nim":"240101",
    "nama":"Budi Santoso",
    "prodi":"Teknologi Informasi"
}
#no 2 b mengubah prodi
data_mahasiswa["prodi"]="Sastra Mesin"
data_mahasiswa["angkatan"]="2026"
# no 2 c menghapus nim dan menampilkan data akhir
del data_mahasiswa["nim"]
print("Data mahasiswa setelah menghapus NIM:")
print(data_mahasiswa)

#no 3 perulangan pada dictionary
# a buat dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000,
}
total_belanja = 0
# b perulangan untuk menampilkan setiap barang dan harganya
print("---Daftar Belanja---")
for buah, harga in keranjang.items():
    print(f"{buah}: Rp {harga}")
    total_belanja += harga
#c tampilkan total belanja
print("---Total Belanja---")
print("Total belanja: Rp", total_belanja)

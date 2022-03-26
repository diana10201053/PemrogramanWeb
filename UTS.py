class Student:
    jumlah_student = 0
    jumlah_berat   = 0
    jumlah_umur    = 0

    def __init__(self, nama, umur, tinggi, berat, jenis_kelamin):
        self.nama          = nama
        self.umur          = umur
        self.tinggi        = tinggi
        self.berat         = berat
        self.jenis_kelamin = jenis_kelamin
        
        Student.jumlah_student += 1

    def tampil(self):
        print("Nama          :", self.nama)
        print("Umur          :", self.umur)
        print("Tinggi        :", self.tinggi)
        print("Berat         :", self.berat)
        print("Jenis Kelamin :", self.jenis_kelamin)

    def Belajar(self):
        print("Mahasiswa yang sedang belajar Pemrograman Berbasis Objek adalah", self.nama)

    def Membaca(self):
        print("Mahasiswa yang sedang membaca buku PBO di perpustakaan adalah ", self.nama)

    def Berdiri(self):
        print("Mahasiswa yang sedang berdiri di samping meja bulat adalah", self.nama)

    def Berjalan(self):
        print("Mahasiswa yang sedang berjalan menuju kantin untuk makan adalah ", self.nama)

    def JumlahBB(self):
        print("Jumlah Berat Badan Seluruh Mahasiswa adalah ", self.berat)
    
    def JumlahUmur(self):
        print("Jumlah Umur Seluruh Mahasiswa adalah ", self.umur)
        
#Menambah Student (VARIABEL)
Student1 = Student("Mardiana", "19 Tahun", "150 cm", "51 kg", "Perempuan")
Student2 = Student("Dedi", "24 Tahun", "160 cm", "59kg", "Laki-Laki")
Student3 = Student("Erick", "26 Tahun", "168 cm", "57 kg", "Perempuan")

#METHOD BELAJAR
Student1.Belajar()
#METHOD MEMBACA
Student2.Membaca()
#METHOD BERDIRI
Student3.Berdiri()
#METHOD BERJALAN
Student1.Berjalan()
#METHOD JUMLAH BERAT BADAN
Student2.JumlahBB()
#METHOD JUMLAH UMUR
Student3.JumlahUmur()
print("\n")

#Print Hasil Seluruh Siswa
print("Mahasiswa Kelas A Pemrograman Berbasis Objek (PBO)")

print("Mahasiswa Pertama")
Student1.tampil()
print("\n")

print("Mahasiswa Kedua")
Student2.tampil()
print("\n")

print("Mahasiswa Ketiga")
Student3.tampil()
print("\n")

print("Jumlah Mahasiswa   : ", Student.jumlah_student, "Mahasiswa")
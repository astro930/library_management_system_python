# /===== Data Model =====/
# Example data model buku
data_buku = [
        {"id_buku": 1, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "penerbit": "Bentang Pustaka", "tahun": "2005", "kategori": "Inspiratif", "status": "Ada"},
        {"id_buku": 2, "judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer","penerbit": "Hasta Mitra", "tahun": "1980", "kategori": "Fiksi", "status": "Terlambat"},
        {"id_buku": 3, "judul": "Cantik Itu Luka", "penulis": "Eka Kurniawan","penerbit": "Gramedia Pustaka Utama", "tahun": "2002", "kategori": "Realisme", "status": "Dipinjam"},
        {"id_buku": 4, "judul": "Negeri 5 Menara", "penulis": "Akhmad Fuadi","penerbit": "Gramedia Pustaka Utama", "tahun": "2009", "kategori": "Inspiratif", "status": "Ada"},
        {"id_buku": 5, "judul": "Hujan", "penulis": "Tere Liye","penerbit": "Gramedia Pustaka Utama", "tahun": "2016", "kategori": "Fiksi", "status": "Ada"}
] 
# Example data model peminjaman
data_peminjaman = [
        {"id_pinjam": 1001, "id_siswa": "12001", "id_buku":1,"judul_buku":"Laskar Pelangi","tanggal_pinjam":"10-09-2026", "durasi_pinjam": 5,"tanggal_kembali": "15-09-2026","status": "Kembali"},
        {"id_pinjam": 1002, "id_siswa": "12001", "id_buku":2,"judul_buku":"Laskar Pelangi","tanggal_pinjam":"10-09-2026", "durasi_pinjam": 5,"tanggal_kembali": "15-09-2026","status": "Kembali"},
        {"id_pinjam": 1003, "id_siswa": "12002", "id_buku":2,"judul_buku":"Laskar Pelangi","tanggal_pinjam":"10-09-2026", "durasi_pinjam": 5,"tanggal_kembali": "15-09-2026","status": "Terlambat"},
        {"id_pinjam": 1004, "id_siswa": "12003", "id_buku":3,"judul_buku":"Laskar Pelangi","tanggal_pinjam":"10-09-2026", "durasi_pinjam": 5,"tanggal_kembali": "15-09-2026","status": "Berhasil"},
        {"id_pinjam": 1004, "id_siswa": "12003", "id_buku":4,"judul_buku":"Laskar Pelangi","tanggal_pinjam":"10-09-2026", "durasi_pinjam": 5,"tanggal_kembali": "15-09-2026","status": "Request Approval"}
]
# Example data model user
data_user = [
        {"nim": "10001", "nama": "admin", "jurusan": "librarian", "password": "admin001","status":"Aktif"},
        {"nim": "12001", "nama": "Boby", "jurusan": "Sastra", "password": "boby001", "status":"Aktif"},
        {"nim": "12002", "nama": "Anton", "jurusan": "Biologi", "password": "anton001", "status":"Aktif"},
        {"nim": "12003", "nama": "Sinta", "jurusan": "Kimia", "password": "sinta001", "status":"Aktif"}
]

# /===== Feature Program =====/
# Create your feature program here
def menu(user):
    """Fungsi untuk menampilkan menu"""
    admin = ("""
        === MENU UTAMA ===

    1. Tambah Buku Baru
    2. Update Data Buku
    3. Hapus Buku
    4. Approve pinjaman
    5. Lihat/Cari Data Buku
    6. Lihat/Cari Data User
    7. Lihat/Cari Data Peminjaman
    8. Exit Library
    """)
    siswa = ("""
        === MENU UTAMA ===
        
    1. Cari dan Pinjam Buku
    2. Lihat History Peminjaman
    3. Exit Library
    """)
    list_menu = {"admin": admin, "siswa": siswa}
    return list_menu[user]

def show_data(listdata):
    """Fungsi untuk menampilkan hasil pencarian dalam bentuk tabel"""
    header = list(listdata[0])
    isi_baris = ""
    char_qty =[]
    print_header = ""
    for item in header:
        if header.index(item) == 0:
            char_qty.append(10)
        elif header.index(item) == 1:
            char_qty.append(30)
        else:
            char_qty.append(25)
        print_header += (item.ljust(char_qty[header.index(item)]) + "|")
    strip = (sum(char_qty)+len(char_qty))//2
    print("- "*strip)
    print(print_header)
    print("- "*strip)
    for item1 in listdata:
        for item2 in header:
            isi_baris += str(str((item1[item2])).ljust(char_qty[header.index(item2)]) + "|")
        print(isi_baris)
        isi_baris = ""
    print("- "*strip)

def search(list,type,key1,key2,key3,indeks):
    """Fungsi untuk melakukan pencarian data"""
    while True:
        print(f"""Opsi Pencarian {type}:
        1. {key2} {type}
        2. Keyword {key1}
        3. Status
        4. Tampilkan semua data {type}
    """)
        opsi = input(f"Masukkan {key2} {type} atau Keyword {key1} untuk mencari {type} (1,2,3,atau 4): ")
        found = "no"
        index = 0
        found_book = []
        if opsi == "1":
            if (list == data_buku) or (list == data_peminjaman):
                cari_id = int(input(f"{key2} {type}".ljust(20)+":"))
            else:
                cari_id = input(f"{key2} {type}".ljust(20)+":")
            for item in list:
                if item[f"{indeks}"] == cari_id:
                    found = "yes"
                    found_book.append(item)
        elif opsi == "2":
            cari_keyword = input(f"Keyword {key1}".ljust(20)+":")
            for item in list:
                if cari_keyword.lower() in item[f"{key1}"].lower():
                    found = "yes"
                    found_book.append(item)
        elif opsi == "3":
            cari_status = input(f"Status {type}".ljust(20)+":")
            for item in list:
                if cari_status.lower() in item[f"{key3}"].lower():
                    found = "yes"
                    found_book.append(item)
        elif opsi == "4":
            found = "all"
        else:
            print("Pilihan tidak sesuai !")
        if found == "no":
            print(f"Pencarian tidak ditemukan, ulangi input {key2}/Keyword!")
            continue
        else:
            if found == "all":
                print(f"\nBerikut daftar seluruh {type}: \n")
                show_data(list)
            else:
                print(f"\nPencarian berhasil, berikut daftar {type} sesuai pencarian: \n")
                show_data(found_book)
            while True: 
                cari_lagi = input("\nUlangi pencarian? ketik 'ya' atau 'tidak': ").lower()
                if cari_lagi == "ya":
                    search(list,type,key1,key2,key3,indeks)
                elif cari_lagi == "tidak":
                    break
                else:
                    print("Respon tidak sesuai !")
                    continue
                break
            break


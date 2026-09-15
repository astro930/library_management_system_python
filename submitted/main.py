# ===================================
# [LIBRARY MANAGEMENT SYSTEM]
# ===================================
# Developed by. Astro Lihardo Aloysius
# JCDS - [34]
# /************************************/

# Import data, functions from other file
from add_utilities import data_buku, data_peminjaman, data_user
from add_utilities import menu, show_data, search
from datetime import datetime,timedelta

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    # Ucapan pembuka sistem
    print("\n=== PERPUSTAKAAN KAMPUS NUSANTARA ===\n")

    # login atau daftar anggota baru
    print("Untuk melakukan peminjaman, silahkan login terlebih dahulu atau lakukan pendaftaran jika belum menjadi member!")
    
    while True:
        print("1. Login\n2. Daftar Member\n")
        login_or_daftar = input("Masukkan pilihan (1 atau 2): ")
        if login_or_daftar == "2":
            print("\n"*20)
            print("== PENDAFTARAN SISWA ==")
            print("\nMasukkan data siswa berikut: ")
            while True:
                nim = input("- NIM / NIK (5 digit, diawali 1)  : ")
                check = "ok"
                for data in data_user:
                    if data["nim"] == nim:
                        check = "terdaftar"
                if check =="ok":
                    if (nim.isdigit()) and (nim[0] == "1") and (len(nim)) == 5:
                        nama = input   ("Nama Lengkap                    : ")
                        jurusan = input("Jurusan/pekerjaan               : ")
                        password = input("Create password (8 karakter)   : ")
                        data_user.append({"nim": nim, "nama": nama, "jurusan": jurusan, "password": password})
                        print("Pendaftaran Berhasil, Anda sudah menjadi member! ")
                        print("Silahkan melakukan login !\n")
                        break
                    else:
                        print("Masukkan NIM/NIK yang sesuai !")
                        continue
                else:
                    print("NIM/NIK sudah terdaftar, silakan login !")
                    break

        elif login_or_daftar == "1":
            print("\n"*20)
            print("== LOGIN ==")
            print("\n")
            repeat_login = 3
            while True:
                enter_library = "no"
                nim = input("Masukkan NIM / NIK (5 digit, diawali 1)  : ")
                password = input("Masukkan password anda ( 8 karakter): ")
                for data in data_user:
                    if data["nim"] == nim and data["password"] == password:
                        enter_library = "yes"
                        break

                if enter_library == "no":
                    print(f"Input NIM/NIK / password gagal, masukkan input yang sesuai ({repeat_login-1}/3),")
                    repeat_login -= 1
                    if repeat_login == 0:
                        print("Silakan menghubungi admin untuk bantuan !")
                        break
                    else:
                        continue
                else:
                    if nim == "10001":
                        while True:
                            print("\n"*20)
                            print(menu("admin"))
                            pilih_menu = input("Masukkan nomor menu: ")
                            if pilih_menu == "1":
                                while True:
                                    print("\n"*20)
                                    print("== TAMBAH BUKU BARU == ")
                                    print("\n")
                                    """Function for create the data
                                        """
                                    print("Masukkan data buku baru: ")
                                    judul = input("Judul".ljust(15)+":").capitalize()
                                    penulis = input("Penulis".ljust(15)+":").capitalize()
                                    penerbit = input("Penerbit".ljust(15)+":").capitalize()
                                    tahun = input("Tahun".ljust(15)+":")
                                    kategori = input("Kategori".ljust(15)+":").capitalize()
                                    next_index = 0
                                    for book in data_buku:
                                        if book["id_buku"] > next_index:
                                            next_index = book["id_buku"]
                                    data_buku.append({"id_buku": next_index + 1, "judul": judul, "penulis": penulis, "penerbit": penerbit, "tahun": tahun, "kategori": kategori, "status": "Ada"})
                                    print("\nData buku baru berhasil ditambahkan :\n")
                                    show_data(data_buku)
                                    opsi = input("\nTambahkan data buku lain atau kembali ke menu utama? (tambah/kembali): ").lower()
                                    if opsi == "tambah":
                                        continue
                                    else:
                                        break
                            elif pilih_menu == "2":
                                while True:
                                    print("\n"*20)
                                    print("== UPDATE DATA BUKU ==")
                                    print("\n")
                                    """Function for update the data
                                        """
                                    search(data_buku,"Buku","judul","ID","status","id_buku")
                                    pilih_buku = int(input("Masukkan ID buku yang ingin diupdate: "))
                                    perubahan =[]
                                    print("Masukkan input update atau tekan enter untuk input update berikutnya !")
                                    judul = input("Judul".ljust(15)+":").capitalize()
                                    penulis = input("Penulis".ljust(15)+":").capitalize()
                                    penerbit = input("Penerbit".ljust(15)+":").capitalize()
                                    tahun = input("Tahun".ljust(15)+":")
                                    kategori = input("Kategori".ljust(15)+":").capitalize()
                                    status = input("Status".ljust(15)+":").capitalize()
                                    perubahan.append({"id_buku": pilih_buku, "judul": judul, "penulis": penulis, "penerbit": penerbit, "tahun": tahun, "kategori": kategori, "status": status})
                                    print("Berikut adalah summary update: ")
                                    show_data(perubahan)
                                    print("""
                                        1. Simpan update
                                        2. Ulangi update
                                        3. Kembali ke menu utama
                                    """)
                                    confirm = input("Silakan pilih opsi di atas (1,2, atau 3): ")
                                    if confirm == "1":
                                        for item in data_buku:
                                            if item["id_buku"] == pilih_buku:
                                                if judul != "":
                                                    item["judul"] = judul
                                                if penulis != "":
                                                    item["penulis"] = penulis
                                                if penerbit != "":
                                                    item["penerbit"] = penerbit
                                                if tahun != "":
                                                    item["tahun"] = tahun
                                                if kategori != "":
                                                    item["kategori"] = kategori
                                                if status != "":
                                                    item["status"] = status
                                        print("\nUpdate berhasil disimpan !\n")
                                        break
                                    elif confirm == "2":
                                        continue
                                    elif confirm == "3":
                                        break
                                    else:
                                        print("Pilihan tidak tersedia")
                                        break
                            elif pilih_menu == "3":
                                while True:
                                    print("\n"*20)
                                    print("== HAPUS BUKU ==")
                                    print("\n")
                                    """Function for delete the data
                                        """
                                    search(data_buku,"Buku","judul","ID","status","id_buku")
                                    pilih_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
                                    print("""
                                        1. Confirm Penghapusan Buku
                                        2. Ulangi Penghapusan Buku
                                        3. Kembali ke menu utama
                                    """)
                                    confirm = input("Silakan pilih opsi di atas (1,2, atau 3): ")
                                    if confirm == "1":
                                        for item in data_buku:
                                            if item["id_buku"] == pilih_buku:
                                                data_buku.remove(item)
                                                print("\nBuku Berhasil dihapus !")
                                                break
                                    elif confirm == "2":
                                        continue
                                    elif confirm == "3":
                                        break
                                    else:
                                        print("Pilihan tidak tersedia")
                                        break     
                            elif pilih_menu == "4":
                                while True:
                                    print("\n"*20)
                                    print("== APPROVAL PEMINJAMAN ==")
                                    print("\n")
                                    search(data_peminjaman,"Peminjaman","judul_buku","ID","status","id_pinjam")
                                    pilih_peminjaman = int(input("Masukkan ID peminjaman yang ingin diapprove " \
                                    "atau ketik '0' untuk kembali ke menu utama: "))
                                    if pilih_peminjaman == 0:
                                        break
                                    else:
                                        temp_list =[]
                                        id_pinjam = 0
                                        id_siswa = ""
                                        id_buku = 0
                                        judul_buku = ""
                                        tanggal_pinjam = ""
                                        durasi_pinjam = 0
                                        tanggal_kembali = ""
                                        print("Masukkan status approval !")
                                        for item in data_peminjaman:
                                            if item["id_pinjam"] == pilih_peminjaman:
                                                id_pinjam = item["id_pinjam"]
                                                id_siswa  = item["id_siswa"]
                                                id_buku = item["id_buku"]
                                                judul_buku = item["judul_buku"]
                                                tanggal_pinjam = item["tanggal_pinjam"]
                                                durasi_pinjam = item["durasi_pinjam"]
                                                tanggal_kembali = item["tanggal_kembali"]
                                                durasi_pinjam =item["durasi_pinjam"]
                                        status = input("Approval Status".ljust(20)+":").capitalize()
                                        temp_list.append({"id_pinjam": id_pinjam, "id_siswa": id_siswa, "id_buku":id_buku,"judul_buku":judul_buku,"tanggal_pinjam":tanggal_pinjam, "durasi_pinjam": durasi_pinjam ,"tanggal_kembali": tanggal_kembali,"status": status})
                                        print("\nBerikut adalah summary approval: ")
                                        show_data(temp_list)
                                        print("""
                                            1. Konfirmasi update
                                            2. Ulangi konfirmasi
                                            3. Kembali ke menu utama
                                        """)
                                        confirm = input("Silakan pilih opsi di atas (1,2, atau 3): ")
                                        if confirm == "1":
                                            for item in data_peminjaman:
                                                if item["id_pinjam"] == pilih_peminjaman:
                                                    item["status"] = status
                                            print("\nKonfirmasi berhasil disimpan !")
                                            break
                                        elif confirm == "2":
                                            continue
                                        elif confirm == "3":
                                            break
                                        else:
                                            print("Pilihan tidak tersedia")
                                            break
                                        
                            elif pilih_menu == "5":        
                                while True:
                                    print("\n"*20)
                                    print("== LIHAT/CARI DATA BUKU ==")
                                    print("\n")
                                    """Function for read the data
                                        """
                                    search(data_buku,"Buku","judul","ID","status","id_buku")
                                    print("""
                                        1. Lihat/Cari data buku lainnya
                                        2. Kembali ke menu utama
                                    """)
                                    choice = input("Silakan pilih opsi di atas (1 atau 2): ")
                                    if choice == "1":
                                        continue
                                    elif choice == "2":
                                        break
                                    else:
                                        print("Pilihan tidak tersedia")
                                        break     
                            elif pilih_menu == "6":        
                                while True:
                                    print("\n"*20)
                                    print("== LIHAT/CARI DATA USER ==")
                                    print("\n")
                                    """Function for read the data
                                        """
                                    search(data_user,"User","nama","NIM","status","nim")
                                    print("""
                                        1. Lihat/Cari data user lainnya
                                        2. Kembali ke menu utama
                                    """)
                                    choice = input("Silakan pilih opsi di atas (1 atau 2): ")
                                    if choice == "1":
                                        continue
                                    elif choice == "2":
                                        break
                                    else:
                                        print("Pilihan tidak tersedia")
                                        break
                            elif pilih_menu == "7":        
                                while True:
                                    print("\n"*20)
                                    print("== LIHAT/CARI DATA PEMINJAMAN ==")
                                    print("\n")
                                    """Function for read the data
                                        """
                                    search(data_peminjaman,"Peminjaman","judul_buku","ID","status","id_pinjam")
                                    print("""
                                        1. Lihat/Cari data user lainnya
                                        2. Kembali ke menu utama
                                    """)
                                    choice = input("Silakan pilih opsi di atas (1 atau 2): ")
                                    if choice == "1":
                                        continue
                                    elif choice == "2":
                                        break
                                    else:
                                        print("Pilihan tidak tersedia")
                                        break    
                            elif pilih_menu == "8":
                                print("Terima kasih atas kunjungannya, Sampai jumpa lagi !")
                                break
                            else:
                                print("Pilihan tidak tersedia !")
                                continue
                        break
                    else:
                        while True:
                            print(menu("siswa"))
                            pilih_menu = input("Masukkan nomor menu: ")
                            if pilih_menu == "1":
                                while True:
                                    print("\n"*20)
                                    print("== LIHAT/CARI DATA BUKU ==")
                                    print("\n")
                                    search(data_buku,"Buku","judul","ID","status","id_buku")
                                    print("""
                                        1. Lihat/Cari data buku lainnya
                                        2. Request Peminjaman Buku
                                        3. Kembali ke menu utama
                                    """)
                                    choice = input("Silakan pilih opsi di atas (1 atau 2): ")
                                    if choice == "1":
                                        continue
                                    elif choice == "2":
                                        while True:
                                            print("\n"*20)
                                            print("== PEMINJAMAN BUKU == ")
                                            print("\n")
                                            print("Masukkan request peminjaman buku: ")
                                            id_siswa = input("id_siswa".ljust(20)+":").capitalize()
                                            id_buku = int(input("id_buku".ljust(20)+":"))
                                            tanggal_pinjam = input("Tanggal_pinjam (dd-mm-yyyy)".ljust(20)+":").capitalize()
                                            start_date = datetime.strptime(tanggal_pinjam, "%d-%m-%Y")
                                            durasi_pinjam = int(input("Durasi Pinjam (day)".ljust(20)+":"))
                                            end_date = start_date + timedelta(days=durasi_pinjam)
                                            tanggal_kembali = end_date.strftime("%d-%m-%Y")
                                            next_index = 0
                                            judul=""
                                            for data in data_peminjaman:
                                                if data["id_pinjam"] > next_index:
                                                    next_index = data["id_pinjam"]
                                            for book in data_buku:
                                                if book["id_buku"] == id_buku:
                                                    judul = book["judul"]
                                            data_peminjaman.append({"id_pinjam": next_index+1, "id_siswa": id_siswa, "id_buku":id_buku,"judul_buku":judul,"tanggal_pinjam":tanggal_pinjam, "durasi_pinjam": durasi_pinjam,"tanggal_kembali": tanggal_kembali,"status": "Reques Approval"})
                                            print("Request Peminjaman berhasil disubmit !")
                                            print("Silahkan konfirmasi admin untuk approval dan pengambilan buku !")
                                            show_data(data_peminjaman)
                                            opsi = input("Tambahkan request buku lain atau kembali ke menu utama? (tambah/kembali): ").lower()
                                            if opsi == "tambah":
                                                continue
                                            else:
                                                break
                                            break

                                    elif choice == "3":
                                        break
                                    else:
                                        print("Pilihan tidak tersedia")
                                        break
                                                                
                            elif pilih_menu == "2":        
                                while True:
                                    print("\n"*20)
                                    print("== LIHAT/CARI DATA PEMINJAMAN ==")
                                    print("\n")
                                    search(data_peminjaman,"Peminjaman","judul_buku","ID","status","id_pinjam")
                                    print("""
                                        1. Lihat/Cari data user lainnya
                                        2. Kembali ke menu utama
                                    """)
                                    choice = input("Silakan pilih opsi di atas (1 atau 2): ")
                                    if choice == "1":
                                        continue
                                    elif choice == "2":
                                        break
                                    else:
                                        print("Pilihan tidak tersedia")
                                        break    
                            elif pilih_menu == "3":
                                print("\n"*20)
                                print("Terima kasih atas kunjungannya, Sampai jumpa lagi !")
                                break
                            else:
                                print("Pilihan tidak tersedia !")
                                continue
                        break
                    break
                break
            break     
        else:
            print("Pilihan tidak tersedia, silakan masukkan pilihan kembali !")
                    
if __name__ == "__main__":
    main()
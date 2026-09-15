## Python CRUD Application for Library Management

A comprehensive Python application for managing LIBRARY inventory data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

Project ini merupakan sistem management perpustakaan yang mengelola proses peminjaman dan penyimpanan buku. Sistem ini akan digunakan oleh siswa untuk melakukan pengecekan ketersediaan buku dan melakukan peminjaman. Sistem ini juga digunakan oleh admin untuk melakukan penambahan, pembaharuan, dan penghapusan informasi. Sistem ini juga dapat digunakan oleh admin untuk melakukan pemberitahuan keterlambatan pengembalian buku yang dipinjam.

**Benefits:**

* Membantu siswa melakukan pengecekan ketersediaan buku dan melakukan peminjaman secara online
* Membantu admin perpustakaan dalam melakukan merekam transaksi peminjaman dan melakukan notifikasi pengembalian bagi siswa yang terlambat mengembalikan buku

**Target Users:**

Aplikasi ini diperuntukkan untuk manager dan admin perpustakaan untuk memaintain ketersediaan buku serta siswa yang ingin melakukan peminjaman buku.

## Features
* **Create:**
    * Menambahkan transaksi peminjaman buku oleh siswa, lengkap dengan detail transaksinya seperti judul buku, tanggal pinjam, lama peminjaman
    * Menambahkan inventory buku baru mencakup judul, penulis, penerbit, tahun terbit, kategori
    * Implementasi validasi untuk memastikan akurasi data
* **Read:**
    * Mencari dan mengambil informasi spesifik dari buku yang dipinjam: ID, judul, penerbit, kategory
    * Menampilkan detail produk dengan tampilan user friendly
* **Update:**
    * Mengupdate atribut buku oleh admin: judul buku, penulis, penerbit, tahun penerbitan, kategori
    * Memberikan konfirmasi terhadap proses update : berhasil atau tidak berhasil
* **Delete:**
    * Menghapus data buku yang sudah rusak atau hilang atau sudah diganti versi terbaru
* **Reporting:**
    * Generate report dari inventori level, status peminjaman, keperluan penambahan buku

## Installation

1. **Prerequisites:**
    * Python version 3.7 or later
    * Additional dependencies:
        * `pip install flask`
        * `pip install sqlalchemy`
        * `pip install psycopg2`  # For connecting to a PostgreSQL database

2. **Installation:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/python-inventory-crud.git
    cd python-inventory-crud
    pip install -r requirements.txt
    ```

3. **Database Setup:**
    * Create a PostgreSQL database and configure the connection details in `config.py`.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new product to the inventory, providing necessary details like name, SKU, and quantity.
    * **Read:** Search for a specific product by name or SKU to view its details and stock level.
    * **Update:** Modify the quantity of a product or update other product details.
    * **Delete:** Remove a discontinued product from the inventory (with authorization).
    * **Reports:** Generate reports on low-stock items or overall inventory levels for analysis.

## Data Model

This project utilizes a relational database (PostgreSQL) to store product information. The following tables are used:

* **Products:**
    * `id` (Integer, Primary Key): Unique identifier for each product.
    * `name` (String): Name of the product.
    * `description` (Text): Detailed product description (optional).
    * `sku` (String, Unique): Stock Keeping Unit for the product.
    * `quantity` (Integer): Current stock level of the product.
    * `reorder_point` (Integer): Minimum stock level before reordering.
    * `category` (String): Category of the product (e.g., electronics, clothing).
    * `image_url` (String, optional): URL for the product image.
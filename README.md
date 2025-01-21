# Implementasi Software Defined Network (SDN) dengan Mininet dan Ryu Controller

## Pendahuluan
Software Defined Network (SDN) adalah pendekatan inovatif dalam pengelolaan jaringan yang memisahkan fungsi kontrol dari perangkat keras fisik. Dengan SDN, network administrator dapat mengatur lalu lintas jaringan melalui software tanpa perlu konfigurasi manual pada perangkat jaringan.

Dalam proyek ini, kita akan mengeksplorasi bagaimana tree topology dapat diimplementasikan dalam lingkungan SDN menggunakan Mininet dan Ryu Controller.

---

## Persyaratan
Sebelum memulai, pastikan sistem Anda memiliki:

- **Sistem Operasi:** Ubuntu/Debian
- **Akses root/admin**
- **Koneksi internet yang stabil**

## Langkah-langkah Instalasi

### 1. Perbarui Paket Sistem
```bash
sudo apt-get update
```
Command ini digunakan untuk memperbarui daftar paket pada sistem agar versi terbaru tersedia.

### 2. Install Python3 dan Pip
```bash
sudo apt-get install python3
sudo apt-get install pip
```
Pip akan digunakan untuk menginstall modul tambahan dari repositori Python (PyPI), seperti Ryu.

### 3. Install Mininet
```bash
sudo apt-get install mininet
```
Mininet memungkinkan simulasi jaringan SDN dalam lingkungan virtual.

### 4. Install Virtual Environment dan Python 3.9
Ryu Controller saat ini belum mendukung Python 3.10, sehingga kita perlu menggunakan Python 3.9 di dalam virtual environment.

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install virtualenv python3.9 python3.9-distutils
```

### 5. Buat dan Aktifkan Virtual Environment
```bash
virtualenv -p `which python3.9` ryu-python3.9-venv
source ryu-python3.9-venv/bin/activate
```
Verifikasi aktivasi dengan:
```bash
echo $VIRTUAL_ENV
```
Jika berhasil, akan muncul direktori virtual environment.

### 6. Install Ryu Controller di Virtual Environment
```bash
pip install ryu
```
Karena ada ketidakcocokan versi eventlet, kita perlu melakukan reinstall dengan versi yang kompatibel:
```bash
pip uninstall eventlet
pip install eventlet==0.30.2
```
Verifikasi instalasi Ryu dengan:
```bash
ryu-manager --help
```

### 7. Clone Repository Ryu dari GitHub
```bash
git clone https://github.com/faucetsdn/ryu.git
```
Repository ini berisi aplikasi controller preset yang dapat digunakan.

---

## Pembuatan Topologi

Sebagai gambaran, kita menggunakan topologi tree yang terdiri dari:

- 1 controller
- 15 switch
- 15 host

Topologi ini dibuat menggunakan bahasa Python dengan nama `initopo.py`.

### 8. Menjalankan Ryu Controller
```bash
cd /path_to_ryu/app/
ryu-manager simple_switch_13.py
```
Jika berhasil, Ryu akan masuk ke mode standby untuk menerima traffic dari SDN.

### 9. Menjalankan Mininet dengan Topologi
```bash
mn --custom initopo.py --controller remote --switch ovsk
```
Jika status menunjukkan "Starting CLI:", artinya Mininet telah berhasil dijalankan.

### 10. Pengujian Konektivitas

- Cek konektivitas antar host dengan:
```bash
pingall
```
- Tampilkan nodes yang ada dengan:
```bash
nodes
```
Jika hasil ping sukses, maka implementasi jaringan berhasil.

### 11. Verifikasi Traffic pada Ryu Controller
Kembali ke terminal Ryu untuk melihat traffic yang diterima dan paket data yang diteruskan berdasarkan ARP table.

---

## Kesimpulan
Dengan mengikuti langkah-langkah di atas, kita telah berhasil:

1. Menginstall dan mengkonfigurasi lingkungan SDN menggunakan Mininet dan Ryu Controller.
2. Membuat dan menjalankan topologi jaringan dalam lingkungan virtual.
3. Menguji konektivitas dan memastikan komunikasi antar host berjalan dengan baik.

---

## Referensi
- [Ryu SDN Framework](https://github.com/faucetsdn/ryu)
- [Mininet SDN Emulator](http://mininet.org/)

---

## Lisensi
Proyek ini berada di bawah lisensi MIT. Silakan digunakan dan dikembangkan sesuai kebutuhan.

---

Terima kasih telah menggunakan panduan ini!


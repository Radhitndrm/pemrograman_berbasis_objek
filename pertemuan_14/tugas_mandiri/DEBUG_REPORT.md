
# DEBUG REPORT – Bug PPN 10%

## Informasi Umum

* Modul: `diskon_service.py`
* Class: `DiskonCalculator`
* Method: `hitung_diskon`
* Tools Debugging: `pdb` (Python Debugger)

---

## Deskripsi Bug

Pada fungsi `hitung_diskon`, ditemukan bug berupa **penambahan PPN 10% secara tidak sengaja** pada harga setelah diskon. Hal ini menyebabkan hasil perhitungan harga akhir menjadi lebih besar dari yang diharapkan dan mengakibatkan beberapa unit test gagal.

---

## Langkah-Langkah Debugging

### 1. Menambahkan Breakpoint

Breakpoint ditambahkan pada awal fungsi `hitung_diskon` menggunakan perintah:

```python
import pdb
pdb.set_trace()
```

---

### 2. Menjalankan Unit Test

Unit test dijalankan dengan perintah:

```bash
python -m unittest
```

Eksekusi program berhenti pada breakpoint yang telah ditentukan.

---

### 3. Pemeriksaan Nilai Variabel (pdb)

Dilakukan inspeksi variabel menggunakan perintah `p` di dalam mode pdb.

```text
(pdb) p harga_awal
1000

(pdb) p persentase_diskon
10

(pdb) p jumlah_diskon
100.0

(pdb) p harga_setelah_diskon
900.0

(pdb) p ppn
90.0

(pdb) p harga_akhir
990.0
```

---

## Analisis

* Nilai `harga_setelah_diskon` sudah benar, yaitu **900.0**
* Variabel `ppn` bernilai **90.0**, yaitu 10% dari harga setelah diskon
* `harga_akhir` menjadi **990.0**, padahal sesuai spesifikasi seharusnya **900.0**

Hal ini membuktikan bahwa **PPN 10% ditambahkan secara tidak sengaja**, sehingga harga dihitung lebih dari yang diharapkan.

---

## Kesimpulan

Bug disebabkan oleh adanya perhitungan dan penambahan PPN 10% yang **tidak termasuk dalam spesifikasi fungsi** `hitung_diskon`.

---

## Solusi

Menghapus seluruh logika perhitungan PPN dari fungsi `hitung_diskon`, sehingga fungsi hanya bertanggung jawab menghitung harga setelah diskon.

---

## Status Setelah Perbaikan

* Bug PPN berhasil dihilangkan
* Seluruh unit test (`test_diskon.py` dan `test_diskon_advanced.py`) **LULUS (OK)**

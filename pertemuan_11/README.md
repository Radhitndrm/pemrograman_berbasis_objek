# Analisis SOLID Principles (SRP, OCP, DIP)

Readme ini menganalisis pelanggaran prinsip **SOLID** pada kode *sebelum refactor* serta menjelaskan bagaimana refactor memperbaikinya.

---

## 1. Single Responsibility Principle (SRP)

**Prinsip:**
Sebuah kelas seharusnya hanya memiliki **satu tanggung jawab** dan satu alasan untuk berubah.

### ❌ Pelanggaran (Sebelum Refactor)

Kelas `OrderManager` memiliki banyak tanggung jawab sekaligus:

* Mengatur alur checkout
* Menentukan metode pembayaran
* Memproses pembayaran
* Mengirim notifikasi ke pelanggan
* Mengubah status order

Seluruh logika tersebut berada di dalam satu method `process_checkout()`.
Jika salah satu aspek berubah (misalnya metode notifikasi), maka kelas ini ikut berubah, sehingga melanggar SRP.

### ✅ Perbaikan (Sesudah Refactor)

Tanggung jawab dipisahkan ke dalam beberapa komponen:

* `IPaymentProcessor` → menangani pembayaran
* `INotificationService` → menangani notifikasi
* `CheckoutService` → mengoordinasikan proses checkout

Setiap kelas kini memiliki satu tanggung jawab yang jelas.

---

## 2. Open/Closed Principle (OCP)

**Prinsip:**
Perangkat lunak harus **terbuka untuk ekstensi** namun **tertutup untuk modifikasi**.

### ❌ Pelanggaran (Sebelum Refactor)

Pemilihan metode pembayaran menggunakan struktur `if/elif`:

```python
if payment_method == "credit_card":
elif payment_method == "bank_transfer":
elif payment_method == "qris":
```

Untuk menambahkan metode pembayaran baru, kode yang sudah ada harus dimodifikasi, sehingga melanggar OCP.

### ✅ Perbaikan (Sesudah Refactor)

Setiap metode pembayaran diimplementasikan sebagai class tersendiri:

* `CreditCardProcessor`
* `BankTransferProcessor`
* `QRISProcessor`

Untuk menambah metode baru, cukup membuat class baru yang mengimplementasikan `IPaymentProcessor` tanpa mengubah kode existing.

---

## 3. Dependency Inversion Principle (DIP)

**Prinsip:**

* Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah
* Keduanya harus bergantung pada **abstraksi**

### ❌ Pelanggaran (Sebelum Refactor)

`OrderManager` bergantung langsung pada:

* Detail metode pembayaran
* Implementasi notifikasi (menggunakan `print`)

Ketergantungan langsung pada detail ini menyebabkan kode sulit diuji, sulit diperluas, dan memiliki *tight coupling*.

### ✅ Perbaikan (Sesudah Refactor)

`CheckoutService` bergantung pada abstraksi:

* `IPaymentProcessor`
* `INotificationService`

Implementasi konkretnya di-*inject* melalui constructor (*Dependency Injection*), sehingga:

* Kode lebih fleksibel
* Mudah diuji (mocking)
* Low coupling dan high cohesion

---

## Kesimpulan

Refactor yang dilakukan berhasil:

* Menghilangkan kelas dengan banyak tanggung jawab (*God Class*)
* Mengurangi kompleksitas `if/else`
* Menerapkan *Dependency Injection*
* Membuat kode lebih **scalable**, **testable**, dan **maintainable**

Implementasi setelah refactor telah memenuhi prinsip **SRP, OCP, dan DIP** dengan baik serta mencerminkan praktik *Clean Architecture*.

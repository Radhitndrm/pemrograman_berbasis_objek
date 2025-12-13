from abc import ABC, abstractmethod


# ==================================================
# ABSTRAKSI VALIDATION RULE (DIP)
# ==================================================
class IValidationRule(ABC):
    """
    Interface untuk semua rule validasi
    Setiap rule hanya fokus pada 1 jenis validasi (SRP)
    """

    @abstractmethod
    def validate(self, data):
        pass


# ==================================================
# RULE VALIDASI SKS (SRP)
# ==================================================
class SksLimitRule(IValidationRule):
    """
    Bertanggung jawab hanya untuk validasi batas SKS
    """

    def __init__(self, max_sks):
        self.max_sks = max_sks

    def validate(self, data):
        if data["total_sks"] > self.max_sks:
            return False, f"SKS melebihi batas {self.max_sks}"
        return True, "SKS OK"


# ==================================================
# RULE VALIDASI PRASYARAT (SRP)
# ==================================================
class PrerequisiteRule(IValidationRule):
    """
    Bertanggung jawab hanya untuk validasi prasyarat matakuliah
    """

    def validate(self, data):
        missing = [
            req for req in data["prasyarat"]
            if req not in data["matkul_yang_sudah_diambil"]
        ]

        if missing:
            return False, f"Prasyarat belum terpenuhi: {missing}"

        return True, "Prasyarat OK"


# ==================================================
# RULE VALIDASI JADWAL (SRP)
# ==================================================
class JadwalBentrokRule(IValidationRule):
    """
    Bertanggung jawab hanya untuk validasi bentrok jadwal
    """

    def validate(self, data):
        seen = set()

        for jam in data["jadwal"]:
            if jam in seen:
                return False, f"Jadwal bentrok pada {jam}"
            seen.add(jam)

        return True, "Jadwal OK"


# ==================================================
# SERVICE KOORDINATOR VALIDASI (DIP)
# ==================================================
class RegistrationService:
    """
    Mengatur proses validasi
    Tidak bergantung pada rule konkret (DIP)
    """

    def __init__(self, rules: list[IValidationRule]):
        self.rules = rules

    def validate_registration(self, data):
        """
        Menjalankan semua rule tanpa tahu detail implementasinya
        """
        results = []

        for rule in self.rules:
            status, message = rule.validate(data)
            results.append(
                (rule.__class__.__name__, status, message)
            )

        return results


# ==================================================
# CHALLENGE – PEMBUKTIAN OCP
# Tambah rule BARU TANPA mengubah kode lama
# ==================================================
class SemesterAktifRule(IValidationRule):
    """
    Rule baru: validasi apakah mahasiswa masih semester aktif
    (Bukti OCP: extend tanpa modify)
    """

    def validate(self, data):
        if not data["semester_aktif"]:
            return False, "Mahasiswa tidak dalam semester aktif"
        return True, "Semester aktif OK"


# ==================================================
# CONTOH PENGGUNAAN
# ==================================================
rules = [
    SksLimitRule(24),
    PrerequisiteRule(),
    JadwalBentrokRule(),
    SemesterAktifRule(),  # Rule baru ditambahkan (OCP)
]

service = RegistrationService(rules)

data = {
    "total_sks": 22,
    "prasyarat": ["MatkulA", "MatkulB"],
    "matkul_yang_sudah_diambil": ["MatkulA"],
    "jadwal": ["Senin-07", "Senin-09", "Senin-07"],
    "semester_aktif": True,
}

hasil = service.validate_registration(data)

for h in hasil:
    print(h)

import logging
from abc import ABC, abstractmethod

# ==================================================
# KONFIGURASI LOGGING
# ==================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ==================================================
# ABSTRAKSI VALIDATION RULE (DIP)
# ==================================================
class IValidationRule(ABC):
    """Interface untuk semua rule validasi.

    Setiap rule harus mengimplementasikan method validate()
    dan hanya bertanggung jawab pada satu jenis validasi (SRP).
    """

    @abstractmethod
    def validate(self, data: dict) -> tuple[bool, str]:
        """Melakukan validasi terhadap data registrasi.

        Args:
            data (dict): Data registrasi mahasiswa.

        Returns:
            tuple[bool, str]: Status validasi dan pesan hasil validasi.
        """
        pass


# ==================================================
# RULE VALIDASI SKS (SRP)
# ==================================================
class SksLimitRule(IValidationRule):
    """Rule untuk memvalidasi batas maksimal SKS mahasiswa."""

    def __init__(self, max_sks: int):
        """Inisialisasi batas maksimal SKS.

        Args:
            max_sks (int): Batas maksimal SKS.
        """
        self.max_sks = max_sks

    def validate(self, data: dict) -> tuple[bool, str]:
        """Memvalidasi apakah total SKS melebihi batas.

        Args:
            data (dict): Data registrasi mahasiswa.

        Returns:
            tuple[bool, str]: Status dan pesan validasi.
        """
        if data["total_sks"] > self.max_sks:
            logger.warning("SKS melebihi batas maksimum.")
            return False, f"SKS melebihi batas {self.max_sks}"

        logger.info("Validasi SKS berhasil.")
        return True, "SKS OK"


# ==================================================
# RULE VALIDASI PRASYARAT (SRP)
# ==================================================
class PrerequisiteRule(IValidationRule):
    """Rule untuk memvalidasi prasyarat mata kuliah."""

    def validate(self, data: dict) -> tuple[bool, str]:
        """Memeriksa apakah semua prasyarat telah dipenuhi.

        Args:
            data (dict): Data registrasi mahasiswa.

        Returns:
            tuple[bool, str]: Status dan pesan validasi.
        """
        missing = [
            req for req in data["prasyarat"]
            if req not in data["matkul_yang_sudah_diambil"]
        ]

        if missing:
            logger.warning("Prasyarat belum terpenuhi.")
            return False, f"Prasyarat belum terpenuhi: {missing}"

        logger.info("Validasi prasyarat berhasil.")
        return True, "Prasyarat OK"


# ==================================================
# RULE VALIDASI JADWAL (SRP)
# ==================================================
class JadwalBentrokRule(IValidationRule):
    """Rule untuk memvalidasi bentrok jadwal perkuliahan."""

    def validate(self, data: dict) -> tuple[bool, str]:
        """Memeriksa apakah terdapat jadwal bentrok.

        Args:
            data (dict): Data registrasi mahasiswa.

        Returns:
            tuple[bool, str]: Status dan pesan validasi.
        """
        seen = set()
        for jam in data["jadwal"]:
            if jam in seen:
                logger.warning("Terdapat bentrok jadwal.")
                return False, f"Jadwal bentrok pada {jam}"
            seen.add(jam)

        logger.info("Validasi jadwal berhasil.")
        return True, "Jadwal OK"


# ==================================================
# SERVICE KOORDINATOR VALIDASI (DIP)
# ==================================================
class RegistrationService:
    """Service untuk mengoordinasikan proses validasi registrasi.

    Service ini bergantung pada abstraksi (IValidationRule),
    bukan implementasi konkret (DIP).
    """

    def __init__(self, rules: list[IValidationRule]):
        """Inisialisasi service dengan daftar rule validasi.

        Args:
            rules (list[IValidationRule]): Daftar rule validasi.
        """
        self.rules = rules

    def validate_registration(self, data: dict) -> list[tuple[str, bool, str]]:
        """Menjalankan seluruh rule validasi terhadap data registrasi.

        Args:
            data (dict): Data registrasi mahasiswa.

        Returns:
            list[tuple[str, bool, str]]: Hasil validasi tiap rule.
        """
        results = []

        logger.info("Memulai proses validasi registrasi.")
        for rule in self.rules:
            status, message = rule.validate(data)
            results.append((rule.__class__.__name__, status, message))

        logger.info("Proses validasi registrasi selesai.")
        return results


# ==================================================
# CHALLENGE – BUKTI OCP
# ==================================================
class SemesterAktifRule(IValidationRule):
    """Rule untuk memvalidasi status semester aktif mahasiswa."""

    def validate(self, data: dict) -> tuple[bool, str]:
        """Memeriksa apakah mahasiswa berada di semester aktif.

        Args:
            data (dict): Data registrasi mahasiswa.

        Returns:
            tuple[bool, str]: Status dan pesan validasi.
        """
        if not data["semester_aktif"]:
            logger.warning("Mahasiswa tidak dalam semester aktif.")
            return False, "Mahasiswa tidak dalam semester aktif"

        logger.info("Validasi semester aktif berhasil.")
        return True, "Semester aktif OK"

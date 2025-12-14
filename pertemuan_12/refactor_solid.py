
import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod

# ======================
# KONFIGURASI LOGGING
# ======================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


@dataclass
class Order:
    """Merepresentasikan data pesanan pelanggan.

    Attributes:
        customer_name (str): Nama pelanggan.
        total_price (float): Total harga pesanan.
        status (str): Status pesanan (default: "Open").
    """
    customer_name: str
    total_price: float
    status: str = "Open"


class OrderManager:
    """Mengelola proses checkout pesanan (sebelum refactor).

    Class ini menangani proses pembayaran dan notifikasi
    secara langsung dalam satu method.
    """

    def process_checkout(self, order: Order, payment_method: str) -> bool:
        """Memproses checkout pesanan berdasarkan metode pembayaran.

        Args:
            order (Order): Objek pesanan pelanggan.
            payment_method (str): Metode pembayaran yang digunakan.

        Returns:
            bool: True jika checkout berhasil, False jika gagal.
        """
        logger.info("Memulai checkout untuk %s", order.customer_name)

        if payment_method == "credit_card":
            logger.info("Memproses pembayaran dengan kartu kredit")
        elif payment_method == "bank_transfer":
            logger.info("Memproses pembayaran dengan transfer bank")
        elif payment_method == "qris":
            logger.info("Memproses pembayaran dengan QRIS")
        else:
            logger.warning("Metode pembayaran tidak dikenal: %s", payment_method)
            return False

        logger.info("Mengirim notifikasi ke %s", order.customer_name)
        order.status = "paid"
        logger.info("Checkout selesai")
        return True


# ============================================================
#  SESUDAH REFACTOR
# ============================================================

class IPaymentProcessor(ABC):
    """Abstraksi untuk pemrosesan pembayaran."""

    @abstractmethod
    def process(self, order: Order) -> bool:
        """Memproses pembayaran pesanan.

        Args:
            order (Order): Objek pesanan.

        Returns:
            bool: True jika pembayaran berhasil.
        """
        pass


class INotificationService(ABC):
    """Abstraksi untuk layanan notifikasi."""

    @abstractmethod
    def send(self, order: Order):
        """Mengirim notifikasi terkait pesanan.

        Args:
            order (Order): Objek pesanan.
        """
        pass


class CreditCardProcessor(IPaymentProcessor):
    """Pemroses pembayaran menggunakan kartu kredit."""

    def process(self, order: Order) -> bool:
        """Memproses pembayaran kartu kredit."""
        logger.info("Memproses pembayaran kartu kredit")
        return True


class BankTransferProcessor(IPaymentProcessor):
    """Pemroses pembayaran menggunakan transfer bank."""

    def process(self, order: Order) -> bool:
        """Memproses pembayaran transfer bank."""
        logger.info("Memproses pembayaran transfer bank")
        return True


class QRISProcessor(IPaymentProcessor):
    """Pemroses pembayaran menggunakan QRIS."""

    def process(self, order: Order) -> bool:
        """Memproses pembayaran QRIS."""
        logger.info("Memproses pembayaran QRIS")
        return True


class EmailNotifier(INotificationService):
    """Layanan notifikasi melalui email."""

    def send(self, order: Order):
        """Mengirim notifikasi email kepada pelanggan."""
        logger.info("Mengirim notifikasi email ke %s", order.customer_name)


class CheckoutService:
    """Service inti untuk menjalankan proses checkout.

    Class ini hanya bertanggung jawab mengorkestrasi
    proses pembayaran dan notifikasi.
    """

    def __init__(
        self,
        payment_processor: IPaymentProcessor,
        notifier: INotificationService
    ):
        """Menginisialisasi CheckoutService."""
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order) -> bool:
        """Menjalankan proses checkout pesanan.

        Args:
            order (Order): Objek pesanan pelanggan.

        Returns:
            bool: True jika checkout berhasil.
        """
        logger.info("Memulai checkout untuk %s", order.customer_name)

        payment_success = self.payment_processor.process(order)

        if payment_success:
            self.notifier.send(order)
            order.status = "paid"
            logger.info("Checkout selesai")
            return True

        logger.error("Checkout gagal untuk %s", order.customer_name)
        return False

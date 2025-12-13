# ============================================================
#  SEBELUM REFACTOR
# ============================================================

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "Open"


class OrderManager:
    def process_checkout(self, order: Order, payment_method: str):
        print(f"\nMemulai checkout untuk {order.customer_name}...")

        if payment_method == "credit_card":
            print("Memproses pembayaran dengan kartu kredit...")
        elif payment_method == "bank_transfer":
            print("Memproses pembayaran dengan transfer bank...")
        elif payment_method == "qris":
            print("Memproses pembayaran dengan QRIS...")
        else:
            print("Metode pembayaran tidak dikenal.")
            return False

        print(f"Mengirim notifikasi ke {order.customer_name}...")
        order.status = "paid"
        print("Checkout selesai.")
        return True


# ===== DEMO SEBELUM REFACTOR =====
print("========== DEMO SEBELUM REFACTOR ==========")
order_sebelum = Order("Andi", 500000)
manager = OrderManager()
manager.process_checkout(order_sebelum, "credit_card")


# ============================================================
#  SESUDAH REFACTOR
# ============================================================


# ======================
# ABSTRACTION
# ======================

class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass


class INotificationService(ABC):
    @abstractmethod
    def send(self, order: Order):
        pass


# ======================
# IMPLEMENTASI PAYMENT
# ======================

class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Memproses pembayaran dengan kartu kredit...")
        return True


class BankTransferProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Memproses pembayaran dengan transfer bank...")
        return True


class QRISProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Memproses pembayaran dengan QRIS...")
        return True


# ======================
# IMPLEMENTASI NOTIFIKASI
# ======================

class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Mengirim notifikasi email ke {order.customer_name}...")


# ======================
# CORE SERVICE
# ======================

class CheckoutService:
    def __init__(
        self,
        payment_processor: IPaymentProcessor,
        notifier: INotificationService
    ):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order):
        print(f"\nMemulai checkout untuk {order.customer_name}...")
        payment_success = self.payment_processor.process(order)

        if payment_success:
            self.notifier.send(order)
            order.status = "paid"
            print("Checkout selesai.")
            return True

        return False


# ===== DEMO SESUDAH REFACTOR =====
print("\n========== DEMO SESUDAH REFACTOR ==========")

email_service = EmailNotifier()

# Skenario 1: Kartu Kredit
andi_order = Order("Andi", 500000)
checkout_cc = CheckoutService(CreditCardProcessor(), email_service)
checkout_cc.run_checkout(andi_order)

# Skenario 2: QRIS
budi_order = Order("Budi", 10000)
checkout_qris = CheckoutService(QRISProcessor(), email_service)
checkout_qris.run_checkout(budi_order)

# Skenario 3: Bank Transfer
citra_order = Order("Citra", 75000)
checkout_bank = CheckoutService(BankTransferProcessor(), email_service)
checkout_bank.run_checkout(citra_order)

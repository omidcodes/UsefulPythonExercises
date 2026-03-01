# Below is the messy code before SOLID -->
# class OrderService:
#     def __init__(self):
#         self.db = MySQL()
#         self.email = EmailService()

#     def process_order(self, order, payment_type):
#         if payment_type == "card":
#             print("Processing card")
#         elif payment_type == "paypal":
#             print("Processing paypal")

#         self.db.save(order)
#         self.email.send_confirmation(order)


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass()
class Order:
    _id: int
    name: str

# ---------------------- Payment -------------

class Payment(ABC):

    @abstractmethod
    def process(self, order:Order):
        pass

class CardPayment(Payment):

    def process(self, order:Order):
        print(f"Processing order->'{order.name}' using card")

class PaypalPayment(Payment):

    def process(self, order:Order):
        print(f"Processing order->'{order.name}' using paypal")

# ---------------------- Storage -------------

class Storage(ABC):

    @abstractmethod
    def save(self, data):
        pass

class MySQL(Storage):
    def save(self, data):
        print("save to MySQL")


class PostgreSQL(Storage):
    def save(self, data):
        print("save to PostgreSQL")

# ---------------------- Message -------------
class MessageNotifier(ABC):

    @abstractmethod
    def send_confirmation(self, data):
        pass

class EmailNotifier(MessageNotifier):
    def send_confirmation(self, data):
        print("sending Email")

class SMSNotifier(MessageNotifier):
    def send_confirmation(self, data):
        print("sending SMS")

class OrderService:
    def __init__(self, storage: Storage, message_notifier: MessageNotifier, payment: Payment):
        self.storage = storage
        self.message_notifier = message_notifier
        self.payment = payment

    def process_order(self, order: Order):
        self.payment.process(order=order)

        self.storage.save(order)
        self.message_notifier.send_confirmation(order)

order_service = OrderService(storage=MySQL() , message_notifier=SMSNotifier(), payment=PaypalPayment())
order = Order(_id= 10, name="myorder01")
order_service.process_order(order)
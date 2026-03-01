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


# ---------------------- Payment -------------

class Payment(ABC):

    @abstractmethod
    def process(self):
        pass

class CardPayment(Payment):

    def process(self):
        print("Processing card")

class PaypalPayment(Payment):

    def process(self):
        print("Processing paypal")

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

class Email(MessageNotifier):
    def send_confirmation(self, data):
        print("sending Email")

class SMS(MessageNotifier):
    def send_confirmation(self, data):
        print("sending SMS")

class OrderService:
    def __init__(self, order, storage: Storage, message_notifier: MessageNotifier, payment: Payment):
        self.storage = storage
        self.message_notifier = message_notifier
        self.__payment = payment
        self.order = order

    def process_order(self):
        self.__payment.process()

        self.storage.save(self.order)
        self.message_notifier.send_confirmation(self.order)

OrderService(order="myorder01" , storage=MySQL() , message_notifier=Email(), payment=PaypalPayment())
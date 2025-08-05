from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, sender: str, message: str):
        pass


class NotificationSMS(Notification):
    def send(self, sender: str, message: str):
        print(f"SMS from {sender}: {message}")


class NotificationEmail:
    def send(self, sender: str, message: str, subject: str):
        print(f"Email from {sender} with subject {subject}: {message}")


class NotificationEmailAdapter(Notification):
    def __init__(self, notification_email: NotificationEmail, subject: str):
        self.notification_email = notification_email
        self.subject = subject

    def send(self, sender: str, message: str):
        self.notification_email.send(sender, message, self.subject)


def create_order(notification: Notification, sender: str, message: str):
    print("Se crea la orden")
    print("Se factura")
    notification.send(sender, message)


notification_sms = NotificationSMS()

create_order(notification_sms, "13324651869", "Order created")

notification_email = NotificationEmail()
notification_email_adapter = NotificationEmailAdapter(
    notification_email, "About the order"
)

create_order(notification_email_adapter, "13324651869", "Order created")

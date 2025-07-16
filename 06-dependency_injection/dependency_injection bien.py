from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EMailNotification(Notification):
    def __init__(self, user, pwd, url):
        self.user = user
        self.pwd = pwd
        self.url = url

    def send(self, message):
        print(f"Sending email to {self.user} with message: {message}")


class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"Sending SMS to {self.phone_number} with message: {message}")


class NotificationManager:
    def __init__(self, notification: Notification):
        self._notification = notification

    def notify(self, message):
        self._notification.send(message)


email_notification = EMailNotification("usuario", "senha", "http://url")
sms_notification = SMSNotification("123456789")

notification_manager = NotificationManager(email_notification)
notification_manager.notify("Olá, mundo!")

notification_manager = NotificationManager(sms_notification)
notification_manager.notify("Olá, mundo!")
# This code demonstrates the use of dependency injection to allow for flexible notification methods.
# This allows for easier testing and swapping of notification methods without changing the NotificationManager class.

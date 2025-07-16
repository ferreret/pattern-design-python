class EMailNotification:
    def __init__(self, user, pwd, url):
        self.user = user
        self.pwd = pwd
        self.url = url

    def send(self, message):
        print(f"Sending email to {self.user} with message: {message}")


class NotificationManager:
    def __init__(self):
        # Creating a dependency directly
        # This is not ideal for testing or flexibility
        self._notification = EMailNotification("usuario", "senha", "http://url")

    def notify(self, message):
        self._notification.send(message)


notification_manager = NotificationManager()
notification_manager.notify("Olá, mundo!")

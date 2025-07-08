class SMS:
    def send(self):
        print("Sending SMS...")


class Saver:
    def save(self):
        print("Saving data...")


class Email:
    def send(self):
        print("Sending Email...")


class Sale(SMS, Saver, Email):
    pass


sale = Sale()
sale.send()  # This will call the send method from the first class in the MRO (SMS)
sale.save()

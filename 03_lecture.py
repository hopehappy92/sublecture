# class Email:
#     def __init__(self):
#         self.is_sent = 'False'

#     def send_email(self):
#         self.is_sent = 'True'

# my_email = Email()
# print(my_email.is_sent)
# my_email.send_email()
# print(my_email.is_sent)


class Bag:
    def __init__(self):
        self.lst = []
    def add(self, num):
        self.lst.append(num)
    def add_twice(self, num):
        self.lst.append(num)
        self.lst.append(num)
    def data(self):
        return self.lst

bag = Bag()
bag.add(1)
bag.add_twice(5)
print(bag.data())





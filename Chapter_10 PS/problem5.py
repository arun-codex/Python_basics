'''
5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
fare information of train running under Indian Railways.

'''
from random import randint

class Train:

    def __init__(self, TrainNo):
        self.TrainNO = TrainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.TrainNO} from {fro} to {to}.")

    def getStatue(self):
        print(f"Trin no: {self.TrainNO} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is fare in train no: {self.TrainNO} from {fro} to {to} is {randint(222,5555)}")


t = Train(1806)
t.book("Patna", "Delhi")
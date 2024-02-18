class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getInfo(self):
        print("-----------------------------------------------------------------------")
        print(f'''The name of the currently available train is: {self.name}. \nAnd the fair is Rs.{self.fare}.''')

    def getStatus(self):
        print("-----------------------------------------------------------------------")

        print(f"Total seats available in the train is {self.seats}")

    def bookTicket(self):
        print("-----------------------------------------------------------------------")

        if(self.seats>0):
             print("Congratulation! your ticket has been booked.")
             self.seats = self.seats - 1
        else:
                print("Sorry! there are no seats available.")

    def getStatus(self):
       print("-----------------------------------------------------------------------")

       print(f"Total seats available in the train is {self.seats}")


train = Train("HOOL EXPRESS 22013", 110, 2)
train.getInfo()
train.getStatus()
train.bookTicket()
train.getStatus()




"""

Constructors re-used to create and initialize an object of a class with or without
starting values

3 Types of Constructors
    Empty Constructors
    No argument Constructors
    Parameters Constructors

The difference between .__new__() and .__init__() is that .__new__() creates the instance, while .__init__() initializes it.

"""

class Salman:
    # name= "Muhammad Salman"
    # address= "Lahore"
    # degree= "BSCS"

    def __init__(self):
        print('Hi I am a man')

    def info(self):
        print(f'The name is {self.name} and the address is {self.address}, and finally the degree is {self.degree}')

a=Salman()
a.name= "Bunny"
a.address= "Bahria Town"
a.info()
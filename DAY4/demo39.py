class product:
    def display(self):
        '''this is product display list'''
        print("Display - Product details")

class Customer(product):
    def display(self):
        print('Display customer records')
        super().display() # calling parent class method
        
obj = Customer()
obj.display()

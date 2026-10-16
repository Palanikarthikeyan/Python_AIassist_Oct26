class Product:
    pname = 'pA'
    pcost = 1000
    pqty  = 5

class Customer(Product): # Single Inheritance
    cus_id = 'cus-A'
    cus_name = 'Mr.ABC'
    pqty = 10
    QTY = Product.pqty
obj = Customer()
print(obj.pname)
print(obj.pcost)
print(obj.cus_id)
print(obj.cus_name)
print(obj.pqty)
print(obj.QTY)
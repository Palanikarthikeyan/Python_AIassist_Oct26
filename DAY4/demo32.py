fobj = open('C:\\Users\\Karth\\emp.csv','r')
L = fobj.readlines()
fobj.close()
total = 0
for var in L:
    if 'sales' in var:
        cost = var.split(",")[-1]
        total = total + int(cost)

print(f'Sum of sales dept cost is:{total}')
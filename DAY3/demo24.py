fobj = open('C:\\Users\\karth\\emp.csv','r')
L = fobj.readlines()
fobj.close()
for var in L:
    if 'sales' in var:
        print(var.strip()) # display matched pattern lines only
        
# in windows:  findstr sales emp.csv
#              -------
# in Linux: grep sales emp.csv
#           ----
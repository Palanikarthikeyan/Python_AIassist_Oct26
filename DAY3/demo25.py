fobj = open('C:\\Users\\karth\\emp.csv','r')
L = fobj.readlines()
fobj.close()
wobj = open('s1.csv','w')
for var in L:
    if 'sales' in var:
        wobj.write(var) # write data to FILE
        #print(var.strip()) # display matched pattern lines only
        
wobj.close()
# in windows:  findstr sales emp.csv >s1.csv
#              -------
# in Linux: grep sales emp.csv  >s1.csv
#           ----
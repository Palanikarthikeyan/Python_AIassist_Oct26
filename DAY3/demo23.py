fobj = open('C:\\Users\\karth\\emp.csv','r')
s = fobj.read() # str
fobj.close()

print('File emp.csv contents')
print(s)
print(f'Total no.of chars:{len(s)}')

# --------------------
fobj = open('C:\\Users\\karth\\emp.csv','r')
L = fobj.readlines() # list
fobj.close()
print(f"Total no.of lines from emp.csv file: {len(L)}")
for var in L:
    print(var.strip())

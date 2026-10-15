fobj = open('C:\\users\\karth\\emp.csv','r')
L = fobj.readlines()
for var in L[-4:]:  # display last 4 lines
    print(var.strip())
fobj.close()

# again read - r1.log file - display last 3 lines
# ..
# again read - r2.log file - display last 10 lines
#########################################################
def file_read():
    fobj = open('C:\\users\\karth\\emp.csv','r')
    L = fobj.readlines()
    for var in L[-4:]:  # display last 4 lines
        print(var.strip())
    fobj.close()
    
file_read()
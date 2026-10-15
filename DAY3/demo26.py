with open('C:\\Users\\karth\\emp.csv','r') as fobj:
    L = fobj.readlines()
    for var in L:
        var = var.strip()
        eid,ename,edept,eplace,ecost = var.split(",")
        print(f'{ename.title()}  {edept.upper()}')

print('\n End of the line')
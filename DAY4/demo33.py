from functools import reduce
# map(function,collection)->generator
#      |_lambda |_fileContents
'''
print(list(map(lambda a:a,open('C:\\Users\\karth\\emp.csv','r').readlines())))
print('')
print(list(map(lambda a:a.split(","),open('C:\\Users\\karth\\emp.csv','r').readlines())))
print('')
print(list(map(lambda a:a.split(",")[-1],open('C:\\Users\\karth\\emp.csv','r').readlines())))
'''
P1 = filter(lambda a:'sales' in a,open('C:\\Users\\karth\\emp.csv','r').readlines())
P2 = map(lambda a:a.split(",")[-1],P1)
P3 = reduce(lambda a,b:int(a)+int(b),P2)
print(f'Sum of sales dept cost is:{P3}')
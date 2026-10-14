'''
Given List
emp = ['101,raj,sales,pune,1000',
'102,anu,hr,hyderabad,2000',
'103,leo,sales,nodia,3000',
'104,theeb,prod,mumbai,4000']

Iterate a given list - one by one
-> display Emp name in title case
-> display Emp working City in uppercase 
|
->Calculate sum Emp's cost
-> Display total Emp's Cost at the end.
'''
emp = ['101,raj,sales,pune,1000',
'102,anu,hr,hyderabad,2000',
'103,leo,sales,nodia,3000',
'104,theeb,prod,mumbai,4000']

total = 0
for var in emp:
    eid,ename,edept,eplace,ecost = var.split(",")
    print(f'Emp name is: {ename.title()}\t Working City: {eplace.upper()}')
    total = total + float(ecost)
else:
    print("--" * 25)
    print(f"Sum of Emp's Cost is:{total}")
    print("--" * 25)
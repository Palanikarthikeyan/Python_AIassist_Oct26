'''
file_info = [
    'emp.csv:123:2KB:userA',
    'r1.log:321:4KB:userB',
    't1.java:435:3KB:userC',
    'r2.log:345:5KB:userD'
]

'''
import pprint
file_info = [
    'emp.csv:123:2KB:userA',
    'r1.log:321:4KB:userB',
    't1.java:435:3KB:userC',
    'r2.log:345:5KB:userD'
]
d={'fname':[],'findex':[],'fsize':[],'fowner':[]} # dict of list
for var in file_info:
    f,i,s,u = var.split(":")
    d['fname'].append(f)
    d['findex'].append(i)
    d['fsize'].append(s)
    d['fowner'].append(u)

pprint.pprint(d)    
    
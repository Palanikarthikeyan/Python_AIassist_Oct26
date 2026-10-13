'''
write a python program:
using for loop - calculate sum of the digits (given below)
s='123456789'
'''
s = '123456789'
t = 0
for v in s:
    t = t + int(v)

print(f'Sum of {s} is {t}')
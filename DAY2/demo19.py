'''
Write a Python Program:
- create an empty dict
- use while loop - limit 5
    - read a host alias name from <STDIN>(ex: host01)
    - read a host IP address from <STDIN>
    dict key as alias - ip address as value // 
    - add input details to dict
- using for loop - display hostname and IP
|
- read a alias name from <STDIN>
- test - input alias name is exists in dict
                 |-> update IP- 127.0.0.1
       |--not exists -> add input host to an existing dict
                        (value is: 127.0.0.1)
- using pprint.pprint() - display updated dict
'''
import pprint
hosts = {} # empty dict
count = 0
while count < 5:
    k = input('Enter an alias name:')
    v = input(f'Enter {k} IP Address:')
    hosts[k] = v # adding new data to an existing dict
    count += 1
print('Hostname\t IPAddress:')
for var in hosts:
    print(f'{var} - {hosts[var]}')
print('') # empty line
k = input('Enter a hostname:')
if k in hosts:
    hosts[k] = '127.0.0.1'
    print(f'host {k} ip is updated')
else:
    hosts[k] = '127.0.0.1' 
    print(f'host {k} is added to an existing host-dict')

print('Updated dict details:-')
pprint.pprint(hosts)
''''
Write a python program:
create an empty list 
display no.of items 
|
using while loop - limit is 5
       - read a device name from <STDIN>
       - add input device into an existing list # use append()
display no.of items
|
using for loop - display each device details one by one
|
read any device name from <STDIN>
test input device is exists from device_list -> device is found at nth index
                     |
                    Not-exists - add input device to an existing list
                    display updated list items
'''
devices = [] # empty list
print(f'Total no.of devices:{len(devices)}')
c = 0
while(c < 5):
    dname = input('Enter a device name:')
    devices.append(dname) # adding new data to an existing list
    c = c + 1
print(f'\nNow - Total no.of devices:{len(devices)}')
print('List of devices:')
for var in devices:
    print(var)
#-----------------------
d = input('Enter a device name:')
if d in devices:
    print(f'Yes device {d} is exists at {devices.index(d)} index')
else:
    devices.append(d)
    print(f'device {d} is added into existing device list')
    print('Updated device list')
    for var in devices:
        print(var)

print("\n ---- End of the Line -----")
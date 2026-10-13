'''
Write a python program
step 1: initialize a pin number (ex: pin = 1234)
|
step 2: use while loop - limit is 3
           -> read a pinNumber from <STDIN>
           -> test - input pin with an existing pin
           ->          if pin is valid -> Success is pin is matched - <count>
step 3: if all 3 inputs are failed ->pin is blocked
'''
pin = 1234
count = 0
while(count < 3):
    p = input('Enter a pinNumber:')
    count = count + 1
    if(int(p) == pin):
        print(f'Success - pin is matched - {count}')
        break

if(int(p) != pin):
    print('Sorry pin is blocked')

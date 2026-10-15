import time

def pin_test():
    fobj = open('pin_history.log','a') # append mode
    pin = 1234
    count = 0
    while(count < 3):
        count = count + 1
        p = input('Enter a pin Number:')
        if(int(p) == pin):
            fobj.write(f'Success pin is matched - {count}')
            fobj.write(f' Pin entry date/time is:{time.ctime()}\n')
            print(f'Success - pin is matched - {count}')
            break
        else:
            fobj.write(f'Failed - User input pin {p} is not matched')
            fobj.write(f' Pin entry date/time is:{time.ctime()}\n')
    if(int(p) != pin):
        print('Sorry your pin is blocked')
        fobj.write(f'Sorry your pin is blocked - blocked time is:{time.ctime()}\n')
    fobj.close()

pin_test()
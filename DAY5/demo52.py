import logging

logging.basicConfig(
    filename='pin_history.log',
    filemode='a',
    level=logging.INFO,
    format='%(levelname)s %(asctime)s %(message)s',
)

pin = 1234
count = 0
while(count < 3):
    count = count + 1
    p = input('Enter a pin Number:')
    if(int(p) == pin):
        logging.info(f'Success pin is matched - {count}')
        print(f'Success - pin is matched - {count}')
        break
    else:
        logging.warning(f'Failed - User input pin {p} is not matched')

if(int(p) != pin):
    print('Sorry your pin is blocked')
    logging.error('Sorry your pin is blocked')
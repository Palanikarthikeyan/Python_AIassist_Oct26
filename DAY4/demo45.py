try:
    n = input('Enter n value:')
    if(int(n) > 100):
        raise ValueError("n value is above 100")
except Exception as eobj:
    print(eobj)
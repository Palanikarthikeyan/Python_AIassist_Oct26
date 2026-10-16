'''
map()     -> map(function,collection) -> generator 
filter()  -> filter(function,collection) ->  generator
reduce()  -> reduce(function,collection) -> SingleValue
# --- 2.x
# Vs
# ---- 3.x 
# functools.reduce()
'''
print(list(map(lambda a: a>30,[10,20,45,15,55,65])))
print("") # empty line
print(list(filter(lambda a: a>30,[10,20,45,15,55,65])))
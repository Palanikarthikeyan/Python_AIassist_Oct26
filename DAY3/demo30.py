# step - 1 Empty dict
d = {}

# step - 2 File Handling
fobj = open('network.cfg','r')
L = fobj.readlines()
fobj.close()
for var in L:
    var = var.strip() # remove \n
    K,V = var.split("=") # split each line into multiple values 
    d[K] = V # adding new data to dict

# step - 3 display Key - Value
for var in d:
    print(f'{var} - {d[var]}')
print('') # empty line
# step - 4 dict operation
d['Interface'] = "eth1"      # dict modification
d['bootproto'] = 'static'    # dict modification
d['onboot'] = 'yes'          # dict modification
d['IPADDR'] = '192.168.1.10' # dict add operation
d['PREFIX'] = 24             # dict add operation
d['DNS2'] = '122.444.322.111' # dict add operation

# step - 5 display Updated dict details
for var in d:
    print(f'{var} - {d[var]}')
    
# step - 6 create new network config and write updated dict to Config file 
wobj = open('new_network.cfg','w')
for var in d:
    wobj.write(f'{var} = {d.get(var)}\n') # writing data to FILE
wobj.close()
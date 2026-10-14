import pprint

L = [('flask', 'version is 2.34', 5000),
     ('fastAPI', 'version is 1.83', 8000),
     ('streamlit', 'version is 1.34', 5001), 
     ('django', 'versionis 0.92', 8001)]

print(L[1]) # fastAPI details
if L[2][-1] == 5001:
    web_app = L[2][0]
    print("run this application using streamlit command")
else:
    print('Invalid port')
    
L.append(('flask','version 4.3',5002),) # add new data
pprint.pprint(L)
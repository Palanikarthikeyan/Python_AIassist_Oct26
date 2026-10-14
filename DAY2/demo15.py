app_details = []

'''
[flask]   [fastAPI]   [streamlit]   [django]
- port
- config
'''
app_details.append(['flask','version is 2.34',5000])
app_details.append(['fastAPI','version is 1.83',8000])
app_details.append(['streamlit','version is 1.34',5001])
app_details.append(['django','version is 0.92',8001])
print(app_details)
# how to update streamlit port 5001 -> 5002
app_details[2][2] = 5002 # modification
print(app_details)
app_details.append(['web2.0','version is 4.32',9090])
print(app_details)
# How to add fastapi.conf in fastapi list ?
app_details[1].append('fastapi.conf') 
print(app_details)
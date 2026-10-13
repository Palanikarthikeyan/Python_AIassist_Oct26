'''
variable - namespace <or> placeholder 

variableName = value
------------
|->Variable name starts with A-Za-z_ (not starts with digits)
|->Variable name not allows space , specialchars 
'''
port = 5000
print(port) # 5000
#print(PORT)
#print(Port)
# -------------// NameError 
# Task 
# --------
# Write a python program:
# Initialize an app Name , running port number , app version , running status to individual variable
# using print() - display app details
# ------------------------------------------------------------------------------------------------------
# Ex: app name is: TestApp - running port number:1234 version:1.45 status:True
#                  =======                       ====         ====        =====
app_name = 'TestApp'
app_port = 1234
app_version = 1.45
app_status = True
print(app_name)
print(app_port,app_version,app_status)
print("App name is:",app_name) # 1st style
print("App name is:%s"%(app_name)) # 2nd style - extend from C language 
print("App name is:{}".format(app_name)) # 3rd style obj.method()
print(f"App name is:{app_name}")  # 4th style <==
print(f'{app_name} running port number is:{app_port}')
print(f'{app_name} version is:{app_version}')
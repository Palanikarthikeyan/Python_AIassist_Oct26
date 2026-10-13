'''
Write a python program:
-> read an app name from <STDIN>
-> test - input app name is:grafana - initialize app port number is 3000
         ----------------------
            |-> say message input app is not matched
            |-> default app name is: demoApp running port:8000

-> display app name and running port number
'''
app_name = input('Enter an app name:')
if(app_name == 'grafana' or app_name == 'GRAFANA' or app_name == 'Grafana'):
    port = 3000
else:
    app_name = 'demoApp'
    port = 8000

print(f'App name is:{app_name} running port number is:{port}')

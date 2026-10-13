'''
Write a python program:
- read an app name from <STDIN>
- test - input app name is: grafana -> initialize port number - 3000
                                       config file is - /etc/grafana.conf
- test - input app name is: prometheus -> initialize port number - 9090
                                       config file is - /etc/prometheus.yml
- test - input app name is: webauth -> initialize port number is - 5001
                                       config file is: - /etc/web2.0/auth.cfg
|
- default - app name is demoApp - port number 8000 - /etc/demoapp.cfg 

- display app details
'''
login_name = input('Enter a login name:')
if(login_name == 'root'):
    app_name = input('Enter an app name:')
    if(app_name == 'grafana'):
        port = 3000
        fname = "/etc/grafana.conf"
    elif(app_name == 'prometheus'):
        port = 9090
        fname = '/etc/prometheus.yml'
    elif(app_name == 'webauth'):
        port = 5001
        fname = '/etc/web2.0/auth.cfg'
    else:
        app_name = 'demoApp'
        port = 8000
        fname = '/etc/demoApp.cfg'
else:
    print(f'Sorry {login_name} your not a root user')
    exit() # exit from process

print(f'''App name is:{app_name}
Running port:{port}
Configuration file is:{fname}''')
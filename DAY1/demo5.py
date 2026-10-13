app_name = input('Enter an App name:')
app_port = input(f'Enter {app_name} port Number:')
app_version = input(f'Enter {app_name} version:')
app_status = True

print(f'''App name is:{app_name}
----------------------------------------------
      {app_name} running port number:{app_port}
-----------------------------------------------
      {app_name} version is:{app_version}
------------------------------------------
      Running status is:{app_status}
------------------------------------------''')
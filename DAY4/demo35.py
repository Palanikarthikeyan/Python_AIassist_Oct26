class Enrollment:
    def __init__(self,en,eb,ed):
        self.ename = en
        self.edob = eb
        self.edept = ed
        print(f'Emp {self.ename} enrollment is done')
    def display(self):
        print(f'Emp name:{self.ename} DOB:{self.edob} Working dept is:{self.edept}')
        
eobj1 = Enrollment('arun','1st Jan','sales')
eobj2 = Enrollment('theeb','2nd Feb','HR')
### 
# display emp details
eobj1.display()
eobj2.display()
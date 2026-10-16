class Enrollment:
    ename = ''
    edob = ''
    edept = ''
    def initialize(self,en,eb,ed):
        self.ename = en
        self.edob = eb
        self.edept = ed
        print(f'Emp {self.ename} enrollment is done')
    def display(self):
        print(f'Emp name:{self.ename} DOB:{self.edob} Working dept is:{self.edept}')
        
eobj1 = Enrollment()
eobj1.initialize('arun','1st Jan','sales')
eobj2 = Enrollment()
eobj2.initialize('theeb','2nd Feb','HR')
### 
# display emp details
eobj1.display()
eobj2.display()
class Employee:
    def __init__(self, empno, ename, basic, hra,da):
        self.empno = empno 
        self.ename  = ename 
        self.basic = basic 
        self.hra = hra 
        self.da = da 
        self.netpay = 0.0 

    def calculate(self):
        self.netpay = self.basic + self.hra + self.da 
        return self.netpay 

    def dispdata(self):
        print("emp no : ", self.empno)   
        print("emp name : ", self.ename )
        print("basic salary : ", self.basic )
        print("HRA : ",self.hra)
        print("DA : ", self.da)
        print(" net Pay : ", self.netpay) 

emp = Employee(101, "John Doe", 30000, 5000, 3000)
emp.calculate()
emp.dispdata()

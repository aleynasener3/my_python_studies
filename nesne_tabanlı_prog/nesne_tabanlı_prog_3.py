class employer():
    def __init__(self,name,salary,department):

        self.name = name
        self.salary = salary
        self.department =department

    def show_info(self):
        print("name : {} \n Salary : {} \n Department {}".format(self.name,self.salary,self.department))

    def change_department(self,new_department):
        self.deparment = new_department


class owner(employer):
    def __init__(self,name,salary,department,emp_num):

        super().__init__(name,salary,department)
        #self.name=name
        #self.salary=salary
        #self.department=department
        self.emp_num=emp_num

    def show_info(self):
        print("name : {} \n Salary : {} \n Department {} Employer Number : {}".format(self.name,self.salary,self.department,self.emp_num))

    def add_salary(self,add_amount):
        self.salary+= add_amount

owner = owner("aleyna",20000,"eee")

owner.show_info()
owner.add_salary(500)
owner.show_info()


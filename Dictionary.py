emp_detail = {}
emp_detail['name'] = input("Enter your name : ")
emp_detail.setdefault('name')
emp_detail['age'] = input("Enter your age: ")
emp_detail.setdefault('age')
emp_detail['address'] = input("Enter your address : ")
emp_detail.setdefault('address')
emp_detail['year'] = input("Enter year of experience: ")
emp_detail.setdefault('year')

for key, value in emp_detail.items():
    print(f"{key} : {value}")

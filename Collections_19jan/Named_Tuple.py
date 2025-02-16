from collections import namedtuple 

Student = namedtuple('Student', ['name', 'age' , 'DOB'])

S = Student('Anjali', '16', '54657')

print("the student age is using index : ", end ="")
print(S[1])

print("the student name using keyname is : ", end = "")
print(S.name)


# _make() and _asdict()  concversion operations 


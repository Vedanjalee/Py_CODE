from collections import UserString 

class Mystring(UserString):
    def append(self,s):
        self.data += s 

    def remove(self,s):
        self.data =  self.data.replace(s, "")

s1 = Mystring("Geeks")
print("original string: ", s1.data)

# appending to string

s1.append("s")
print("string after appending ", s1.data)

# remoing frmm string 
s1.remove("e")
print("string after removing : ", s1.data)


# example and codes for __init__() function

# constructor always takes an arguement or parameter called the "self" parameter

# it refernces / means itself or the object itself that is in context

# self is basically the name of the instance of the class...

# self arguement always has to written....if self is not written in the init function, then u get an error.

# self can be any other word also...but basically the first parameter in the init function means "self" itself
# the self parameter is a referance to the instance of the class, and it is used to access variables that belong to the class.

# if a constructor only has the self parameter then it is called a default parameter....and if a constructor has some parameter other than self then its called as parameterized constructors.

# any data/variable is called as an attribute...example- name and score are both attributes.

class Student:

    # this is a default constructor( gets cretated automatically by python if not created by us)
    def __init__(self):
        pass

    # this is a parameterized constructor as it has other parameters other than self
    def __init__(self,name,marks):
        self.name=name
        self.score=marks
        
        print("adding new student to db...." )

s1=Student("shreyas",97)
print(s1.name, s1.score)

s2=Student("meg",98)
print(s2.name,s2.score)



class Teacher:
    def __init__(self, fullname):
        self.name=fullname
        print("adding new teahcer to the db")

t1=Teacher("manjunath")
print(f"new teachers name is {t1.name}")






# Class example

# Why use classes? 

# Allows us to group data and fucntions together in a logical way
# data = attributes like health, name, social security
# functions = methods

# imagine an employee, we'd need lots of info on them so we can create a class to stop us doing shit manually everytime

class Test:
    pass # just skip this, prevents an error


x = Test() # This creates an 'instance;' ---- <__main__.Test instance at 0x1004cf050> <- shows unique position in memory
y = Test() # creates another UNIQUE instance of that class

# We will use 'self' a lot, this basically refers to the classess own functions and variables 

class Ph:
    def printHam(self): # when you call functions, you dont need the self in there, only when defining
        print 'Ham'

# if you remove self you get a type error printHam takes 0 arguments but one is given!
# classes always need to pass self 

x = Ph() # creates an instance

x.printHam() #this almost feels like an import on a module, it needs to be imported first


## Create CONSTRUCTOR - or in other words initialisation function for the class ##

# These run when the class is created or initalised 
# in charge of the setup work for the class
# as an example if we wanted a game character to have default health, 
# we would do this in the constructor function

class Ph:
    def __init__(self):
        self.y = 5 # the correct way to create variables that can be accessed outside - these are GLOBAL (avaialbe outside the function)
        z = 5 # is only available LOCALLY in the function and cannot be called as below

        self.printHam() # notice how i can call this in the __init__ before i declare it logically!?

    def printHam(self): # when you call functions, you dont need the self in there, only when defining
        print 'Ham'


x = Ph()

print x.y 
# print x.z # causes: AttributeError: Ph instance has no attribute 'z'





##### ---- EXAMPLE: Creating a Hero ---- #####

class Hero:
    '''A hero who is allergic to apples no less'''

    def __init__(self, name):
        self.name = name
        self.health = 100

    def eat(self, food):
        if food == 'apple':
            self.health -= 100
        elif food == 'ham':
            self.health +=20

bob = Hero('Bob')
print bob.health
print bob.name

bob.eat('ham')



#### ---- Employee Example ---- ####


class Employee:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        
        self.emailConstructor()
        self.displayDetails() # can call before definition and it will execute on creation

    def emailConstructor(firstName, lastName):
        companyEmail ='%s.%s@myCompany.com' %(self.firstName, self.lastName)
        return companyEmail 

    def displayDetails(self):
        print '****** NEW EMPLOYEE DETAILS ******'
        print 'First Name:', self.firstName
        print 'Last Name:', self.lastName
        print 'e-mail address:', self.email

employee1 = Employee('Kris', 'McCarty', 'kristofor.mccarty@yournob.com')




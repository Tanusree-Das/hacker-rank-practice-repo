"""Errors detected during execution are called exceptions.
The statements try and except can be used to handle selected exceptions.
A try statement may have more than one except clause to specify handlers for different exceptions.

The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.

Task:- Perform integer division and print a/b (In the case of ZeroDivisionError or ValueError, print the error code)

Constraints:- 0<T<10"""

if __name__=="__main__": #can be executed only as script
    what_to_execute=int(input("press 1 to execute number division Exception \n"
                              "press 2 to execute KeyBoard Exception \n"
                              "press 3 class level exception:\n"
                              "press 4 to assign args and str in a custom Exception\n"
                              "press 5 for except,else and finally block check\n"))
    if what_to_execute==1:
        print("Code for Number division Exception Handling From HackerRank.")
        number_of_test_cases=int(input("number of test cases?"))
        for i in range(number_of_test_cases):
            try:
                a,b=map(int,input("space separated values of a and b?").split())
                print(a//b)
                raise KeyboardInterrupt
            except ZeroDivisionError as e:
                print("Error Code arugemnts:",e.args[0]," and Error Code String:",e)
            except ValueError as e:
                print("Error Code:",e)
            except KeyboardInterrupt as e: #this shouldn't be included in program unless it is doing some specific work
                print("Error code:",e)
                print("This is my doing just for testing")
            finally:
                print("lets see whether it will be executed or not")
    elif what_to_execute==2:
        print("Code to perform Keyboard Exception when we try to stop the program.")
        while True:
            try:
                x=int(input("Please provide a valid number"))
                break
            except ValueError as e:
                print("Error code:",e)
            except KeyboardInterrupt:
                print("Interrupted by you")
    elif what_to_execute==3:
        print("Code to show how Exception class and subclass performs when order changes!!")
        print("\n**Sequence of Exception handle will be changed here "
              "Exception block is written in Top to Bottom fashion "
              "that means first parent,child and then grandchild except block**")
        class CreatedBaseClass(Exception):
            pass
        class CreatedChildClass(CreatedBaseClass):
            pass
        class CreatedGrandChildClass(CreatedChildClass):
            pass
        for cls1 in [CreatedBaseClass,CreatedChildClass,CreatedGrandChildClass]:
            try:
                print("Raising Exception For:",cls1.__name__)
                raise cls1()
            except CreatedBaseClass as e:
                print("Exception will be handled by -> Base Class Except block")
            except CreatedChildClass as e:
                print("Exception will be handled by -> Child Class Except block")
            except CreatedGrandChildClass as e:
                print("Exception will be handled by -> Grand Child Class Except block")

        print("\n**Sequence of Exception handle will be changed here "
              "Exception block is written in bootom to top fashion "
              "that means first grancchild,child,parent except block**")
        for cls2 in [CreatedBaseClass,CreatedChildClass,CreatedGrandChildClass]:
            try:
                print("Raising Exception For:",cls2.__name__)
                raise cls2()
            except CreatedGrandChildClass as e:
                print("Exception will be handled by -> Grand Child Class Except block")
            except CreatedChildClass as e:
                print("Exception will be handled by -> Child Class Except block")
            except CreatedBaseClass as e:
                print("Exception will be handled by -> Base Class Except block")

        print("\n**That means except clause is compatible with an exception if it "
              "is the same class or a base class but not the other way around**")
    elif what_to_execute == 4:
        class LowAgeError(Exception):
            def __init__(self,*args):
                pass
            def __str__(self):
                return "You are too young to be an Employee"
        class Employee:
            def __init__(self,name,age):
                self.name=name
                if age>18:
                    self.age=age
                else:
                    raise LowAgeError(age)
            def display(self):
                print("The name of the employee is ",self.name," and age is ",self.age)
        try:
            employee2 = Employee("Dipesh",50)
            employee1 = Employee("Tanusree", 15)
        except LowAgeError as e:
            print("Error Code:",e.args)


    elif what_to_execute==5:
        try:
            my_dividend=int(input("2/?"))
            my_result=2//my_dividend
            another_ip=input()
        except ZeroDivisionError as e:
            print("Error Code:",e.args)
        else:
            print("No exception occured and o/p is->",my_result)
        finally:
            print("---The End---")



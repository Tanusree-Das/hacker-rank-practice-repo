'''collections.namedtuple()
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.'''

from collections import namedtuple

if __name__=="__main__":
  N=int(input("total number of student?"))
  column1,column2,column3,column4=input("please provide the spreadsheet header").split()
  #student=namedtuple("student","ID MARKS CLASS NAME")
  total_marks=0
  for student_details in range(N):
    student_input_details=input("enter the data").split()
    if(column1=="MARKS"):
      total_marks+=int(student_input_details[0])
    elif(column2=="MARKS"):
      total_marks+=int(student_input_details[1])
    elif (column3 == "MARKS"):
      total_marks+= int(student_input_details[2])
    else:
      total_marks+= int(student_input_details[3])
  average_marks=total_marks/N
  print("average marks=",average_marks)
  #average_marks=(studen1.MARKS+student2.MARKS....+studentn.MARKS)/N
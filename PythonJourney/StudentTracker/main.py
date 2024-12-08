from studentCreate import studentCreate
from studentCreate import student_view
from studentCreate import student_update
from studentCreate import student_delete
from filterStudent import FindStudent,subjectFiltering,FailedStudent
from statisticsStudent import TopperStudent, studentsRanking,conditionalList



def main():
 while (True):
  print("Welcome to the Student tracker App")
  print("\nChoose anything From the Menu")
  print("\n1. CRUD on Student Data")
  print("\n2. Student Filter")
  print("\n3. Calculate Statistics")
  print("\n4. Exit")
  choice = input("Enter Your Choice:")
  if int(choice) == 1:
   print("\n Welcome to the Students Section")
   print("\n1. Create")
   print("\n2. Update")
   print("\n3. View")
   print("\n4. Delete")
   choice_student = input("What do you want to do with data")
   if int(choice_student) == 1:
    name = input("Enter Your Name")
    Marks = input("Enter Your Marks")
    Subject = input("Enter Your Favourite Subject")
    studentCreate(name,Subject,Marks)
   elif int(choice_student) == 3:
    student_view()
   elif int(choice_student) == 2:
    name1 = input("Enter the name: ")
    key = input("Enter the property: ")
    value = input("Enter what you want to update it into: ")
    student_update(name1,key,value)
   elif int(choice_student) == 4:
    name2 = input("Enter the name of record you want to delete: ")
    student_delete(name2)
  elif int(choice) == 2:
   print("\nWelcome to Student Filter Section")
   print("\n1. Search by name")
   print("\n2. Subject Based Filter")
   print("\n3. Failing Students")
   print("\n4. Range marks Students")
   choice_filter = input("Enter the Function you want to add")
   if int(choice_filter) == 1:
    name_of_student = input("Type the Name: ")
    FindStudent(name_of_student)
   elif int(choice_filter) == 2:
    name_of_Subject=input("Type in the Subject : ")
    subjectFiltering(name_of_Subject)
   elif int(choice_filter)==3:
    FailedStudent()
  elif int(choice) == 3:
   print("\nWelcome to Student Statistics Section")
   print("\n1. Rankings")
   print("\n2. Toppers Subject Wise")
   choice_statistics = input("Enter the Function you want to add")
   if int(choice_statistics)==1:
    studentsRanking()
   elif int(choice_statistics) ==2:
    TopperStudent()
   elif int(choice_statistics) ==3:
    condition=input("Enter the value: ")
    conditionalList(condition)

   



if __name__ == "__main__":
 main()
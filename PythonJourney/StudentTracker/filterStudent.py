import os
import json
from studentCreate import file_checker


folder_path = os.path.join(os.getcwd(),'StudentTracker')
file_path = os.path.join(folder_path,"data.json")
database_file=[]
temp_filterStuff = []

def file_loader():
  global database_file
  with open(file_path,'r') as file:
    database_file = json.load(file)



def FindStudent (name_of_student):
  if file_checker():
    file_loader()
    for Student in database_file:
      if name_of_student == Student["name"]:
        print("item mAtched")
        print(Student)
  else:
    print("No File")

def subjectFiltering(name_of_Subject):
  if file_checker():
    file_loader()
    filtered_Students = list(filter(lambda student:student['Subject'] == name_of_Subject,database_file))
    print(filtered_Students)

def FailedStudent():
  if file_checker():
    file_loader()
    failed_student = list(filter(lambda student: student['Marks']<=40,database_file))
    print(failed_student)
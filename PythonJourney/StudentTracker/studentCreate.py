import os
import json

folder_path = os.path.join(os.getcwd(), "StudentTracker")  
file_path = os.path.join(folder_path, "data.json")

database_file = []


def file_checker():
  if os.path.exists(file_path):
    return True
  else:
    return False
  
def file_reader():
  global database_file
  if file_checker():
    print("in the file checker in file_reader")
    with open(file_path,'r') as file:
        file_content = file.read().strip()
        if file_content: 
          database_file = json.loads(file_content)
        else:
          database_file = []
  else :
    print("no file as such") 

def file_writer():
 with open(file_path,'w') as file:
  json.dump(database_file,file,indent=4)

def studentCreate(name,Subject,Marks):
 data = {
   "name":name,
   "Subject":Subject,
   "Marks":Marks
 }

 if file_checker():
   file_reader()
   database_file.append(data)
   file_writer()
   print("Student added successfully.")
 else:
  print("No file exists with No data")

def student_view ():
 if file_checker():
  file_reader()
  print(database_file)
 else:
    print("No file exists with No data") 

def student_update(name1,key,value):
  if file_checker():
   file_reader()
   for students in database_file:
     if students['name']==name1:
       if key in students:
        students[key]=value
        file_writer()
        print("Successfully updated")
       else :
         print("Wrong key") 
     else:
       print("No name present") 
  else:
   print("No file exists with No data") 
  
def student_delete(name2):
  if file_checker():
    file_reader()
    for student in database_file:
      if student['name'] == name2:
        database_file.remove(student)
        file_writer()
      
    print("removed Successfully")
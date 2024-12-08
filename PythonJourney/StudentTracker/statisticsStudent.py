import json
import re
from studentCreate import file_checker
from filterStudent import file_path


database_file=[]
subject_grouped = {}
topper_List = {}

def subjectGrouper():
  for filesLoop in database_file:
      subject=filesLoop['Subject']
      if subject not in subject_grouped:
        subject_grouped[subject]=[]
      subject_grouped[subject].append(filesLoop)

def finalRanker():
  for subject,student_list in subject_grouped.items():
    sort_Students = sorted(student_list, key=lambda student:student['Marks'],reverse=True)
    topper_List[subject]=sort_Students[0]['name']
  for subject,topper in topper_List.items():
   print(f'the {subject} topper is {topper}')




def file_loader():
  global database_file
  with open(file_path,'r') as file:
    database_file = json.load(file)

def studentsRanking():
  if file_checker():
    print("working in studentRankings")
    file_loader()
    result = list(sorted(database_file,key=lambda student:student['Marks'],reverse=True))
    final_result = list(map(lambda student:student['name'],result))
    print(final_result)

def TopperStudent():
  if file_checker():
    print("the topper Student is working ")
    file_loader()
    subjectGrouper()
    finalRanker()
  else:
    print("else ciondition")
    
def conditionalList(condition):
  if file_checker():
    file_loader()


int()  

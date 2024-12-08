

from addTask import tasks

def view_tasks():
  if (not tasks):
    print("No task is there.")
    return
  for index,item in enumerate(tasks,start=1):
   print(f"Task no. {index}")
   print("===================")
   print(f"Name: {item['name']}")
   print(f"description: {item['description']}")
   print(f"deadline {item['deadline']}")
   print(f"priority {item['priority']}")

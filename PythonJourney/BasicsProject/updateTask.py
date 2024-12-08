

from addTask import tasks

def update_task(name,key,value):
  for item in tasks:
    if item[name] == name:
      if key in item:
        item[key]=value
        print(f"Successfully updated the task{name}")
    else:
      print(f"the{key}is wrong")
    return
  print(f"there is no task named{name}")
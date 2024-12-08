

from addTask import tasks

def delete_task(name):
  for items in tasks:
    if items[name]==name:
      tasks.remove(items)
      print(f"task successfully removed")
      return
    else:
      print(f"No task was there to named{name}")
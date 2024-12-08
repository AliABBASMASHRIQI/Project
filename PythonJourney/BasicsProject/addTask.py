tasks = []

def add_task(name,description,deadline,priority,):
  task = {
    "name":name,
    "description":description,
    "deadline":deadline,
    "priority":priority
  }

  tasks.append(task)
  print(f'the{task["name"]} has been added Successfully.')
from addTask import add_task
from deleteTask import delete_task
from updateTask import update_task
from readTask import view_tasks

def main():
    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter task name: ")  
            description = input("Enter task description: ")  
            deadline = input("Enter task deadline : ")  
            priority = input("Enter task priority : ")  
            add_task(name, description, deadline, priority)
        
        elif choice == "2":
            view_tasks()
        
        elif choice == "3":
            name = input("Enter task name to update: ")  
            key = input("Enter the field to update (name/description/deadline/priority): ")  
            value = input(f"Enter new value for {key}: ")  
            update_task(name, key, value)
        
        elif choice == "4":
            name = input("Enter task name to delete: ")
            delete_task(name)
        
        elif choice == "5":
            print("Exit Task Management ")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

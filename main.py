import json
from tabulate import tabulate

TASK_FILE = "tasks.json" #saves all files

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)  # Try to load tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []  #return an empty list if the file doesn't exist or is corrupted
    
def save_tasks(tasks): #saves tasks to file
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(): #add tasks
    task_description = input("Enter task description: ")
    priority = input("Enter priority (Low, Medium, High): ").capitalize()
    tasks = load_tasks()  # Load existing tasks
    new_task = {"task": task_description, "priority": priority, "status": "Pending"}
    tasks.append(new_task)  # Append new task to the list
    save_tasks(tasks)  # Save the updated list of tasks
    print("Task added successfully!")


def view_task(): #view task
    task = load_tasks()
    if not task:
        print("No tasks available.")
        return
    print(tabulate(task, headers = "keys", tablefmt = "grid"))

def mark_done(): #mark task as done
    view_task()
    task = load_tasks()
    if not task:
        return
    try:
        task_id = int(input("Enter the task number to mark as done: ")) - 1
        task[task_id]["status"] = "Done"
        save_tasks(task)
        print("Task marked as done!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def delete_task(): #delete task
    view_task()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        task_id = int(input("Enter the task number to delete: ")) - 1
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def main(): #main menu
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


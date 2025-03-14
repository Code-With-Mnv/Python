# Initialize an empty task list
task_list = []

def display_tasks():
    if not task_list:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def add_task(task):
    task_list.append(task)
    print(f"Task '{task}' added.")

def remove_task(task_index):
    if 0 <= task_index < len(task_list):
        removed_task = task_list.pop(task_index)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task index.")

def update_task(task_index, new_task):
    if 0 <= task_index < len(task_list):
        task_list[task_index] = new_task
        print(f"Task {task_index + 1} updated to '{new_task}'.")
    else:
        print("Invalid task index.")

def sort_tasks():
    task_list.sort()
    print("Tasks sorted.")


while True:
    print("\nTask Manager")
    print("1. Display tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Update task")
    print("5. Sort tasks")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '3':
        task_index = int(input("Enter the task index to remove: ")) - 1
        remove_task(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task index to update: ")) - 1
        new_task = input("Enter the new task: ")
        update_task(task_index, new_task)
    elif choice == '5':
        sort_tasks()
    elif choice == '6':
        print("Exiting Task Manager.")
        break
    else:
        print("Invalid choice. Please try again.")

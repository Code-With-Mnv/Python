# Initialize an empty task list
task_list = []

def display_tasks():
    if not task_list:
        print("No tasks in the list.")
    else:
        for index, (task, priority) in enumerate(task_list, start=1):
            print(f"{index}. {task} [{priority}]")

def add_task(task, priority):
    task_list.append((task, priority))
    print(f"Task '{task}' with priority '{priority}' added.")

def remove_task(task_index):
    if 0 <= task_index < len(task_list):
        removed_task, removed_priority = task_list.pop(task_index)
        print(f"Task '{removed_task}' with priority '{removed_priority}' removed.")
    else:
        print("Invalid task index.")

def update_task(task_index, new_task, new_priority):
    if 0 <= task_index < len(task_list):
        task_list[task_index] = (new_task, new_priority)
        print(f"Task {task_index + 1} updated to '{new_task}' with priority '{new_priority}'.")
    else:
        print("Invalid task index.")

def sort_tasks():
    priority_order = {'Urgent': 1, 'Necessary': 2, 'Normal': 3}
    task_list.sort(key=lambda x: priority_order[x[1]])
    print("Tasks sorted by priority.")

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
        priority = input("Enter the priority (Urgent, Necessary, Normal): ").capitalize()
        if priority in ['Urgent', 'Necessary', 'Normal']:
            add_task(task, priority)
        else:
            print("Invalid priority. Please enter one of Urgent, Necessary, Normal.")
    elif choice == '3':
        task_index = int(input("Enter the task index to remove: ")) - 1
        remove_task(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task index to update: ")) - 1
        new_task = input("Enter the new task: ")
        new_priority = input("Enter the new priority (Urgent, Necessary, Normal): ").capitalize()
        if new_priority in ['Urgent', 'Necessary', 'Normal']:
            update_task(task_index, new_task, new_priority)
        else:
            print("Invalid priority. Please enter one of Urgent, Necessary, Normal.")
    elif choice == '5':
        sort_tasks()
    elif choice == '6':
        print("Exiting Task Manager.")
        break
    else:
        print("Invalid choice. Please try again.")

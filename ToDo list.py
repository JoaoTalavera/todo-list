import json
import os

FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks):
        status = "✔" if task['done'] else "✘"
        print(f"{i + 1}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter the new task: ")
    tasks.append({'title': title, 'done': False})
    save_tasks(tasks)

def mark_as_done(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Enter the number of the task that is completed: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]['done'] = True
            save_tasks(tasks)
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Enter the number of the task you want to remove: ")) - 1
        if 0 <= i < len(tasks):
            tasks.pop(i)
            save_tasks(tasks)
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")

def menu():
    tasks = load_tasks()
    while True:
        print("\n=== Menu ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")
        option = input("\nChoose an option: ")

        if option == '1':
            show_tasks(tasks)
        elif option == '2':
            add_task(tasks)
        elif option == '3':
            mark_as_done(tasks)
        elif option == '4':
            remove_task(tasks)
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == '__main__':
    menu()

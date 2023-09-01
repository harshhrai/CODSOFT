import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{new_task}' added.")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter a new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            show_tasks(tasks)
            task_index = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

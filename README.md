# CODSOFT  This code is a Python script for a command-line To-Do List application. It allows users to manage a list of tasks by providing options for viewing, adding, and deleting tasks. Here's a breakdown of how the code works:

1. Importing the `json` Module:
   ```python
   import json
   ```

   The script starts by importing the `json` module, which will be used to load and save tasks in a JSON file.

2. `load_tasks` Function:
   ```python
   def load_tasks():
       try:
           with open('tasks.json', 'r') as file:
               return json.load(file)
       except FileNotFoundError:
           return []
   ```

   - This function attempts to open a file called 'tasks.json' in read mode.
   - If the file exists, it loads the tasks from the file using `json.load()` and returns them as a list.
   - If the file does not exist (FileNotFoundError), it returns an empty list.

3. `save_tasks` Function:
   ```python
   def save_tasks(tasks):
       with open('tasks.json', 'w') as file:
           json.dump(tasks, file)
   ```

   - This function takes a list of tasks as input and saves them to a file called 'tasks.json' in write mode using `json.dump()`.

4. `show_tasks` Function:
   ```python
   def show_tasks(tasks):
       print("To-Do List:")
       for i, task in enumerate(tasks, start=1):
           print(f"{i}. {task}")
   ```

   - This function takes a list of tasks as input and displays them on the console, enumerating them with numbers.

5. `add_task` Function:
   ```python
   def add_task(tasks, new_task):
       tasks.append(new_task)
       save_tasks(tasks)
       print(f"Task '{new_task}' added.")
   ```

   - This function allows users to add a new task to the list. It takes a list of tasks and the new task description as input.
   - It appends the new task to the list, saves the updated list to the file, and prints a confirmation message.

6. `delete_task` Function:
   ```python
   def delete_task(tasks, task_index):
       if 1 <= task_index <= len(tasks):
           deleted_task = tasks.pop(task_index - 1)
           save_tasks(tasks)
           print(f"Task '{deleted_task}' deleted.")
       else:
           print("Invalid task number.")
   ```

   - This function allows users to delete a task from the list. It takes a list of tasks and the index of the task to delete as input.
   - It checks if the provided task index is valid (within the range of existing tasks), deletes the task, saves the updated list, and prints a confirmation message. If the index is invalid, it prints an error message.

7. `main` Function:
   ```python
   def main():
       tasks = load_tasks()
       while True:
           # Display menu options and take user input for choices
           # Call the appropriate functions based on the user's choice
   ```

   - The `main` function serves as the entry point of the script. It loads existing tasks using `load_tasks` and then enters a loop to display a menu of options to the user.
   - The user can choose to show tasks, add a task, delete a task, or quit the application.
   - Based on the user's choice, the corresponding functions are called to perform the desired task.

8. `if __name__ == "__main__":` Block:
   ```python
   if __name__ == "__main__":
       main()
   ```

   - This block ensures that the `main` function is executed when the script is run directly (not imported as a module).

In summary, this code provides a simple command-line To-Do List application with options to add, delete, and display tasks. The tasks are stored in a 'tasks.json' file using JSON serialization. Users can interact with the application through a menu-driven interface.

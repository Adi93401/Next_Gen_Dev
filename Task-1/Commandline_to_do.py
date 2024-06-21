import json

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Marked task {task_number} as completed.")
        else:
            print("Invalid task number.")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]["task"]
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Updated task {task_number} from '{old_task}' to '{new_task}'.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {task['task']}")
        else:
            print("Invalid task number.")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)
        print(f"Tasks saved to {filename}")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty list.")

def main():
    todo_list = TodoList()
    todo_list.load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Save Tasks")
        print("7. Load Tasks")
        print("8. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == "5":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "6":
            todo_list.save_tasks()
        elif choice == "7":
            todo_list.load_tasks()
        elif choice == "8":
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

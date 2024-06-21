import tkinter as tk
from tkinter import messagebox
import json

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.load_tasks()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack()

        self.load_tasks_to_listbox()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.entry.delete(0, tk.END)
            self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks.pop(index)
            self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def load_tasks_to_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)
        messagebox.showinfo("Info", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

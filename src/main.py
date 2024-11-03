import customtkinter as ctk
import pickle
from tkinter import messagebox
from tkinter import Listbox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")

        self.tasks = []

        self.title_label = ctk.CTkLabel(
            self.root, text="Daily Tasks", font=ctk.CTkFont(size=30)
        )
        self.title_label.pack()

        self.task_input = ctk.CTkEntry(self.root, width=500)
        self.task_input.pack(pady=10)

        self.add_task_button = ctk.CTkButton(
            self.root, width=500, text="Add Task", command=self.add_task
        )
        self.add_task_button.pack(pady=10)

        self.delete_task_button = ctk.CTkButton(
            self.root, width=500, text="Delete Task", command=self.delete_task
        )
        self.delete_task_button.pack(pady=10)

        self.task_listbox = Listbox(
            self.root, width=60, background="black", foreground="white"
        )
        self.task_listbox.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.update_task()
            self.task_input.delete(0, ctk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            self.tasks.remove(selected_task)
        except:
            messagebox.showwarning("Warning", "Select a task to delete")

        self.update_task()

    def update_task(self):
        self.task_listbox.delete(0, ctk.END)
        self.save_tasks()
        for task in self.tasks:
            self.task_listbox.insert(ctk.END, task)

    def save_tasks(self):
        with open("save.txt", "wb") as f:
            pickle.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open("save.txt", "rb") as f:
                self.tasks = pickle.load(f)
        except EOFError:
            pass
        self.update_task()


if __name__ == "__main__":
    root = ctk.CTk()
    app = TodoApp(root)
    root.mainloop()

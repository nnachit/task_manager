import customtkinter as ctk
from tkinter import messagebox


class TodoApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")

        self.tasks = []

        self.title_label = ctk.CTkLabel(self.root, text="Daily Tasks", font=ctk.CTkFont(size=30))
        self.title_label.pack()

        self.task_input = ctk.CTkEntry(self.root, width=500)
        self.task_input.pack(pady=10)

        self.task_frame = ctk.CTkScrollableFrame(self.root, width=500, height=150)
        self.task_frame.pack(pady=10)

        self.add_task_button = ctk.CTkButton(self.root, width=500, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.delete_task_button = ctk.CTkButton(self.root, width=500, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.update_task()
            self.task_input.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "The task entry is empty")

    def delete_task(self):
        # TODO : delete selected task    
        pass

    def update_task(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in self.tasks:
            task_label = ctk.CTkLabel(self.task_frame, text=task, anchor="w")
            task_label.pack(fill="x", pady=2)

if __name__ == "__main__":
    root = ctk.CTk()
    app = TodoApp(root)
    root.mainloop()
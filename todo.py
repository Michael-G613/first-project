import tkinter as tk
from tkinter import messagebox
class TodDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks_listbox = tk.Listbox(self.root, width=50,height=15)
        self.tasks_listbox.pack(pady=10)

        self.task_entry=tk.Entry(self.root, width = 50)
        self.task_entry.pack(pady=5)

        self.add_button=tk.Button(self.root, text="Add Task",command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button=tk.Button(self.root, text="Remove Task",command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task= self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0,tk.END)

        else:
            messagebox.showwarning("Input Error","Please emter a task!")

    def remove_task(self):
        try:
            selected_task_index=self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)

        except IndexError: 
            messagebox.showwarning("Selection Error","Please select a task to remove!")

if __name__=="__main__":
    root= tk.Tk()
    app=TodDoApp(root)
    root.mainloop()

    
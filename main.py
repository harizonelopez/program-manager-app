import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry

class Task:
    def __init__(self, title, description, due_date, completed = False, completed_date = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.completed_date = completed_date

class Task_Manager_App:
    def __init__(self, master):
        self.master = master
        self.master.title("Dev_@ladinh production Program Manager App")
        self.master.geometry("400x450")
        self.master.config(background="gray")
        self.master.resizable(False, False)

        self.tasks = []
        
        self.header_label = tk.Label(master, bg="gray", fg="blue", text="A Program Manager App")
        self.header_label.place(x=130, y=20)

        self.title_label = tk.Label(master, text="Title of the Task", bg="gray", fg="blue")     
        self.title_label.place(x=40, y=80)

        self.title_entry = tk.Entry(master, bg="lightgray", fg="blue")
        self.title_entry.place(x=33, y=100)
        
        self.desc_label = tk.Label(master, text="Task description", bg="gray", fg="blue")
        self.desc_label.place(x=40, y=140)

        self.desc_entry = tk.Entry(master, bg="lightgray", fg="blue")
        self.desc_entry.place(x=33,y=160)

        self.due_date_label = tk.Label(master, text="Task due date", bg="gray", fg="blue")
        self.due_date_label.place(x=40, y=200)

        self.due_date_entry = DateEntry(master, date_pattern="yyyy-mm-dd", width=12, background="darkblue", foreground="gray")
        self.due_date_entry.place(x=33, y=220)
        
        self.add_button = tk.Button(master, text="Add Task", fg="orange", bg="green", command=self.add_task)
        self.add_button.place(x=50, y=260)
        
        self.task_listbox = tk.Listbox(master, height=15, width=35)
        self.task_listbox.place(x=175, y=80)
        
        self.mark_completed_button = tk.Button(master, text="Mark Completed", fg="yellow", bg="green", command=self.mark_completed)
        self.mark_completed_button.place(x=243, y=330)
        
        self.delete_button = tk.Button(master, text="Delete Task", fg="yellow", bg="green", command=self.delete_task)
        self.delete_button.place(x=255, y=355)
        
        self.exit_button = tk.Button(master, text="EXIT \nAPP", fg="pink", bg="red", command=self.exit_app)
        self.exit_button.place(x=170, y=400)
        
    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        due_date = self.due_date_entry.get()

        if title and due_date:
            new_task = Task(title, description, due_date)
            self.tasks.append(new_task)
            self.update_task_listbox()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("ERROR WARNING", "ERROR!! Title and due date are required for you to proceed!")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()

        if selected_task_index:
            selected_task = self.tasks[selected_task_index[0]]
            selected_task.completed = True
            selected_task.completed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()

        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END) 
        for task in self.tasks:
            task_info = f"{task.title} - {task.due_date}"

            if task.completed:
                task_info += f" (Completed on {task.completed_date})"
            self.task_listbox.insert(tk.END, task_info)

    def clear_entry_fields(self):
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

    def exit_app(self):
        self.master.destroy()

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Task_Manager_App(root)
    app.run()

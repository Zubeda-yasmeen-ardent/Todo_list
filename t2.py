import tkinter as tk
from tkinter import messagebox


BG_COLOR = '#f0f0f0'
BUTTON_BG = '#4caf50'
BUTTON_COMPLETE_BG = '#2196F3'
BUTTON_REMOVE_BG = '#f44336'

tasks = []

def add_task():
    description = entry_description.get()
    due_date = entry_due_date.get()
    priority = entry_priority.get()
    
    if description and due_date and priority:
        task = {
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "Complete": False
        }
        tasks.append(task)
        update_display()
        messagebox.showinfo("Task Added", "Task Added Successfully.")

        entry_description.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
        entry_priority.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def update_display():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["Complete"] else "Pending"
        task_list.insert(tk.END, f"{i}. Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {status}")

def complete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks[task_index]["Complete"] = True
        update_display()
        messagebox.showinfo("Task Completed", "Task Marked as Completed.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks.pop(task_index)
        update_display()
        messagebox.showinfo("Task Removed", "Task Removed from the List.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to remove.")

def create_main_window():
    root = tk.Tk()
    root.title("To-do List Application")
    root.geometry("450x640")  
    root.configure(bg='#2c3e50')
    root.resizable(False, False)  



    create_ui_elements(root)

    root.mainloop()

def create_ui_elements(root):
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.grid(row=0, column=0, padx=50, pady=50)

    create_entry_widgets(frame)

    create_buttons(frame)

    create_task_list(root)

def create_entry_widgets(frame):
    labels = ["Description:", "Due Date:", "Priority:"]
    global entry_description, entry_due_date, entry_priority
    entry_description = tk.Entry(frame, width=15)
    entry_due_date = tk.Entry(frame, width=15)
    entry_priority = tk.Entry(frame, width=15)  

    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, bg=BG_COLOR)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        if i == 0:
            entry_description.grid(row=i, column=1, padx=15, pady=5, sticky="ew")
        elif i == 1:
            entry_due_date.grid(row=i, column=1, padx=15, pady=5, sticky="ew")
        else:
            entry_priority.grid(row=i, column=1, padx=15, pady=5, sticky="ew")

def create_buttons(frame):
    buttons = [
        ("Add Task", add_task, BUTTON_BG),
        ("Mark as Completed", complete_task, BUTTON_COMPLETE_BG),
        ("Remove Task", remove_task, BUTTON_REMOVE_BG)
    ]

    for i, (text, command, bg_color) in enumerate(buttons):
        button = tk.Button(frame, text=text, command=command, bg=bg_color, fg="white", cursor="hand2", takefocus=False, padx=15)
        button.grid(row=i + 3, column=0, columnspan=2, pady=10, sticky="ew")

def create_task_list(root):
    global task_list
    task_list = tk.Listbox(
        root,
        height=10,
        width=40,  # Increased width
        font=('Helvetica', 10),
        selectbackground='#a6a6a6',
        selectforeground='white',
        bg='#ffffff',
        borderwidth=2,
        relief="groove"
    )
    task_list.grid(row=1, column=0, pady=10, padx=50, sticky="ew")

create_main_window()

import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = task_Entry.get()
    if task != "":
        task_Listbox.insert(tk.END,task)
        task_Entry.delete(0,tk.END)
    else:
        messagebox.showwarning("⚠️ Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = task_Listbox.curselection()[0]
        task_Listbox.delete(selected_index)
    except:
        messagebox.showwarning("⚠️ Warning", "Please select a task to delete!")

def save_tasks():
    task = task_Listbox.get(0, tk.END)
    with open("todo_tasks.txt", "w") as f:
        for t in task:
            f.write(t + "\n")
    messagebox.showinfo("✅ Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("todo_tasks.txt", "r") as f:
            for line in f:
                task_Listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass  

# UI 

root = tk.Tk()
root.title("🌿 TO DO List 🌿")
root.geometry("420x450")
root.config(bg="white") 



title_Label = tk.Label(root, text= "✨ MY TO DO List ✨", font=("Helvetica", 16, "bold"), bg="white", fg="#2c3e50")
title_Label.pack(pady=10)

frame = tk.Frame(root, bg="white")
frame.pack(pady=5)

task_Entry = tk.Entry(frame, width=30, font=("Times New Roman", 12), bd=2, relief="solid")
task_Entry.pack(side=tk.LEFT, padx=5)

add_Button = tk.Button(frame, text="Add Task",command=add_task, bg="Blue", font=("Helvetica",9, "bold"), fg="white", activebackground="#2980b9", relief="flat",width=10)
add_Button.pack(side=tk.LEFT)

task_Listbox = tk.Listbox(root, width=40, height=15, font=("Times New Roman", 12), selectbackground="#b0d6ff" ,  bd=2, relief="groove")
task_Listbox.pack(pady=10)

button_Frame = tk.Frame(root, bg="white")
button_Frame.pack()

delete_Button = tk.Button(button_Frame, text="🗑 Delete Task",command = delete_task , bg="Red", font=("Helvetica",9, "bold"),fg="white",  activebackground="#c0392b", relief="flat", width=15)
delete_Button.pack(side=tk.LEFT, padx=5)

save_Button = tk.Button(button_Frame, text="💾 Save Tasks",command = save_tasks, bg="Green",font=("Helvetica",9, "bold"), fg="white", activebackground="#229954", relief="flat", width=15)
save_Button.pack(side=tk.LEFT, padx=5)

load_tasks()

root.mainloop()
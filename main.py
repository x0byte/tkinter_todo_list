from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkFont


def add_task_to_list():
    task = task_entry.get()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def del_task_from_list():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def load_from_external_file():

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            with open(file_path, "r") as file:
                tasks = file.readlines()
            
            if task_listbox.size() != 0:
                if messagebox.askyesno("Confirm Action", "Are you sure you want to delete the list?"):
                    task_listbox.delete(0, END)

            for task in tasks:
                task_listbox.insert(END, task.strip())

        except Exception as e:
            print(f"Error loading file: {e}")

    
root = Tk()
root.title("TO DO APP")

root.geometry("600x700")
root.minsize(600, 700)

title_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
entry_font = tkFont.Font(family="Helvetica", size=16)
task_font = tkFont.Font(family="Helvetica", size=16, weight="bold")

# Button style
style = ttk.Style()
style.configure("AddButton.TButton", font=("Helvetica", 16), background="chartreuse1")
style.configure("DelButton.TButton", font=("Helvetica", 16), background="firebrick3", foreground="white")
style.configure("ImportButton.TButton", font=("Helvetica", 16), background="gray67")

lbl_title = ttk.Label(root, font=title_font, anchor="center", text="TO DO LIST")
lbl_title.pack(ipady=20)

# Entry frame
entry_frame = ttk.Frame(root)
entry_frame.pack()

task_entry = ttk.Entry(entry_frame, font=entry_font, justify="center", width=40)
task_entry.pack(ipady=20, ipadx=20)

# Frame for buttons (side by side)
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_task = ttk.Button(button_frame, text="Add task", style="AddButton.TButton", command=add_task_to_list)
add_task.grid(row=0, column=0, padx=10, ipadx=10, ipady=20)

del_task = ttk.Button(button_frame, text="Delete task", style="DelButton.TButton", command=del_task_from_list)
del_task.grid(row=0, column=1, padx=10, ipadx=10, ipady=20)

import_task = ttk.Button(button_frame, text="Import Tasks", style="ImportButton.TButton", command=load_from_external_file)
import_task.grid(row=0, column=2, padx=10, ipadx=10, ipady=20)

# Listbox frame
list_frame = ttk.Frame(root)
list_frame.pack(pady=20)

task_listbox = Listbox(list_frame, font=task_font, width=43, height=20, bg="white", selectbackground="lightblue", highlightthickness=0, selectmode=SINGLE)
task_listbox.pack(pady=20, ipady=10, ipadx=10)

root.mainloop()

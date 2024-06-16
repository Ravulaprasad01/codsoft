import tkinter as tk

def add_task():
  """Adds a new task to the listbox."""
  task = entry.get()
  if task:
    listbox.insert(tk.END, task)
    listbox.itemconfig(tk.END, foreground="black")  # Default color for new tasks
    entry.delete(0, tk.END)

def remove_task():
  """Removes the selected task from the listbox."""
  selected_task = listbox.curselection()
  if selected_task:
    listbox.delete(selected_task[0])

def complete_task():
  """Marks the selected task as completed (green foreground)."""
  selected_task = listbox.curselection()
  if selected_task:
    task_index = selected_task[0]
    task = listbox.get(task_index)
    completed_task = task  # Example: Add "[DONE]" prefix
    listbox.delete(task_index)
    listbox.insert(task_index, completed_task)
    listbox.itemconfig(task_index, foreground="green")  # Green for completed tasks

def not_done_task():
  """Marks the selected task as not done (red foreground, removes "[DONE]")."""
  selected_task = listbox.curselection()
  if selected_task:
    task_index = selected_task[0]
    task = listbox.get(task_index)
    # Remove "[DONE]" prefix and set red foreground
    if task.startswith("[DONE] "):
      not_done_task = task[7:]
    
    else:
      not_done_task = task
    listbox.delete(task_index)
    listbox.insert(task_index, not_done_task)
    listbox.itemconfig(task_index, foreground="red")  # Red for "Not Done" tasks

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Add a heading label
heading_label = tk.Label(root, text="My To-Do List", font=("Arial", 20, "bold","italic"))

# Create widgets
entry = tk.Entry(root, width=30)
entry.insert(0, "Enter task here")  
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30)

complete_button = tk.Button(root, text="Mark Done", command=complete_task)
not_done_button = tk.Button(root, text="Not Done", command=not_done_task)

# Place widgets on the window
heading_label.pack(pady=10)
entry.pack(pady=10)
add_button.pack()
listbox.pack(pady=10)
remove_button.pack(side=tk.LEFT)
complete_button.pack(side=tk.LEFT)
not_done_button.pack(side=tk.LEFT)

root.mainloop()

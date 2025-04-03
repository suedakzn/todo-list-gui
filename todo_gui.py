# Creating a graphical interface using tkinter
import tkinter as tk
from tkinter import messagebox
from todo import ToDoList  # Importing the class that manages tasks
import tkinter.font as tkFont

# Creating an instance of ToDoList (tasks are stored in a JSON file)
todo = ToDoList()

# Creating the main application window
window = tk.Tk()
window.title("To-Do App")
window.geometry("600x500")
window.configure(bg="#f0f0f0")  # Default background color for light theme

# Variable to keep track of the current theme (light or dark)
current_theme = "light"

# Function to apply the selected theme to all components
def apply_theme():
    if current_theme == "light":
        bg = "#f0f0f0"
        fg = "black"
        button_bg = "#4caf50"
        delete_bg1 = "#f44336"
        delete_bg2 = "#9c27b0"
        complete_bg = "#2196f3"
        done_fg = "gray"
    else:
        bg = "#2e2e2e"
        fg = "white"
        button_bg = "#388e3c"
        delete_bg1 = "#d32f2f"
        delete_bg2 = "#7b1fa2"
        complete_bg = "#1976d2"
        done_fg = "#aaaaaa"

    # Applying theme colors to all widgets
    window.configure(bg=bg)
    title.config(bg=bg, fg=fg)
    entry.config(bg="white" if current_theme == "light" else "#3c3c3c", fg=fg)
    label1.config(bg=bg, fg=fg)
    label2.config(bg=bg, fg=fg)
    label_status.config(bg=bg, fg=fg)
    frame_lists.config(bg=bg)
    button_frame.config(bg=bg)
    add_button.config(bg=button_bg)
    done_button.config(bg=complete_bg)
    delete_button1.config(bg=delete_bg1)
    delete_button2.config(bg=delete_bg2)
    listbox_pending.config(bg="white", fg=fg)
    listbox_done.config(bg="white", fg=done_fg)

# Switch between light and dark themes
def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

# Add a new task to the list
def add_task():
    task_text = entry.get()
    if task_text != "":
        todo.add_task(task_text)
        entry.delete(0, tk.END)
        update_lists()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Delete the selected task
def delete_task(listbox, done=False):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        actual_index = get_actual_index(index, done)
        todo.delete_task(actual_index + 1)
        update_lists()

# Mark the selected task as completed
def mark_done():
    selected = listbox_pending.curselection()
    if selected:
        index = selected[0]
        actual_index = get_actual_index(index, done=False)
        todo.mark_done(actual_index + 1)
        update_lists()

# Shorten long tasks for display in the list
def trim_task_text(text, max_length=30):
    return text if len(text) <= max_length else text[:max_length] + "..."

# Update both task lists (pending and completed)
def update_lists():
    listbox_pending.delete(0, tk.END)
    listbox_done.delete(0, tk.END)

    for task in todo.tasks:
        if task["done"]:
            display_text = f"✔️ {trim_task_text(task['task'])}"
            listbox_done.insert(tk.END, display_text)
        else:
            display_text = trim_task_text(task["task"])
            listbox_pending.insert(tk.END, display_text)

    # Display remaining/completed task count at the bottom
    label_status.config(
        text=f"{sum(not t['done'] for t in todo.tasks)} remaining · {sum(t['done'] for t in todo.tasks)} completed"
    )

# Get the real index of a task in the original list (filtered by done status)
def get_actual_index(index_in_box, done):
    filtered = [i for i, t in enumerate(todo.tasks) if t["done"] == done]
    return filtered[index_in_box]

# --- UI Components ---

# Theme toggle button
theme_button = tk.Button(window, text="🌙 Toggle Theme", command=toggle_theme, font=("Arial", 10))
theme_button.pack(pady=5)

# Title label
title = tk.Label(window, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Task entry input
entry = tk.Entry(window, font=("Arial", 12), width=50)
entry.pack(pady=5)

# Button to add new task
add_button = tk.Button(window, text="➕ Add Task", command=add_task, bg="#4caf50", fg="white", font=("Arial", 11))
add_button.pack(pady=5)

# Frame for both task listboxes
frame_lists = tk.Frame(window, bg="#f0f0f0")
frame_lists.pack(pady=10)

# Labels for each list
label1 = tk.Label(frame_lists, text="To-Do", font=("Arial", 12, "bold"), bg="#f0f0f0")
label1.grid(row=0, column=0, padx=20)

label2 = tk.Label(frame_lists, text="Completed", font=("Arial", 12, "bold"), bg="#f0f0f0")
label2.grid(row=0, column=1, padx=20)

# List of pending tasks
listbox_pending = tk.Listbox(frame_lists, width=30, height=10, font=("Arial", 10))
listbox_pending.grid(row=1, column=0, padx=20)

# List of completed tasks
listbox_done = tk.Listbox(frame_lists, width=30, height=10, font=("Arial", 10), fg="gray")
listbox_done.grid(row=1, column=1, padx=20)

# Buttons for complete/delete actions
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

# Button to mark task as done
done_button = tk.Button(button_frame, text="✅ Complete", command=mark_done, bg="#2196f3", fg="white", font=("Arial", 11))
done_button.grid(row=0, column=0, padx=10)

# Button to delete pending task
delete_button1 = tk.Button(button_frame, text="🗑️ Delete To-Do", command=lambda: delete_task(listbox_pending, False), bg="#f44336", fg="white", font=("Arial", 11))
delete_button1.grid(row=0, column=1, padx=10)

# Button to delete completed task
delete_button2 = tk.Button(button_frame, text="🗑️ Delete Completed", command=lambda: delete_task(listbox_done, True), bg="#9c27b0", fg="white", font=("Arial", 11))
delete_button2.grid(row=0, column=2, padx=10)

# Label to show task count
label_status = tk.Label(window, text="", font=("Arial", 10), bg="#f0f0f0", fg="black")
label_status.pack(pady=5)

# Initialize task lists and theme
update_lists()
apply_theme()

# Start the application
window.mainloop()


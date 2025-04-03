import tkinter as tk
from tkinter import messagebox
from todo import ToDoList
import tkinter.font as tkFont

todo = ToDoList()

# TKINTER PENCERESİ
window = tk.Tk()
window.title("To-Do Uygulaması")
window.geometry("600x500")
window.configure(bg="#f0f0f0")  # arkaplan

current_theme = "light" # tema bilgisi

def apply_theme():
    if current_theme == "light":
        bg = "#f0f0f0"
        fg = "black"
        button_bg = "#4caf50"
        delete_bg1 = "#f44336"
        delete_bg2 = "#9c27b0"
        complete_bg = "#2196f3"
        done_fg = "gray"
    else:  # dark theme
        bg = "#2e2e2e"
        fg = "white"
        button_bg = "#388e3c"
        delete_bg1 = "#d32f2f"
        delete_bg2 = "#7b1fa2"
        complete_bg = "#1976d2"
        done_fg = "#aaaaaa"

    # Arka planlar
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

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()


# --- GÖREV EKLEME ---
def add_task():
    task_text = entry.get()
    if task_text != "":
        task = task_text
        todo.add_task(task)
        entry.delete(0, tk.END)
        update_lists()
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")

# --- GÖREVİ SİL ---
def delete_task(listbox, done=False):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        actual_index = get_actual_index(index, done)
        todo.delete_task(actual_index + 1)
        update_lists()

# --- GÖREVİ TAMAMLANDI OLARAK İŞARETLE ---
def mark_done():
    selected = listbox_pending.curselection()
    if selected:
        index = selected[0]
        actual_index = get_actual_index(index, done=False)
        todo.mark_done(actual_index + 1)
        update_lists()

# --- GÖREVLERİ AYRI LİSTELE ---
def update_lists():
    listbox_pending.delete(0, tk.END)
    listbox_done.delete(0, tk.END)

    for i, task in enumerate(todo.tasks):
        if task["done"]:
            # Görev metnine üstü çizili havası veren stil
            display_text = f"✔️{task['task']}"
            listbox_done.insert(tk.END, display_text)
        else:
            listbox_pending.insert(tk.END, task["task"])
        
    
    label_status.config(
    text=f"{sum(not t['done'] for t in todo.tasks)} görev kaldı · {sum(t['done'] for t in todo.tasks)} tamamlandı")


theme_button = tk.Button(window, text="🌙 Tema Değiştir", command=toggle_theme, font=("Arial", 10))
theme_button.pack(pady=5)

# --- GÖREV İNDEKSİ HESAPLAMA ---
def get_actual_index(index_in_box, done):
    filtered = [i for i, t in enumerate(todo.tasks) if t["done"] == done]
    return filtered[index_in_box]
# BAŞLIK
title = tk.Label(window, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12), width=50)
entry.pack(pady=5)

add_button = tk.Button(window, text="➕ Görev Ekle", command=add_task, bg="#4caf50", fg="white", font=("Arial", 11))
add_button.pack(pady=5)

# --- LİSTELER ---
frame_lists = tk.Frame(window, bg="#f0f0f0")
frame_lists.pack(pady=10)

label1 = tk.Label(frame_lists, text="Yapılacaklar", font=("Arial", 12, "bold"), bg="#f0f0f0")
label1.grid(row=0, column=0, padx=20)

label2 = tk.Label(frame_lists, text="Tamamlananlar", font=("Arial", 12, "bold"), bg="#f0f0f0")
label2.grid(row=0, column=1, padx=20)

listbox_pending = tk.Listbox(frame_lists, width=30, height=10, font=("Arial", 10))
listbox_pending.grid(row=1, column=0, padx=20)

listbox_done = tk.Listbox(frame_lists, width=30, height=10, font=("Arial", 10), fg="gray")
listbox_done.grid(row=1, column=1, padx=20)

# --- BUTONLAR ---
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

done_button = tk.Button(button_frame, text="✅ Tamamla", command=mark_done, bg="#2196f3", fg="white", font=("Arial", 11))
done_button.grid(row=0, column=0, padx=10)

delete_button1 = tk.Button(button_frame, text="🗑️ Yapılacak Sil", command=lambda: delete_task(listbox_pending, False), bg="#f44336", fg="white", font=("Arial", 11))
delete_button1.grid(row=0, column=1, padx=10)

delete_button2 = tk.Button(button_frame, text="🗑️ Tamamlanan Sil", command=lambda: delete_task(listbox_done, True), bg="#9c27b0", fg="white", font=("Arial", 11))
delete_button2.grid(row=0, column=2, padx=10)

label_status = tk.Label(window, text="", font=("Arial", 10), bg="#f0f0f0", fg="black")
label_status.pack(pady=5)


# --- BAŞLANGIÇTA GÖREVLERİ YÜKLE ---
update_lists()
window.mainloop()
apply_theme()

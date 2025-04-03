# todo.py
import json
import os

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("Henüz hiç görev eklenmedi.")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
            self.save_tasks()
        except IndexError:
            print("Geçersiz görev numarası!")

    def mark_done(self, index):
        try:
            self.tasks[index - 1]["done"] = True
            self.save_tasks()
        except IndexError:
            print("Geçersiz görev numarası!")

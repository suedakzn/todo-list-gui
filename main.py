# main.py
from todo import ToDoList

def menu():
    print("\n------- TO-DO UYGULAMASI -------")
    print("1. Görevleri Listele")
    print("2. Görev Ekle")
    print("3. Görev Sil")
    print("4. Görevi Tamamla")
    print("5. Çıkış Yap")

todo = ToDoList()

while True:
    menu()
    choice = input("Seçiminiz (1-5): ").strip()
    print(f"[DEBUG] Seçilen: {choice}")  # Hangi sayı girilmiş, görelim

    if choice == "1":
        todo.list_tasks()
    elif choice == "2":
        task = input("Yeni görev girin: ")
        todo.add_task(task)
    elif choice == "3":
        try:
            index = int(input("Silinecek görev numarası: "))
            todo.delete_task(index)
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
    elif choice == "4":
        try:
            index = int(input("Tamamlanan görev numarası: "))
            todo.mark_done(index)
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
    elif choice == "5":
        print("Programdan çıkılıyor...")
        break
    else:
        print("⚠️ Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")

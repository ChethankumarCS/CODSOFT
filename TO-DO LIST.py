# ✅ Enhanced To-Do List Program with Emojis
# 🧑‍💻 Author: Abhi (Human-coded vibe)

todo_list = []

def show_menu():
    print("\n✨ ----- TO-DO LIST MENU ----- ✨")
    print("1️⃣  Add a New Task")
    print("2️⃣  View All Tasks")
    print("3️⃣  Mark a Task ✅ as Done")
    print("4️⃣  Delete a Task 🗑")
    print("5️⃣  Exit 🚪")

while True:
    show_menu()
    choice = input("\n👉 Enter your choice (1-5): ")

    if choice == '1':
        task = input("📝 Enter a new task: ")
        todo_list.append({"task": task, "done": False})
        print("✅ Task added successfully!")

    elif choice == '2':
        print("\n📋 Your Tasks:")
        if not todo_list:
            print("😶 No tasks yet. Add something!")
        else:
            for i, item in enumerate(todo_list, 1):
                status = "✔ Done" if item["done"] else "❌ Not Done"
                print(f"{i}. {item['task']} — {status}")

    elif choice == '3':
        if not todo_list:
            print("⚠ No tasks to update.")
            continue
        try:
            task_num = int(input("✅ Enter task number to mark as done: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]["done"] = True
                print("🎉 Task marked as done!")
            else:
                print("❗ Invalid task number.")
        except ValueError:
            print("❗ Please enter a valid number.")

    elif choice == '4':
        if not todo_list:
            print("⚠ No tasks to delete.")
            continue
        try:
            task_num = int(input("🗑 Enter task number to delete: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"🗑 Deleted task: {removed['task']}")
            else:
                print("❗ Invalid task number.")
        except ValueError:
            print("❗ Please enter a valid number.")

    elif choice == '5':
        print("👋 Exiting... Have a productive day, Abhi!")
        break

    else:
        print("⚠ Please enter a valid choice (1-5).")
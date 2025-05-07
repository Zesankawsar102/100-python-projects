class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("Welcome to")
        print(" To-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append(task)
        print("Task added.")

    def remove_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(self.tasks):
                removed = self.tasks.pop(task_num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-4): ")
            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                print("Goodbye!See you agin")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = ToDoList()
    app.run()

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully!")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Quitting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

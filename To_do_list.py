# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")
            

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
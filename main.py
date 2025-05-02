import db
from datetime import datetime

def menu():
    while True:
        print("-----To-Do List Manager------")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks only")
        print("4. Mark Task as Complete")
        print("6. Exit")

        choice = input("Enter your option: ")

        if choice == '1':
            title = input("Enter the task title:  ")
            due_date = input("Enter the due date (YYYY-MM-DD):  ")
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                db.add_task(title,due_date)
            except ValueError:
                print("Invalid date format. Please enter YYYY-MM-DD. \n")

        elif choice == '2':
            db.view_tasks()

        elif choice == '3':
            db.view_tasks(only_pending=True)

        elif choice == '4':
            task_id = input("Enter the task ID to mark as complete: ")
            db.mark_complete(task_id)

        elif choice == '5':
            task_id = input("Enter task ID to delete: ")
            db.delete_task(task_id)

        elif choice == '6':
            db.close_connection()
            print("Goodbye!")
            break

        else:
            print("Invalid choice man. Try again.")




if __name__ == "__main__":
    menu()

    



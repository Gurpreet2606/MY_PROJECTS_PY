tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            number_text = input("Enter task number to remove: ")

            if number_text.isdigit():
                number = int(number_text)
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print("Removed:", removed)
                else:
                    print("Invalid task number.")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("THANKS FOR USING THE TO-DO LIST!")
        break

    else:
        print("Invalid choice. Please try again.")
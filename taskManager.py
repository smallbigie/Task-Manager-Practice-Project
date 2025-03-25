

def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add a Task")
    print("2. Add a step to a Task")
    print("3. Mark Step as Completed")
    print("4. View All Tasks")
    print("5. Remove a Task")
    print("6. Display Total Number of Tasks")
    print("7. Quit")


def add_task(tasks):
    task_name = input("Enter the task name: ").strip()
    if task_name in tasks:
        print(f"Task '{task_name}' already ixists.")
    else:
        tasks[task_name] = [] 
        print(f"Task '{task_name}' added successfully.")


def add_step(tasks):
    task_name = input ("Enter the task name to add a step to: ").strip()
    if task_name not in tasks:
        print(f"Task '{task_name}' does not exist.")
        return
    step_description = input(" Enter the step description: ").strip()


def mark_step_completed(tasks):
    task_name = input("Enter the task name to mark a step as completed: ").strip()
    if task_name not in tasks:
        print(f"Task '{task_name}' does not exist.")
        return
    step_description = input("Enter the step description to mark as completed: ").strip()
    steps = tasks[task_name]
    found = False
    for step in steps:
        if step["description"] == step_description:
            step["status"] = "completed"
            print(f"Step '{step_description}' in task '{task_name}' marked as completed.")
            found = True
            break
    if not found:
        print(f"Step '{step_description}' not found in task '{task_name}'.")

        
def view_all_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\n--- All Tasks ---")
    for task, steps in tasks.items():
        print(f"Task: {task}")
        if steps:
            for step in steps:
                print(f" - Step: {step['description']} | Status: {step['status']}")
        else:
            print(" - No steps added yet.")


def remove_task(tasks):
    task_name = input("Enter the task name to remove: ").strip()
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' removed successfully.")
    else:
        print(f"Task '{task_name}' does not exist.")


def display_total_tasks(tasks):
    total = len(tasks)
    print(f"Total number of tasks: {total}")


def main():
    tasks = {}
    while True:
        display_menu()
        option = input("Choose an option (1-7): ").strip()
        if option == "1":
            add_task(tasks)
        elif option == "2":
            add_step(tasks)
        elif option == "3":
            mark_step_completed(tasks)
        elif option == "4":
            view_all_tasks(tasks)
        elif option == "5":
            remove_task(tasks)
        elif option == "6":
            display_total_tasks(tasks)
        elif option == "7":
            print("Exiting the system. Goodbye")
            break
        else:
            print("Invalid option. Please choose a valid option (1-7).")


if __name__ == "__main__":
    main()


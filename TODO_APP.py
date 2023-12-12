# Initialize an empty dictionary to store tasks
tasks = {}

def add_task(task_name):
    """Add a task to the to-do list."""
    tasks[task_name] = False  # False indicates task is not completed
    print(f'Task "{task_name}" added.')

def delete_task(task_name):
    """Delete a task from the to-do list."""
    if task_name in tasks:
        del tasks[task_name]
        print(f'Task "{task_name}" deleted.')
    else:
        print(f'Task "{task_name}" not found.')

def display_tasks():
    """Display the current to-do list."""
    if not tasks:
        print('No tasks in the to-do list.')
    else:
        print('To-Do List:')
        for task, completed in tasks.items():
            status = "Completed" if completed else "Not Completed"
            print(f'- {task} ({status})')

def mark_as_complete(task_name):
    """Mark a task as complete."""
    if task_name in tasks:
        tasks[task_name] = True
        print(f'Task "{task_name}" marked as complete.')
    else:
        print(f'Task "{task_name}" not found.')

# Example usage:
add_task("Buy groceries")
add_task("Complete homework")
add_task("Go for a run")

display_tasks()

mark_as_complete("Buy groceries")

display_tasks()

delete_task("Complete homework")

display_tasks()


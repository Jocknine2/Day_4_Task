from modules.input import *
from modules.task_list import *
from modules.output import *
from data.task_list import *

print_menu()
while True:
    option = get_user_option()
    if option.lower() == "q":
        break
    if option == "1":
        print_list(tasks)
    elif option == "2":
        print_list(get_uncompleted_tasks(tasks))
    elif option == "3":
        print_list(get_completed_tasks(tasks))
    elif option == "4":
        option = get_user_description()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == "5":
        time = get_user_duration
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == "6":
        option = get_user_description()
        print(get_task_with_description(tasks, description))
    elif option == "7":
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")

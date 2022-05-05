tasks = [
    {"description": "Wash Dishes", "completed": False, "time_taken": 10},
    {"description": "Clean Windows", "completed": False, "time_taken": 15},
    {"description": "Make Dinner", "completed": True, "time_taken": 30},
    {"description": "Feed Cat", "completed": False, "time_taken": 5},
    {"description": "Walk Dog", "completed": True, "time_taken": 60},
]

# Functions to complete:

## Get a list of completed tasks
def get_completed_tasks(list):
    found = []

    for task in tasks:
        if task["completed"] == True:
            found.append(task)

    return found


print(get_completed_tasks(tasks))

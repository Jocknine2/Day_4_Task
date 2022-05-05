from start_code.app import *
from start_code.output import *


tasks = [
    {"description": "Wash Dishes", "completed": False, "time_taken": 10},
    {"description": "Clean Windows", "completed": False, "time_taken": 15},
    {"description": "Make Dinner", "completed": True, "time_taken": 30},
    {"description": "Feed Cat", "completed": False, "time_taken": 5},
    {"description": "Walk Dog", "completed": True, "time_taken": 60},
]

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    found = []

    for task in list:
        if task["completed"] == False:
            found.append(task)

    return found


print(get_uncompleted_tasks(tasks))

## Get a list of completed tasks
def get_completed_tasks(list):
    found = []

    for task in list:
        if task["completed"] == True:
            found.append(task)

    return found


print(get_completed_tasks(tasks))
print("_______________________________________")


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):

    for times in list:
        if times["time_taken"] == time:

            return times


print(get_tasks_taking_at_least(tasks, 5))
print("_______________________________________")


## Find a task with a given description
def get_task_with_description(list, description):

    for task in list:
        if task["description"] == description:

            return task


print(get_task_with_description(tasks, "Make Dinner"))


# Extention (Function):

## Get a list of tasks by status
def get_tasks_by_status(list, status):

    status_list = []

    for stat in list:
        if stat["completed"] == status:
            status_list.append(stat)

    return stat and print(status_list)


print(get_tasks_by_status(tasks, True))

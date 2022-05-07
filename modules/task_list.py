# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    found = []

    for task in list:
        if task["completed"] == False:
            found.append(task)

    return found


## Get a list of completed tasks
def get_completed_tasks(list):
    found = []

    for task in list:
        if task["completed"] == True:
            found.append(task)

    return found


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    tasks = []
    for task in list:
        if task["time_taken"] >= time:
            tasks.append(task)

    return tasks


## Find a task with a given description
def get_task_with_description(list, description):

    for task in list:
        if task["description"] == description:

            return task
    return None


# Extention (Function):

## Get a list of tasks by status
def get_tasks_by_status(list, status):

    status_list = []

    for stat in list:
        if stat["completed"] == status:
            status_list.append(stat)

    return stat

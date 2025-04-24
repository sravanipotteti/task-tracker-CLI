import sys
import os
import json

#file where tasks will be saved
TASKS_FILE = "tasks.json"

#load tasks from the file 
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE,"r") as file:
        return json.load(file)

#save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks,file,indent=2)


#add new task
def add_task(title):
    tasks=load_tasks()
    task_id=tasks[-1]["id"] +1 if tasks else 1
    new_task={
        "id": task_id,
        "title": title,
        "status": "todo"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added:",task_id,title)

#list all tasks
def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if not tasks:
        print("No tasks with status:", filter_status)
        return

    print("Tasks:")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} - {task['status']}")


#update the title of the task
def update_task(task_id, new_title):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            save_tasks(tasks)
            print(f" Task [{task_id}] updated to: {new_title}")
            return
    print(f" Task with ID {task_id} not found.")

#marks the tasks as done, in-progress,not-done 
def mark_task(task_id, status):
    valid_statuses = ["in-progress", "done", "not-done"]
    if status not in valid_statuses:
        print(f" Invalid status. Use one of: {', '.join(valid_statuses)}")
        return

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "todo" if status == "not-done" else status
            save_tasks(tasks)
            print(f" Task [{task_id}] marked as {task['status']}")
            return
    print(f" Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(updated_tasks):
        print(f"Task with ID {task_id} not found.")
        return

    save_tasks(updated_tasks)
    print(f" Task [{task_id}] deleted.")



def main():
    if len(sys.argv)<2:
        print("Usage: python tracker.py <command> [arguments]")
        return
    command=sys.argv[1]

    if command=="add":
        if len(sys.argv)<3:
            print("Error:Please provide a task title")
            return
        title = " ".join(sys.argv[2:])
        add_task(title)
    elif command=="list":
        if len(sys.argv) == 2:
            list_tasks()
        else:
            status = sys.argv[2]
            valid_status = ["done", "not-done", "in-progress", "todo"]
            if status not in valid_status:
                print("invalid status:",status)
            else:
                list_tasks(status)
    elif command == "update":
        if len(sys.argv) < 4:
            print(" Usage: python tracker.py update <task_id> <new_title>")
            return
        try:
            task_id = int(sys.argv[2])
            new_title = " ".join(sys.argv[3:])
            update_task(task_id, new_title)
        except ValueError:
            print(" Task ID must be a number.")
    elif command == "mark":
        if len(sys.argv) != 4:
            print(" Usage: python tracker.py mark <task_id> <status>")
            return
        try:
            task_id = int(sys.argv[2])
            status = sys.argv[3]
            mark_task(task_id, status)
        except ValueError:
            print("Task ID must be a number.")
    
    elif command == "delete":
        if len(sys.argv) != 3:
            print("Usage: python tracker.py delete <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Task ID must be a number.")


    else:
        print("Unknown command:",command)

if __name__=="__main__":
    main()
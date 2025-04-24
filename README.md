#  Task Tracker CLI

A simple command-line interface (CLI) project to track your tasks — including adding, updating, marking, and listing tasks.

##  Features

- Add tasks
- Update task titles
- Delete tasks
- Mark tasks as `in-progress`, `done`, or `not-done`
- List all tasks or filter by status

##  How to Use

1. **Run any command from the terminal** using:


###  Commands

| Command | Usage Example | Description |
|--------|----------------|-------------|
| `add` | `python tracker.py add "Buy groceries"` | Adds a new task |
| `list` | `python tracker.py list` | Lists all tasks |
| `list done` | `python tracker.py list done` | Lists only done tasks |
| `list in-progress` | `python tracker.py list in-progress` | Lists only in-progress tasks |
| `update` | `python tracker.py update 1 "Read a book"` | Updates task with ID 1 |
| `mark` | `python tracker.py mark 1 done` | Marks task 1 as done |
| `delete` | `python tracker.py delete 1` | Deletes task with ID 1 |

##  Task Storage

All tasks are saved in a file named `tasks.json` in the current directory.

##  Requirements

- Python 3.x
- No external libraries required

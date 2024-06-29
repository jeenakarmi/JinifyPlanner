# 🗒️ Jinify Planner

This is a simple To-Do application built using Django framework with PostgreSQL as database. This application allows users to create, read and delete tasks.

## Getting Started
### Prerequisites

- Python 3.x
- Django
- Bootstrap v5.0
- PostgreSQL
- psycopg2

### Install Dependencies:

1. Install the project dependencies within the virtual environment:

    ```
    pip install -r requirement.txt
    ```

## ✨ Features

- Create a new task.
- View a list of all tasks.
- Delete tasks.

## 🛠️ Built With

- Django - The web framework used
- PostgreSQL - Database management system

## 📁 App structure
```
● Todo_Project
|
+---● todos (app folder)
|   |
|   +--● migrations (includes files related to migrations)
|   | 
|   +--● templates
|   |  |--● todos
|   |  |  |--todo_list.html
|   | 
|   |-- models.py (python class for each database table)
|   |-- urls.py (app. specific url mapping)
|   |-- views.py (view fns. to handle http request)
|
+---● Todo_Project
|   |
|   |--setting.py (project config. file)
|   |--urls.py (url mapping for the project)
```

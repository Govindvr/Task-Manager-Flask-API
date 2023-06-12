# Task-Manager-Flask-API
Flask REST API for Task Management which perform CRUD operations on  psql database.

Python version used : `3.10.6`

## Setup
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Create a `.env` and add the following variables
```bash
DATABASE_URI=<postgresql://username:password@host/name>

```
5. Perform the migrations
```bash
flask db init
flask db migrate
flask db upgrade
```

To install the required packages
```bash
pip  install -r requirements.txt
```
To Run the app
```bash
python run.py
```

The app will be availiable on http://localhost:5000/

## API Endpoints
1. GET /api/tasks - Returns a list of all tasks.
2. GET /api/tasks/<id> - Returns the task with the specified ID.
3. POST /api/tasks - Creates a new task with the specified data.
4. PUT /api/tasks/<id> - Updates the task with the specified ID with the new data.
5. DELETE /api/tasks/<id> - Deletes the user with the specified ID.
6. PUT /api/tasks/<id>/status - Updates the status of the task with the specified ID.

## API Request Format
1. POST /tasks
```json
{
        "title": "String",
        "description": "String",
        "due_date": "yy-mm-dd",      
    }
```
2. PUT /tasks/<id>
```json
{
        "title": "String",
        "description": "String",
        "due_date": "yy-mm-dd",      
    }
```
3. PUT /tasks/<id>/status
```json
{
        "status": "String",     
    }
```

## Testing Results

![Alt text](screenshots/gettask.png?raw=true "GET")
![Alt text](screenshots/gettaskid.png?raw=true "GET ID")
![Alt text](screenshots/posttask.png?raw=true "POST")
![Alt text](screenshots/puttaskstatus.png?raw=true "PUT")


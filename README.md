# Log Summariser
**Overview**
This project contains a Log Summariser that reads a list of log entries and produces a summary.
Each log entry includes a timestamp, a level (INFO, WARN, ERROR), and a message.
**The summariser provides:**
Total count of each log level
The most recent ERROR message
Ability to filter logs by a specific level
Unit tests are included to verify all behaviours.

# What the Summariser Does
Counts how many INFO, WARN, and ERROR logs exist.
Ignores any log entries that have no level.
Finds the latest ERROR message based on timestamp.
Supports filtering so you can view only logs of a certain level, like only ERROR logs.
Returns both the counts and the latest error message.
Unit Tests Included
**The following scenarios are tested:**
Correct counting of INFO, WARN, and ERROR logs
Handling logs where the level is missing
Detecting the most recent error log
Behaviour when there are no error logs
Handling an empty log list
Filtering logs by level
Running the file will execute all the tests and print a success message for each.
**Output of this Log Summariser**
When the summariser is run on sample logs, it returns:
A dictionary with counts of INFO, WARN, and ERROR logs
The latest error message (or None if there are no errors)



# Resilient In-Memory API Implementation 
**This project demonstrates how to build a resilient, production-ready Python REST API using:**
FastAPI
Conda environment & environment.yml
In-memory data storage
Pydantic validation
Middleware for request timing
Pytest-based test automation
Podman containerization (rootless)
Systemd service for auto-start on boot
The API stores data in-memory, meaning data exists only while the application is running.

# Conda Environment Setup:
**Create environment:**
conda create -n myenv python=3.10 -y
conda activate myenv
**Install dependencies:**
pip install fastapi uvicorn pytest

**Export environment file:**
conda env export > environment.yml

# API Implementation
# 1. In-Memory Storage
The API does not use any database.
Instead, it keeps all book information inside a Python list.
This list behaves like temporary storage:
Each time the server starts, the list is empty.
When a book is added, it is stored inside this list.
When the /books API endpoint is called, it returns the entire list.
This design is simple and suitable for lightweight API demonstrations.

# 2. main.py - API Routes
The main.py file contains:
**Application Initialization**
A FastAPI application object is created.
**Middleware Setup**
A separate middleware function (from another file) is attached to the app.
**Data Storage**
An empty list named books is created to hold all book entries.
**API Endpoints**
The file defines two API routes:
**GET /books**
Returns the current list of books.
Useful to view all items stored in memory.
**POST /books**
Accepts a new book entry.
Validates the input using the Book model.
Adds the book to the in-memory list.
Returns a success message along with the added book.
This setup forms a basic CRUD-style API with two operations (read + create).

# 3. models.py - Data Validation Using Pydantic
This file defines a Book model using Pydantic, which ensures every book follows the correct structure.
Each book entry must include:
an id (a number)
a title (text)
an author (text)
When the API receives data, Pydantic automatically checks if all fields are valid.
If anything is missing or incorrect, FastAPI automatically returns an error.

# 4. middleware.py - Custom Middleware
Middleware is used to execute code before and after each request.
**This middleware captures:**
the time when a request starts
the time when it finishes
calculates how long the request took
attaches that timing information inside a response header (X-Process-Time)
This helps measure request performance and is useful during debugging or optimization.

# 5. Testing Using Pytest
The project includes automated tests to verify the API behavior.
**Test Setup**
A test client is created using the FastAPI testing utility.
It behaves like a real user sending requests to the API.

# Test Cases
1. Test GET /books
Sends a GET request to the /books endpoint.
Checks that the API responds with HTTP status 200, meaning success.
2. Test POST /books
Sends a POST request to add a book.
Verifies:
status code is 200
data returned by the API contains the correct book title
These tests ensure the API works correctly and handles requests as expected.

**Running Tests**
All test cases can be executed with:
pytest -v
This runs the tests in verbose mode, showing detailed output.

# 5. Podman Containerization
Build container
podman build -t api-service .
Run container
podman run -d --name my-api -p 8000:8000 api-service
Check logs
podman logs my-api

# 6. Generate Systemd Unit File (Auto-Start on Boot)
**Generate systemd file**
podman generate systemd --name my-api --files
**It creates:**
container-my-api.service
**Move it to systemd user folder:**
mv container-my-api.service ~/.config/systemd/user/
**Enable service**
systemctl --user enable --now container-my-api.service
**Verify status**
systemctl --user status container-my-api.service
**Save output to:**
systemctl --user status container-my-api.service > systemd_status.txt
systemd_status.txt

# 7. How to Use the API
Start service
systemctl --user start container-my-api.service
GET books
GET http://localhost:8000/books
POST book
POST http://localhost:8000/books
{
  "id": 1,
  "title": "My Book",
  "author": "Sanju"
}
from flask import Flask, jsonify, request
import logging
import mysql.connector

todolist = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# sample data
tasks = [
   {"id": 1, "task": "python basics", "status": "completed"},
   {"id": 2, "task": "conditions in python", "status": "not completed"}
]


# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",      # Change if MySQL is hosted elsewhere
    user="root",  # Replace with your MySQL username
    password="root",  # Replace with your MySQL password
)

# Create a cursor object to execute queries
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS task_db")
cursor.execute("USE task_db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status VARCHAR(100) NOT NULL
    )
""")
conn.commit()

# POST endpoint to add a new task
@todolist.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    if not new_task or 'task' not in new_task or 'status' not in new_task:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        cursor.execute("INSERT INTO tasks (task, status) VALUES (%s, %s)", 
                       (new_task['task'], new_task['status']))
        conn.commit()
        return jsonify({"message": "Task added successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


# GET: Retrieve tasks (all or filtered by ID, task, status)
@todolist.route('/tasks', methods=['GET'])
def get_tasks():
    task_id = request.args.get('id', type=int)
    task = request.args.get('task', type=str)
    status = request.args.get('status', type=str)

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if task_id:
        query += " AND id = %s"
        params.append(task_id)
    if task:
        query += " AND task = %s"
        params.append(task)
    if status:
        query += " AND status = %s"
        params.append(status)

    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        return jsonify(results)
    return jsonify({"error": "No matching task found"}), 404


# PUT: Update a task by ID,task,status
@todolist.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    update_data = request.json
    if not update_data:
        return jsonify({"error": "No data provided for update"}), 400

    update_fields = ", ".join(f"{key} = %s" for key in update_data.keys())
    values = list(update_data.values()) + [task_id]

    query = f"UPDATE tasks SET {update_fields} WHERE id = %s"

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task updated successfully"})
    
 # DELETE: Remove a task by ID
@todolist.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted successfully"}), 200
   
# Ensure Flask runs correctly
if __name__ == '__main__':
    todolist.run(debug=True)
    
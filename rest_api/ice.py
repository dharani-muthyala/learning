from flask import Flask, jsonify, request
import logging
import mysql.connector

ice = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
# Sample data
icecreams = [
    {"id": 1, "flavour": "chocolate", "parlour": "magic restro"},
    {"id": 2, "flavour": "strawberry", "parlour": "ibaco"}
]


# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",      # Change if MySQL is hosted elsewhere
    user="root",  # Replace with your MySQL username
    password="root",  # Replace with your MySQL password
)

# Create a cursor object to execute queries
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS database_db")
cursor.execute("USE database_db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS icecreams (
        id INT AUTO_INCREMENT PRIMARY KEY,
        flavour VARCHAR(50) NOT NULL,
        parlour VARCHAR(100) NOT NULL
    )
""")
conn.commit()


# POST endpoint to add a new ice cream
@ice.route('/icecreams', methods=['POST'])
def add_icecream():
    new_icecream = request.json
    if not new_icecream or 'flavour' not in new_icecream or 'parlour' not in new_icecream:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        cursor.execute("INSERT INTO icecreams (flavour, parlour) VALUES (%s, %s)", 
                       (new_icecream['flavour'], new_icecream['parlour']))
        conn.commit()
        return jsonify({"message": "Ice cream added successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


# GET: Retrieve ice creams (all or filtered by ID, flavour, parlour)
@ice.route('/icecreams', methods=['GET'])
def get_icecreams():
    icecream_id = request.args.get('id', type=int)
    flavour = request.args.get('flavour', type=str)
    parlour = request.args.get('parlour', type=str)

    query = "SELECT * FROM icecreams WHERE 1=1"
    params = []

    if icecream_id:
        query += " AND id = %s"
        params.append(icecream_id)
    if flavour:
        query += " AND flavour = %s"
        params.append(flavour)
    if parlour:
        query += " AND parlour = %s"
        params.append(parlour)

    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        return jsonify(results)
    return jsonify({"error": "No matching ice cream found"}), 404



# PUT: Update an ice cream by ID
@ice.route('/icecreams/<int:icecream_id>', methods=['PUT'])
def update_icecream(icecream_id):
    update_data = request.json
    if not update_data:
        return jsonify({"error": "No data provided for update"}), 400

    update_fields = ", ".join(f"{key} = %s" for key in update_data.keys())
    values = list(update_data.values()) + [icecream_id]

    query = f"UPDATE icecreams SET {update_fields} WHERE id = %s"

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Ice cream not found"}), 404

    return jsonify({"message": "Ice cream updated successfully"})

# DELETE: Remove an ice cream by ID
@ice.route('/icecreams/<int:icecream_id>', methods=['DELETE'])
def delete_icecream(icecream_id):
    cursor.execute("DELETE FROM icecreams WHERE id = %s", (icecream_id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Ice cream not found"}), 404

    return jsonify({"message": "Ice cream deleted successfully"}), 200

# Ensure Flask runs correctly
if __name__ == '__main__':
    ice.run(debug=True)

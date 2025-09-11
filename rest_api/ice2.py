from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

ice2 = Flask(__name__)

# Configure MySQL database connection
ice2.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/database3_db'
ice2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(ice2)

# Define IceCream Model
class IceCream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavour = db.Column(db.String(100), nullable=False)
    parlour = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "flavour": self.flavour, "parlour": self.parlour}

# Create the database tables
with ice2.app_context():
     db.create_all()
     

# POST endpoint to add a new ice cream
@ice2.route('/icecreams', methods=['POST'])
def add_icecream():
    data = request.json
    if not data or 'id' not in data or 'flavour' not in data or 'parlour' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if the ID already exists
    existing_icecream = IceCream.query.get(data['id'])
    if existing_icecream:
        return jsonify({"error": "Ice cream with this ID already exists."}), 400

    new_icecream = IceCream(id=data['id'], flavour=data['flavour'], parlour=data['parlour'])
    db.session.add(new_icecream)
    db.session.commit()

    return jsonify(new_icecream.to_dict()), 201

# GET method for retrieving ice creams
@ice2.route('/icecreams', methods=['GET'])
def get_icecreams():
    icecream_id = request.args.get('id', type=int)
    flavour = request.args.get('flavour', type=str)
    parlour = request.args.get('parlour', type=str)

    query = IceCream.query
    if icecream_id:
        query = query.filter_by(id=icecream_id)
    if flavour:
        query = query.filter_by(flavour=flavour)
    if parlour:
        query = query.filter_by(parlour=parlour)

    icecreams = query.all()
    if icecreams:
        return jsonify([icecream.to_dict() for icecream in icecreams])
    return jsonify({"error": "No matching ice cream found"}), 404

# PUT (Update ice cream)
@ice2.route('/icecreams/<int:icecream_id>', methods=['PUT'])
def update_icecream(icecream_id):
    data = request.json
    icecream = IceCream.query.get(icecream_id)

    if not icecream:
        return jsonify({"error": "Ice cream not found"}), 404

    if 'flavour' in data:
        icecream.flavour = data['flavour']
    if 'parlour' in data:
        icecream.parlour = data['parlour']

    db.session.commit()
    return jsonify(icecream.to_dict())

# DELETE (Delete ice cream)
@ice2.route('/icecreams/<int:icecream_id>', methods=['DELETE'])
def delete_icecream(icecream_id):
    icecream = IceCream.query.get(icecream_id)

    if not icecream:
        return jsonify({"error": "Ice cream not found"}), 404

    db.session.delete(icecream)
    db.session.commit()
    return jsonify({"deleted_item": icecream.to_dict()}), 200

# Run Flask ice2
if __name__ == '__main__':
    ice2.run(debug=True)

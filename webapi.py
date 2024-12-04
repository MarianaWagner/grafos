from social_network import SocialNetwork
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Create Flask app and social network instance
app = Flask(__name__)
CORS(app)
network = SocialNetwork()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/add_connection', methods=['POST'])
def add_connection():
    """API endpoint to add a connection."""
    data = request.json
    user1 = data.get('user1')
    user2 = data.get('user2')
    
    if not user1 or not user2:
        return jsonify({"error": "Both users are required"}), 400
    
    result = network.add_connection(user1, user2)
    return jsonify({"message": result})

@app.route('/remove_connection', methods=['POST'])
def remove_connection():
    """API endpoint to remove a connection."""
    data = request.json
    user1 = data.get('user1')
    user2 = data.get('user2')
    
    if not user1 or not user2:
        return jsonify({"error": "Both users are required"}), 400
    
    result = network.remove_connection(user1, user2)
    return jsonify({"message": result})

@app.route('/is_connected', methods=['POST'])
def check_connection():
    """API endpoint to check connection between users."""
    data = request.json
    user1 = data.get('user1')
    user2 = data.get('user2')
    
    if not user1 or not user2:
        return jsonify({"error": "Both users are required"}), 400
    
    result = network.is_connected(user1, user2)
    return jsonify({"connected": result})

@app.route('/list_connections', methods=['POST'])
def list_user_connections():
    """API endpoint to list connections for a user."""
    data = request.json
    user = data.get('user')
    
    if not user:
        return jsonify({"error": "User is required"}), 400
    
    connections = network.list_connections(user)
    return jsonify({"connections": connections})

@app.route('/mutual_connections', methods=['POST'])
def find_mutual_connections():
    """API endpoint to find mutual connections."""
    data = request.json
    user1 = data.get('user1')
    user2 = data.get('user2')
    
    if not user1 or not user2:
        return jsonify({"error": "Both users are required"}), 400
    
    mutual = network.find_mutual_connections(user1, user2)
    return jsonify({"mutual_connections": mutual})

@app.route('/connection_degree', methods=['POST'])
def get_connection_degree():
    """API endpoint to get connection degree."""
    data = request.json
    user = data.get('user')
    
    if not user:
        return jsonify({"error": "User is required"}), 400
    
    degree = network.get_connection_degree(user)
    return jsonify({"connection_degree": degree})

if __name__ == '__main__':
    app.run(debug=True)

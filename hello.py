from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/messages', methods=['GET'])
def get_message():
    # This function will be executed when a GET request is made to '/messages'
    return jsonify(message="GET Request: Hello World")

# Define a route that handles POST requests
@app.route('/messages', methods=['POST'])
def post_message():
    # Extract JSON data from the POST request
    data = request.json  # Assume JSON data is sent with POST
    # This function will be executed when a POST request is made to '/messages'
    # It assumes that the JSON contains a 'message' key
    return jsonify(message=f"POST Request: Received your message: {data['message']}"), 201


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request

app = Flask(__name__) # Needed so Flask knows where to look for resources

@app.route('/')
def hello_world():
    return render_template('index.html')

# POST API endpoint which is recieving the request
# and then it sends a response
@app.route('/apipost', methods=['POST'])
def post_data():
    data = request.json  # Assuming the request body contains JSON data
    first_name = data.get('first_name')
    # Process the first name...
    return jsonify({'message': f'Hello, {first_name}!'})

@app.route('/apiget', methods = ['GET'])
def get():
    return jsonify ('first_name')

if __name__ == '__main__':
    app.run(debug=True)



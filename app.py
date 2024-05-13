from flask import Flask

app = Flask(__name__) # Needed so Flask knows where to look for resources

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! This is my app running on PythonAnywhere."

if __name__ == "__main__":
    app.run()

from flask import Flask
import database

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homePage():
    data = database.database().getData()
    return str(data)

@app.route('/healthz', methods=["GET"])
def healthy():
    database.database().getData()
    return 'Hello World'

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=8000)
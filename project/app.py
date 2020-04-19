from flask import Flask, request
from flask_cors import CORS
import jsonpickle
from storage import *

app = Flask(__name__)
CORS(app)

@app.route("/endpoint/test", methods=["GET"])
def TestEndpoint():
    return "This works!"

@app.route("/endpoint/test/database", methods=["GET"])
def TestDatabaseEndpoint():
    data = storage.GetTestDatabase()
    return data

if __name__ == "__main__":
    app.run()
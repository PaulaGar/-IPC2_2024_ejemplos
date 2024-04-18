from flask import Flask, jsonify, request
from flask_cors import CORS

app= Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": ""}})

print("Api en flask")

@app.route("/", methods=['GET'])
def hola():
    return "<h1>first Get</h1>"

@app.route("/leerjson", methods=['GET'])
def leer():
    data=request.json
    print(data)
    print(data["nombre"])
    return jsonify({'mensaje': 'Json leido'})

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000) 
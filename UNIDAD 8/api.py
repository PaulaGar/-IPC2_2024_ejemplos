from flask import Flask, jsonify, request
from flask_cors import CORS

app= Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": ""}})

print("Api en flask")

#Area para almacenar temporalmente la informacion
notas ={}
#Al ser diccionario guarda mediante nombres en lugar id numericos 

@app.route("/", methods=['GET'])
def getNotas():
    return jsonify({"data": notas , "message": "Notas obtenidas exitosamente"})


#Si hacemos doble post o crea un duplicado o da error por posibles validaciones de repitencia
@app.route("/", methods=['POST'])
def postNota():
    carnet= request.json["carnet"]
    nota= request.json["nota"]
    notas[carnet]=nota
    return jsonify({ "message": "Nota cargada exitosamente"})

#En una BD es un update, en este ejemplo se ven iguales por como se manejan los diccionarios
@app.route("/", methods=['PUT'])
def putNota():
    carnet= request.json["carnet"]
    nota= request.json["nota"]
    notas[carnet]=nota
    return jsonify({ "message": "Nota editada exitosamente"})

@app.route("/", methods=['DELETE'])
def deleteNota():
    carnet= request.json["carnet"]
    notas.pop(carnet)
    return jsonify({ "message": "Nota eliminada exitosamente"})

#---------------------------------------------------ERRORES-----------------------------------------------
@app.route("/error", methods=['GET'])
def getError():
    carne= request.json["carne"]
    return jsonify({"data": notas , "message": "Notas obtenidas exitosamente"})

#Rutas para codigos de error
@app.route("/normal", methods=['GET'])
def getNormal():

    return jsonify({"message": "todo normal"}),101
@app.route("/bien", methods=['GET'])
def getBien():
    return jsonify({"message": "todo super bien"}),200

@app.route("/masomenos", methods=['GET'])
def getMasomenos():
    return jsonify({"message": "Hay cosas pendientes por hacer"}),300

@app.route("/mal", methods=['GET'])
def getMal():
    return jsonify({"message": "El cliente ha enviado una informacion erronea"}),400

@app.route("/muymal", methods=['GET'])
def getMuymal():
    return jsonify({"message": "El servidor tronó D:"}),500

@app.route("/home", methods=['GET'])
def hola():
    return "<h1>first Get</h1>"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
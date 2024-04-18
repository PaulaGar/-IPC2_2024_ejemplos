from flask import Flask, request #HACER IMPORTS DE : 
from flask_cors import CORS

app= Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": ""}})

#VECTOR QUE GUARDA LA LISTA DE ESTUDIANTES
Estudiantes =[]

@app.route("/getEstudiantes")
def getStudent():
    if len(Estudiantes)==0:
        return "error",404
    return ({"data":Estudiantes}),200

@app.route("/getIndice/<int:id>")
def getById(id):
    try:
        return Estudiantes[id],200
    except:
        return "Estudiante no existente",404

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        Estudiantes.append(nombre)
        return f'¡Hola {nombre} ! Tu formulario ha sido enviado correctamente.'
    else:
        return '''
        <form method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre"><br>
            <input type="submit" value="Enviar">
        </form>
        '''

@app.route("/getHola")
def getHola():
    return "Hola desde la Api",200

if __name__=="__main__":
    print("Api Corriendo en el Puerto", 5000)
    app.run(host='0.0.0.0', port=5000)
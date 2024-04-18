from flask import Flask
from flask_cors import CORS

app= Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": ""}})


@app.route("/", methods=['GET'])
def hola():
    return """<h1>Hola Mundo</h1>
    """

@app.route("/ejemplo", methods=['GET'])
def tabla():
    return """
<table>
    <tr>
        <td>ESTUDIANTE</td>
        <td>CARNET</td>
        <td>AÑO</td>
    </tr>
    <tr>
        <td>PAULA</td>
        <td>201700823</td>
        <td>2024</td>
    </tr>

</table>
"""

if __name__=="__main__":
    print("Api Corriendo en el Puerto", 5000)
    app.run(host='0.0.0.0', port=5000)
from flask import Flask
from routes.route import getClientData_routes, getData_routes
import config

"""
La aplicacio segueix un model MVC (Model Vista Controlador):
Estructura de carpetes:
- Models: instancia db, elasticsearch en aquest cas
- Routes: endpoint d'acces a la app, en auqest cas la "/"
- Controllers: logica de la web, recopilar dades, enviarles a la db i redirigir al client
- Templates: plantilles de resposta que oferim als clients
- main.py i config.py, arxius d'execucio i configuracio de l'app
"""

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(getClientData_routes)
app.register_blueprint(getData_routes)

if __name__ == "__main__":
    app.run()
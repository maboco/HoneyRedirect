"""
Routes: punt d'entrada a la nostra app. Seria la nostra url
"""

from flask import Blueprint
from controllers.serverController import interceptUser, getData

getClientData_routes = Blueprint("getClientData", __name__)


@getClientData_routes.route("/", methods=["GET"])
def getClientData_route():
    return interceptUser()


getData_routes = Blueprint("getData", __name__)


@getData_routes.route("/getdata", methods=["POST"])
def getData_route():
    return getData()

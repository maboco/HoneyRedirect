"""
Controller: middle-man entre models i routes. Gestiona els inputs, dades, i les transmet al model.
"""
from flask import Blueprint, request, render_template
from datetime import datetime
from models.dbManage import PostgresSql

interceptuser = Blueprint("interceptUser", __name__)
def interceptUser():
    return render_template("index.html")

def getData():
    dataClient = request.get_json()
    resolution = dataClient["resolution"]
    ppi = dataClient["ppi"]

    remote_addr = request.headers.get("X-Forwarded-For")
    user_agent = request.user_agent
    accept_languages = request.accept_languages
    local_time = datetime.now()

    data = {
        "ip_address": str(remote_addr),
        "user_agent": str(user_agent),
        "accept_languages": str(accept_languages),
        "resolution": str(resolution),
        "ppi" : str(ppi),
        "local_time": str(local_time)
    }

    PostgresSql().create(data)

    return data

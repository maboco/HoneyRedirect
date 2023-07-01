"""
Controller: middle-man entre models i routes. Gestiona els inputs, dades, i les transmet al model.
"""
import random
from flask import Blueprint, request, render_template, make_response
from datetime import datetime
from models.dbManage import PostgresSql
from controllers.dataBuilder import DataBuilder

interceptuser = Blueprint("interceptUser", __name__)

def interceptUser():
    cookie = request.cookies.get("honeyredirect")
    response = make_response(render_template("index.html"))
    
    if not cookie: 
        response.set_cookie("honeyredirect", str(random.randint(0,10000)))
    
    return response

def getData():
    dataClient = request.get_json()
    remote_addr = request.headers.get("X-Forwarded-For")
    cookie = request.cookies.get("honeyredirect")
    server_time = datetime.now()
    
    data = DataBuilder()
    data.set_ip_address(remote_addr)
    data.set_user_agent(dataClient["userAgent"])
    data.set_accept_languages(dataClient["preferredLanguages"][0])
    data.set_resolution(str(dataClient["screenResolution"]["width"])+"x"+str(dataClient["screenResolution"]["height"]))
    data.set_ppi(dataClient["pixelDensity"])
    data.set_local_time(dataClient["localTime"])
    data.set_cookie(cookie)
    data.set_server_time(server_time)
    
    PostgresSql().create(data.build())

    return dataClient

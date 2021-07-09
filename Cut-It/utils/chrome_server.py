from flask import Flask, request, Response
from PyQt5.QtCore import QObject, pyqtSignal
import json

server = Flask(__name__)

@server.route('/', methods=["POST"])
def getData():
    data = request.form.to_dict()
    with open('userData/Cut-It_Chrome.json', 'w') as f:
        json.dump({"data": data}, f)
    return Response(status=200)
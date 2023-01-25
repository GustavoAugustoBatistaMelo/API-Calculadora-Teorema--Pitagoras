from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from services.pythagorean_theorem import PythagoreanTheorem
from helpers.checks import Checks

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app, support_credentials = True)

@app.get("/api/pythagorean-theorem")
@cross_origin(origin = '*')
def pythagorean_theorem():
    try: 
        response = {
            "statusCode": 200, 
            "message": "Operação realizada com sucesso!", 
            "payload": None
        }
        
        a = request.args.get(key='a', type=int),
        b = request.args.get(key='b', type=int),
        h = request.args.get(key='h', type=int),
        
        validateA = Checks.is_int(a[0])
        validateB = Checks.is_int(b[0])
        validateH = Checks.is_int(h[0])
        
        if validateA and validateB:
            response["payload"] = PythagoreanTheorem.calculate_hypotenuse(a[0], b[0])
        elif validateA and validateH:
            response["payload"] = PythagoreanTheorem.calculate_collared_peccary(a[0], h[0])
        elif validateB and validateH:
            response["payload"] = PythagoreanTheorem.calculate_collared_peccary(b[0], h[0])
        else:
            response["statusCode"] = 412
            response["message"] = "Parâmetros inválidos."

        return jsonify(response), response["statusCode"]
    except Exception as ex:
        response["statusCode"] = 500
        response["message"] = str(ex)

        return jsonify(response), 500
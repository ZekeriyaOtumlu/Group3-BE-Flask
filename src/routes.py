from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planets, Vehicles, Characters
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin


api = Blueprint('api', __name__)
CORS(api)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)



@api.route('/token', methods=['POST'])
def create_token():

    response_body = jsonify(message="Simple server is running")
    response_body.headers.add("Access-Control-Allow-Origin", "*")
    return response_body, 200
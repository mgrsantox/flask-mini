import datetime
import uuid

from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash

from .models import User
from src.databse import db
import jwt
from functools import wraps

from ..key import private_key, public_key

bp = Blueprint('users', __name__, url_prefix='/auth')


def token_required(f):
    from flask import current_app
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Bearer' in request.headers:
            token = request.headers['Bearer']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, public_key, algorithms=["RS256"])
            current_user = User.query.filter_by(id=data['id']).first()
        except Exception as e:
            print(e)
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@bp.route('/add', methods=['POST'])
def create_user():
    data = request.get_json()
    if "email" in data:
        user = User.query.filter_by(email=data["email"]).first()
        if not user:
            if "password" in data:
                if "name" in data:
                    if "location" in data:
                        hashed_password = generate_password_hash(data['password'], method='sha256')
                        new_user = User(id=str(uuid.uuid4()),email=data['email'], password=hashed_password,
                                        name=data["name"], location=data["location"])
                        db.session.add(new_user)
                        db.session.commit()
                        return jsonify({'message': 'New user created!'})
                    else:
                        return make_response({"location": "Location is required"}, 401)
                else:
                    return make_response({"name": "Name is required"}, 401)
            else:
                return make_response({"password": "Password is required"}, 401)
        else:
            return make_response({"email": "Use with this email already exist"}, 401)
    else:
        return make_response({"email": "Email is required"}, 401)


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if "email" in data:
        if "password" in data:
            user = User.query.filter_by(email=data["email"]).first()
            if user:
                from flask import current_app
                if check_password_hash(user.password, data["password"]):
                    token = jwt.encode({'id': user.id,
                                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
                                        private_key, algorithm="RS256")

                    return jsonify({'token': token})
            else:
                return make_response({"email": "User with this email doesn't exist"}, 401)
        else:
            return make_response({"password": "Password is required"}, 401)
    else:
        return make_response({"email": "Email is required"}, 401)


@bp.route("")
@token_required
def info(current_user):
    user_data = dict()
    user_data['id'] = current_user.id
    user_data['email'] = current_user.email
    user_data['name'] = current_user.name
    user_data['location'] = current_user.location
    return jsonify(user_data)

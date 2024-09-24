from flask import Blueprint, jsonify, request
from core import db
from core.models import Teacher, Assignment

bp = Blueprint('principal_teachers', __name__)

@bp.route('/principal/teachers', methods=['GET'])
def list_teachers():
    headers = request.headers.get('X-Principal')
    if not headers or not validate_principal(headers):
        return jsonify({"error": "Unauthorized"}), 401
    
    teachers = Teacher.query.all()
    return jsonify({"data": [teacher.to_dict() for teacher in teachers]})

def validate_principal(headers):
    # Implement validation logic for principal
    return True

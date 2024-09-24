from flask import Blueprint, jsonify, request
from core import db
from core.models import Assignment

bp = Blueprint('principal_assignments', __name__)

@bp.route('/principal/assignments', methods=['GET'])
def list_assignments():
    headers = request.headers.get('X-Principal')
    if not headers or not validate_principal(headers):
        return jsonify({"error": "Unauthorized"}), 401
    
    assignments = Assignment.query.filter(
        (Assignment.state == 'SUBMITTED') | (Assignment.state == 'GRADED')
    ).all()
    return jsonify({"data": [assignment.to_dict() for assignment in assignments]})

@bp.route('/principal/assignments/grade', methods=['POST'])
def grade_assignment():
    headers = request.headers.get('X-Principal')
    if not headers or not validate_principal(headers):
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    assignment = Assignment.query.get(data['id'])
    if not assignment:
        return jsonify({"error": "Assignment not found"}), 404
    
    assignment.grade = data['grade']
    assignment.state = 'GRADED'
    db.session.commit()
    
    return jsonify({"data": assignment.to_dict()})

def validate_principal(headers):
    # Implement validation logic for principal
    return True

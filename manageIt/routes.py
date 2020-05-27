from manageIt import app
from flask import request, Response, make_response, jsonify
from manageIt.user_service import createUser, getUser, deleteUser
from manageIt.kindergarten_service import createKindergarten, getKindergarten, deleteKindergarten
from manageIt.kid_service import createKid, getKid, deletesKid
from manageIt.reports_on_children_srevice import getReport, createReport, updateReport, deleteReport
from manageIt.kids_attendance_table import createRecord, updateRecord, deleteRecord


# Kindergarten
@app.route('/kindergarten', methods=['POST'])
def create_kindergarten():
    createKindergarten(request.json)
    return "created kindergarten"


@app.route('/kindergarten', methods=['GET'])
def get_kindergarten():
    kindergarten = getKindergarten(request.args)
    return jsonify(kindergarten)


@app.route('/kindergarten', methods=['DELETE'])
def delete_kindergarten():
    deleteKindergarten(request.args)
    return "Deleted kindergarten"


@app.route('/kindergarten', methods=['PUT'])
def update_kindergarten():
    return "Updated kindergarten"


# Kids endpoints
@app.route('/kids', methods=['POST'])
def create_kid():
    createKid(request.json)
    return "created kid object"


@app.route('/kids', methods=['GET'])
def get_kid():
    response = getKid(request.args)
    return jsonify(response)


@app.route('/kids', methods=['DELETE'])
def delete_kid():
    deletesKid(request.args)
    return "Deleted kid"


@app.route('/kids', methods=['PUT'])
def update_kid():
    return "Updated kid info"


# Employee endpoints
@app.route('/employee', methods=['POST'])
def create_employee():
    createUser(request.json)
    return "created employee"


@app.route('/employee', methods=['GET'])
def get_employee():
    response = getUser(request.args)
    return jsonify(response)


@app.route('/employee', methods=['DELETE'])
def delete_employee():
    deleteUser(request.args)
    return "Deleted employee"


@app.route('/employee', methods=['PUT'])
def update_employee():
    return "Updated employee"


@app.route('/allergy', methods=['POST'])
def add_allergy():
    return "added allergy"


@app.route('/allergy', methods=['PUT'])
def update_allergy():
    return "updated allergy"


@app.route('/allergy', methods=['DELETE'])
def delete_allergy():
    return "deleted allergy"


@app.route('/allergy', methods=['GET'])
def get_allergy():
    return "allergy"


@app.route('/reportsOnChildren', methods=['GET'])
def get_report():
    return getReport(request.args)


@app.route('/reportsOnChildren', methods=['POST'])
def create_report():
    createReport(request.json, isPutRequest=False)
    return "created"


@app.route('/reportsOnChildren', methods=['DELETE'])
def delete_report():
    deleteReport(request.args)
    return "deleted"


@app.route('/reportsOnChildren', methods=['PUT'])
def update_report():
    updateReport(request.json)
    return "updated"


@app.route('/kidAttendance', methods=['POST'])
def add_record():
    createRecord(request.json)
    return 'record added'


@app.route('/kidAttendance', methods=['PUT'])
def update_record():
    updateRecord(request.json)
    return 'added'


@app.route('/kidAttendance', methods=['DELETE'])
def delete_record():
    deleteRecord(request.args)
    return 'deleted'


if __name__ == '__main__':
    app.run()

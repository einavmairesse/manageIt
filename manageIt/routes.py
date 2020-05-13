from manageIt import app
from flask import request
from manageIt.user_service import createUser
from manageIt.kindergarten_service import createKindergarten
from manageIt.kid_service import createKid


# Kindergarten
@app.route('/kindergarten', methods=['POST'])
def create_kindergarten():
    createKindergarten(request.json)
    return "created kindergarten"


@app.route('/kindergarten', methods=['GET'])
def get_kindergarten():
    return "Get kindergarten"


@app.route('/kindergarten', methods=['DELETE'])
def delete_kindergarten():
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

    return "Get kid"


@app.route('/kids', methods=['DELETE'])
def delete_kid():
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
    return "Get employee"


@app.route('/employee', methods=['DELETE'])
def delete_employee():
    return "Deleted employee"


@app.route('/employee', methods=['PUT'])
def update_employee():
    return "Updated employee"


if __name__ == '__main__':
    app.run()

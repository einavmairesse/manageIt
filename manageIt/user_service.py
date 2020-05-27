from werkzeug.exceptions import abort

from manageIt.models import User, db
from manageIt.security import Security


def createUser(requestData):
    hashedPassword = Security.get_string_hash(requestData['password'])
    user = User(username=requestData['username'], email=requestData['email'], password=hashedPassword)
    db.session.add(user)
    db.session.commit()


def getUser(requestArguments):
    user_id = requestArguments['id']
    user_obj = User.query.filter_by(id=user_id).first()
    users_name = user_obj.username
    email = user_obj.email
    kindergarten = user_obj.kindergarten.name
    return {
        'name': users_name,
        'email': email,
        'kindergarten': kindergarten
    }


def deleteUser(requestArguments):
    user_id = requestArguments['id']
    user_to_delete = User.query.filter_by(id=user_id).first()

    if user_to_delete is None:
        abort(404)

    db.session.delete(user_to_delete)
    db.session.commit()


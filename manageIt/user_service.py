from manageIt.models import User, db
from manageIt.security import Security


def createUser(requestData):
    hashedPassword = Security.get_string_hash(requestData['password'])
    user = User(username=requestData['username'], email=requestData['email'], password=hashedPassword)
    db.session.add(user)
    db.session.commit()

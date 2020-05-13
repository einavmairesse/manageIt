from manageIt.models import User, Kindergarten, db


def createKindergarten(requestData):
    manager = User.query.filter_by(username=requestData['username']).first()
    kindergarten = Kindergarten(name=requestData['name'], manager=manager)
    db.session.add(kindergarten)
    db.session.commit()

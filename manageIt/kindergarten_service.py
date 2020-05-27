from manageIt.models import User, Kindergarten, db


def createKindergarten(requestData):
    manager = User.query.filter_by(username=requestData['username']).first()
    kindergarten = Kindergarten(name=requestData['name'], manager=manager)
    db.session.add(kindergarten)
    db.session.commit()


def getKindergarten(requestArguments):
    kindergartens_id = requestArguments['id']
    kindergarten_obj = Kindergarten.query.filter_by(id=kindergartens_id).first()
    kindergarten_name = kindergarten_obj.name
    kindergarten_manager = kindergarten_obj.manager.username
    return {
        'name': kindergarten_name,
        'manager': kindergarten_manager
    }


def deleteKindergarten(requestArguments):
    kindergartens_id = requestArguments['id']
    kindergarten_to_delete = Kindergarten.query.filter_by(id=kindergartens_id).first()
    db.session.delete(kindergarten_to_delete)
    db.session.commit()

from werkzeug.exceptions import abort
from manageIt.allergies_service import addAllergyToKid
from manageIt.models import Kid, Kindergarten, TypesOfAllergies, allergicKids, KidsAttendanceTable, ReportsOnTheChildren, db
from datetime import datetime


def createKid(requestData):
    birthday_as_date = strToDate(requestData['birthDate'])
    kindergarten = Kindergarten.query.filter_by(name=requestData['kindergarten']).first()
    kid = Kid(name=requestData['name'], birthDate=birthday_as_date, groupAge=requestData['groupAge'],
              kindergarten=kindergarten, kids_birth_id=requestData['ID'], gender=requestData['gender'], status=['status'])
    db.session.add(kid)
    db.session.commit()
    if 'allergies' in requestData:
        addAllergies(requestData['allergies'], kid)


def addAllergies(allergies, kid):
    if allergies is None:
        abort(404)
    for allergy in allergies:
        addAllergyToKid(kid, allergy)


def strToDate(date_text):
    try:
        date_obj = datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD/MM/YYYY")
    return date_obj


def getKid(requestArguments):
    kids_id = requestArguments['id']
    kid_obj = Kid.query.filter_by(id=kids_id).first()
    kids_name = kid_obj.name
    kids_birthdate = kid_obj.birthDate
    group_age = kid_obj.groupAge
    allergies = listOfAllergies(kids_id)
    kid_id = kid_obj.kids_birth_id
    kids_gender = kid_obj.gender
    kids_status = kid_obj.status
    return {
        'name': kids_name,
        'birthdate': kids_birthdate,
        'groupAge': group_age,
        'allergies': allergies,
        'ID': kid_id,
        'gender': kids_gender,
        'status': kids_status
    }


def listOfAllergies(kids_id):
    list_of_allergies = []
    for allergy in db.session.query(allergicKids).filter(allergicKids.c.kid_id == kids_id).all():
        allergy_name = TypesOfAllergies.query.filter_by(id=allergy.allergy_id).first().name
        list_of_allergies.append(allergy_name)
    return list_of_allergies


def isKidExistInTable(kid_id):
    kid = Kid.query.filter_by(id=kid_id).first()
    if kid is None:
        return False
    return True


def deletesKid(requestArguments):
    kid_id = requestArguments['id']
    kid = Kid.query.filter_by(id=kid_id).first()
    if kid_id is None or kid is None:
        abort(404)
    if 'deleteKidPermanently' in requestArguments:
        deleteKidPermanently(kid)
        return
#    if 'allergies' in requestArguments:
#        deleteAllergiesFromKidTable(kid, requestArguments['allergies'])


def deleteKidPermanently(kid):
    if kid is None:
        abort(404)
    deleteKidFromAllTables(kid)
    db.session.delete(kid)
    db.session.commit()


def deleteKidFromAllTables(kid):
    deleteKidFromAttendanceTable(kid)
    deleteKidFromKidsReportsTable(kid)
    deleteKidFromAllergicKidsTable(kid)


def deleteKidFromAttendanceTable(kid):
    # all_records = KidsAttendanceTable.query.filter_by(kid_id=kid.id).all()
    all_records = kid.attendance
    if len(all_records) != 0:
        for record in all_records:
            db.session.delete(record)

    db.session.commit()


def deleteKidFromKidsReportsTable(kid):
    #    all_reports = KidsAttendanceTable.query.filter_by(kid_id=kid.id).all()
    all_reports = kid.reports
    if len(all_reports) != 0:
        for record in all_reports:
            db.session.delete(record)

    db.session.commit()


def deleteKidFromAllergicKidsTable(kid):
    # all_kid_allergies = db.session.query(allergicKids).filter(allergicKids.c.kid_id == kid.id).all()
    all_kid_allergies = kid.allergies
    if all_kid_allergies is not None:
        for allergy in all_kid_allergies:
            db.session.delete(allergy)

    db.session.commit()


def updateKid(requestArguments):
    kid_id = requestArguments['id']
    kid = Kid.query.filter_by(id=kid_id).first()

    if kid_id is None or kid is None:
        abort(404)

    if 'name' in requestArguments:
        updateName(kid,requestArguments['name'])
    if 'birthdate' in requestArguments:
        updateBirthdate(kid, requestArguments['birthdate'])
    if 'groupAge' in requestArguments:
        updateGroupAge(kid, requestArguments['groupAge'])
    if 'allergies' in requestArguments:
        addAllergies(requestArguments['allergies'], kid)
    if 'ID' in requestArguments:
        updateID(kid, requestArguments['ID'])
    if 'gender' in requestArguments:
        updateGender(kid, requestArguments['gender'])
    if 'status' in requestArguments:
        updateStatus(kid, requestArguments['status'])


def updateName(kid, name):
    if name is None:
        abort(404)
    kid.name = name


def updateBirthdate(kid, birthdate):
    if birthdate is None:
        abort(404)
    kid.birthDate = birthdate


def updateGroupAge(kid, groupAge):
    if groupAge is None:
        abort(404)
    kid.groupAge= groupAge


def updateID(kid, ID):
    if ID is None:
        abort(404)
    kid.ID = ID


def updateGender(kid, gender):
    if gender is None:
        abort(404)
    kid.gender = gender


def updateStatus(kid,status):
    if status is None:
        abort(404)
    kid.status = status


#    kid_id = requestArguments['id']
#    kids_name = requestArguments['name']
#    birth_date = requestArguments['birthdate']
#    group_age = requestArguments['groupAge']
#    allergies = requestArguments['allergies']
#    kid_ID = requestArguments['ID']
#   gender = requestArguments['gender']
#    status = requestArguments['status']

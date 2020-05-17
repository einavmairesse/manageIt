from manageIt.models import Kid, Kindergarten, TypesOfAllergies, db
from datetime import datetime


def createKid(requestData):
    birthday_as_date = strToDate(requestData['birthDate'])
    kindergarten = Kindergarten.query.filter_by(name=requestData['kindergarten']).first()
    kid = Kid(name=requestData['name'], birthDate=birthday_as_date, groupAge=requestData['groupAge'],
              kindergarten=kindergarten)
    db.session.add(kid)
    db.session.commit()
    if 'allergies' in requestData:
        addAllergies(requestData['allergies'], kid)


def addAllergies(allergies, kid):
    for allergy in allergies:
        if isAllergyExist(allergy) is False:
            newAllergy = TypesOfAllergies(name=allergy)
            db.session.add(newAllergy)
            db.session.commit()
        current_allergy_obj = TypesOfAllergies.query.filter_by(name=allergy).first()
        kid.allergies.append(current_allergy_obj)
        db.session.commit()


def isAllergyExist(allergy):
    isAllergyExists = TypesOfAllergies.query.filter_by(name=allergy).first()
    if isAllergyExists is None:
        return False
    return True


def strToDate(date_text):
    try:
        date_obj = datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD/MM/YYYY")
    return date_obj

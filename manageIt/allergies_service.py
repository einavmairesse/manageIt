from werkzeug.exceptions import abort
from manageIt.kid_service import isKidExistInTable
from manageIt.models import TypesOfAllergies, db, Kid


# def createAllergy(requestData):
#    allergy_name = requestData['allergy']
#    kid_id = requestData['kid']
#    kid = Kid.query.filter_by(id=kid_id).first()
#    addAllergyToKid(kid, allergy_name)


def addAllergyToTypeOfAllergies(allergy):
    if allergy is None:
        abort(404)
    if isAllergyExist(allergy) is False:
        newAllergy = TypesOfAllergies(name=allergy)
        db.session.add(newAllergy)
        db.session.commit()


def addAllergyToKid(kid, allergy):
    if kid is None or allergy is None:
        abort(404)
    addAllergyToTypeOfAllergies(allergy)
    current_allergy_obj = TypesOfAllergies.query.filter_by(name=allergy).first()
    kid.allergies.append(current_allergy_obj)
    db.session.commit()


def isAllergyExist(allergy):
    isAllergyExists = TypesOfAllergies.query.filter_by(name=allergy).first()
    if isAllergyExists is None:
        return False
    return True


# def deleteAllergiesFromKidTable(kid, allergies):
#    if allergies is None:
#        abort(404)
#        for allergy in allergies:

from werkzeug.exceptions import abort
from manageIt.models import TypesOfAllergies, db, allergicKids



# def createAllergy(requestData):
#    allergy_name = requestData['allFergy']
#    kid_id = requestData['kid']
#    kid = Kid.query.filter_by(id=kid_id).first()
#    addAllergyToKid(kid, allergy_name)


def addAllergyToTypeOfAllergies(allergy):
    if allergy is None:
        abort(404)
    if isAllergyExistInTypesOfAllergies(allergy) is False:
        newAllergy = TypesOfAllergies(name=allergy)
        db.session.add(newAllergy)
        db.session.commit()


def addAllergyToKid(kid, allergy):
    if kid is None or allergy is None:
        abort(404)
    addAllergyToTypeOfAllergies(allergy)
    current_allergy_obj = TypesOfAllergies.query.filter_by(name=allergy).first()
    isKidAllergicToAllergy(kid, current_allergy_obj)
    kid.allergies.append(current_allergy_obj)
    db.session.commit()


def isKidAllergicToAllergy(kid, allergy):
    allKidAllergies = db.session.query(allergicKids).filter(allergicKids.c.kid_id == kid.id).all()
    if allergy in allKidAllergies:
        return True
    return False


def isAllergyExistInTypesOfAllergies(allergy):
    isAllergyExists = TypesOfAllergies.query.filter_by(name=allergy).first()
    if isAllergyExists is None:
        return False
    return True


def listOfAllergies(kids_id):
    list_of_allergies = []
    for allergy in db.session.query(allergicKids).filter(allergicKids.c.kid_id == kids_id).all():
        allergy_name = TypesOfAllergies.query.filter_by(id=allergy.allergy_id).first().name
        list_of_allergies.append(allergy_name)
    return list_of_allergies



# def deleteAllergiesFromKidTable(kid, allergies):
#    if allergies is None:
#        abort(404)
#        for allergy in allergies:

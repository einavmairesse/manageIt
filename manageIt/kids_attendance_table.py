from datetime import timedelta, date

from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import abort

from manageIt.kid_service import strToDate
from manageIt.models import KidsAttendanceTable, db, Kid


def createRecord(requestData):
    kid = Kid.query.filter_by(id=requestData['id']).first()
    if kid is None or isKidExistAllredy(kid):
        abort(404)
    if 'date' in requestData:
        date_to_add = strToDate(requestData['date'])
    else:
        date_to_add = date.today

    if isKidAbsenceYesterday(kid.id, date_to_add) > 0:
        amount_of_days = isKidAbsenceYesterday(kid.id, date_to_add) + 1
    else:
        amount_of_days = 1

    new_record = KidsAttendanceTable(kid=kid, date_of_absence=date_to_add, days_of_absence=amount_of_days)
    if 'reasonOfAbsence' in requestData:
        new_record.reason_of_absence = requestData['reasonOfAbsence']

    db.session.add(new_record)
    commitData()


def isKidAbsenceYesterday(kid_id, day):
    yesterday = day - timedelta(days=1)

    kid_attendance = KidsAttendanceTable.query.filter_by(id=kid_id)
    if kid_attendance.count() == 0:
        return 0

    for record in kid_attendance.all():
        if record.date_of_absence == yesterday:
            return record.days_of_absence
    return 0


def deleteRecord(requestArguments):
    record_id = requestArguments['id']
    record_to_delete = KidsAttendanceTable.query.filter_by(id=record_id).first()

    if record_to_delete is None:
        abort(404)
    db.session.delete(record_to_delete)
    commitData()


def commitData():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()


def addReasonOfAbsence(requestData):
    reason = requestData['reasonOfAbsence']
    record = KidsAttendanceTable.query.filter_by(id=requestData['id']).first()
    record.reason_of_absence = reason
    
    commitData()


def increaseAmountOfDaysByOne(requestArguments):
    record = KidsAttendanceTable.quert.filter_by(id=requestArguments['id'])
    record.days_of_absence = record.days_of_absence + 1


def addAmountOfDays(requestData):
    amountOfDays = requestData['days']
    record = requestData['id']
    record.days_of_absence = amountOfDays


def isKidExistAllredy(kid):
    status = KidsAttendanceTable.query.filter_by(kid_id=kid.id).first()
    if status is None:
        return False
    return True


def updateRecord(requestData):
    if 'addDay' in requestData:
        increaseAmountOfDaysByOne(requestData)
    if 'reasonOfAbsence' in requestData:
        addReasonOfAbsence(requestData)

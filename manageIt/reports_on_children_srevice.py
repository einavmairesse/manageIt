from werkzeug.exceptions import abort
from datetime import date

from manageIt.kid_service import strToDate
from manageIt.models import ReportsOnTheChildren, db, Kid


def createReport(requestData, isPutRequest):
    if 'date' in requestData:
        date_to_add = strToDate(requestData['date'])
    else:
        date_to_add = date.today
    kid = Kid.query.filter_by(name=requestData['name']).first()
    if kid is None:
        abort(404)
    if isPutRequest:
        report = ReportsOnTheChildren(id=requestData['id'], report=requestData['report'], kid=kid, date=date_to_add)
    else:
        report = ReportsOnTheChildren(report=requestData['report'], kid=kid, date=date_to_add)
    db.session.add(report)
    db.session.commit()


def getReport(requestArguments):
    report_id = requestArguments['id']
    report = ReportsOnTheChildren.query.filter_by(id=report_id).first()
    if report is None:
        abort(404)
    return report.report


def updateReport(requestData):
    report_id = requestData['id']
    report = ReportsOnTheChildren.query.filter_by(id=report_id).first()
    if report is None:
        createReport(requestData, isPutRequest=True)
    else:
        report.report = requestData['report']
    db.session.commit()


def deleteReport(requestArguments):
    report_id = requestArguments['id']
    report_to_delete = ReportsOnTheChildren.query.filter_by(id=report_id).first()
    if report_to_delete is None:
        abort(404)

    db.session.delete(report_to_delete)
    db.session.commit()

import cherrypy
import re, json

class UsersControllerI:
    def __init__(self, mdb=None):
        self.mdb = mdb

    def GET(self, uid):
        output = {'result':'success'}
        uid = int(uid)
        try:
            l = self.mdb.users[uid]
            output['gender'] = l[0]
            output['age'] = l[1]
            output['zipcode'] = l[3]
            output['id'] = uid
            output['occupation'] = l[2]
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to get'
        return json.dumps(output)

    def DELETE(self, uid):
        output = {'result':'success'}
        uid = int(uid)
        try:
            self.mdb.users.pop(uid)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to delete'
        return json.dumps(output)

    def PUT(self, uid):
        output = {'result':'success'}
        thebody = cherrypy.request.body.read().decode()
        l = []
        uid = int(uid)
        try:
            thebody = json.loads(thebody)
            zipcode = thebody['zipcode']
            age = thebody['age']
            gender = thebody['gender']
            occupation = thebody['occupation']
            l.append(gender)
            l.append(age)
            l.append(occupation)
            l.append(zipcode)
            self.mdb.users[uid] = l
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to put'
        return json.dumps(output)


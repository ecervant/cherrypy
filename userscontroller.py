import cherrypy
import re, json

class UsersController:
    def __init__(self, mdb=None):
        self.mdb = mdb

    def GET(self):
        output = {'result':'success'}
        l = self.mdb.get_all_users()
        output['users'] = l
        return json.dumps(output)
    
    def POST(self):
        output = {'result':'success'}
        thebody = cherrypy.request.body.read().decode()
        l = []
        try:
            thebody = json.loads(thebody)
            zipcode = thebody['zipcode']
            age = thebody['age']
            gender = thebody['gender']
            occupation = thebody['occupation']
            uid = len(self.mdb.users)+1
            l.append(gender)
            l.append(age)
            l.append(occupation)
            l.append(zipcode)
            self.mdb.users[uid] = l
            output['id'] = uid
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to post'
        return json.dumps(output)

    def DELETE(self):
        output = {'result':'success'}
        self.mdb.users.clear()
        return json.dumps(output)


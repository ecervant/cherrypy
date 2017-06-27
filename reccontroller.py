import cherrypy
import re, json

class RecController:
    def __init__(self, mdb=None):
        self.mdb = mdb

    def GET(self, uid):
        output = {'result':'success'}
        uid = int(uid)
        try:
            mid = self.mdb.get_highest_rated_unvoted_movie(uid)
            output['movie_id'] = mid
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to get'
        return json.dumps(output)

    def PUT(self, uid):
        output = {'result':'success'}
        uid = int(uid)
        thebody = cherrypy.request.body.read().decode()
        try:
            thebody = json.loads(thebody)
            mid = thebody['movie_id']
            rating = thebody['rating']
            self.mdb.set_user_movie_rating(uid, mid, rating)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to put'
        return json.dumps(output)

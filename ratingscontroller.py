import cherrypy
import re, json

class RatingsController:
    def __init__(self, mdb=None):
        self.mdb = mdb
    
    def GET(self, mid):
        output = {'result':'success'}
        mid = int(mid)
        try:
            output['rating'] = self.mdb.get_rating(mid)
            output['movie_id'] = mid
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to get'
        return json.dumps(output)

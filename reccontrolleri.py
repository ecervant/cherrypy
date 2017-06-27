import cherrypy
import re, json

class RecControllerI:
    def __init__(self, mdb=None):
        self.mdb = mdb

    def DELETE(self):
        output = {'result':'success'}
        self.mdb.ratings.clear()
        return json.dumps(output)


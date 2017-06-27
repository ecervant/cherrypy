import cherrypy
import re, json

class MoviesControllerI:
    def __init__(self, mdb=None):
        self.mdb = mdb

    def GET(self, mid):
        output = {'result': 'success'}      
        mid = int(mid)
        try:
            name = self.mdb.movie_names[mid]
            genre = self.mdb.movie_genres[mid]
            output['genres'] = genre
            output['title'] = name
            output['id'] = mid
            output['img'] = self.mdb.imgs[mid]
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'mid not found'
        return json.dumps(output)

    def DELETE(self, mid):
        output = {'result' : 'success'}
        mid = int(mid)
        try:
            self.mdb.movie_names.pop(mid)
            self.mdb.movie_genres.pop(mid)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to delete'
        return json.dumps(output)

    def PUT(self, mid):
        output = {'result':'success'}
        thebody = cherrypy.request.body.read().decode()
        mid = int(mid)
        try:
            thebody = json.loads(thebody)
            genre = thebody['genres']
            title = thebody['title']
            self.mdb.movie_names[mid] = title
            self.mdb.movie_genres[mid] = genre
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'unable to put'
        return json.dumps(output)

import cherrypy
import re, json

class MoviesController:
        def __init__(self, mdb=None):
            self.mdb = mdb

        def GET(self):
            output = {'result': 'success'}      
            l = self.mdb.get_all_movies()
            output['movies'] = l
            return json.dumps(output)

        def POST(self):
            output = {'result' : 'success'}
            thebody = cherrypy.request.body.read().decode()
            try:
                thebody = json.loads(thebody)
                genre = thebody['genres']
                title = thebody['title']
                mid = max(self.mdb.movie_names.keys()) + 1
                self.mdb.movie_names[mid] = title
                self.mdb.movie_genres[mid] = genre
                output['id'] = mid
            except Exception as ex:
                output['result'] = 'error'
                output['message'] = 'unable to post'
            return json.dumps(output)

        def DELETE(self, mid=None):
            output = {'result' : 'success'}
            self.mdb.movie_names.clear()
            self.mdb.movie_genres.clear()
            return json.dumps(output)


import cherrypy
import re, json
class ResetController:
    def __init__(self, mdb=None):
            self.mdb = mdb
    def PUT(self, mid=None):
        output = {'result' : 'success'}
        if mid is None:
            self.mdb.load_movies('ml-1m/movies.dat')
            self.mdb.load_users('ml-1m/users.dat')
            self.mdb.load_ratings('ml-1m/ratings.dat')
            self.mdb.load_images('ml-1m/images.dat')
        else:
            self.mdb.load_movie('ml-1m/movies.dat', mid) 
            self.mdb.load_rating_mid('ml-1m/ratings.dat', mid)
        return json.dumps(output)
            

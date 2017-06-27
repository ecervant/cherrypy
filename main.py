#Esmeralda Cervantes
import cherrypy
import re, json
from _movie_database import _movie_database
from resetcontroller import ResetController
from moviescontroller import MoviesController
from userscontroller import UsersController
from ratingscontroller import RatingsController
from reccontroller import RecController
from moviescontrolleri import MoviesControllerI
from userscontrolleri import UsersControllerI
from reccontrolleri import RecControllerI

def start_service():
    mdb = _movie_database()
    mdb.load_movies('ml-1m/movies.dat')
    mdb.load_users('ml-1m/users.dat')
    mdb.load_ratings('ml-1m/ratings.dat')
    mdb.load_images('ml-1m/images.dat')

    # reset
    resetController = ResetController(mdb)
    # movies
    moviesController = MoviesController(mdb)
    moviesControllerI= MoviesControllerI(mdb) 
    # users
    usersController = UsersController(mdb)
    usersControllerI= UsersControllerI(mdb)
    # ratings
    ratingsController = RatingsController(mdb)
    # recommendations
    recController = RecController(mdb)
    recControllerI = RecControllerI(mdb)

    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    # reset connect
    dispatcher.connect('reset_movie', '/reset/', 
            controller=resetController,
            action = 'PUT', conditions=dict(method=['PUT']))

    dispatcher.connect('reset_movie_mid', '/reset/:mid',
            controller=resetController,
            action = 'PUT', conditions=dict(method=['PUT']))
    
    # movies connect
    dispatcher.connect('movies_get', '/movies/',
            controller=moviesController,
            action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('movies_post', '/movies/',
            controller=moviesController,
            action = 'POST', conditions=dict(method=['POST']))
    dispatcher.connect('movies_delete', '/movies/',
            controller=moviesController,
            action = 'DELETE', conditions=dict(method=['DELETE']))
    dispatcher.connect('movies_get_mid', '/movies/:mid',
            controller=moviesControllerI,
            action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('movies_delete_mid', '/movies/:mid',
            controller=moviesControllerI,
            action = 'DELETE', conditions=dict(method=['DELETE']))
    dispatcher.connect('movies_put_mid', '/movies/:mid',
            controller=moviesControllerI,
            action = 'PUT', conditions=dict(method=['PUT']))
    # users connect
    dispatcher.connect('users_get', '/users/',
            controller=usersController,
            action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('users_get_uid', '/users/:uid',
            controller=usersControllerI,
            action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('users_post', '/users/',
            controller=usersController,
            action = 'POST', conditions=dict(method=['POST']))
    dispatcher.connect('users_delete', '/users/',
            controller=usersController,
            action = 'DELETE', conditions=dict(method=['DELETE']))
    dispatcher.connect('users_put_uid', '/users/:uid',
            controller=usersControllerI,
            action = 'PUT', conditions=dict(method=['PUT']))
    dispatcher.connect('users_delete_uid', '/users/:uid',
            controller=usersControllerI,
            action = 'DELETE', conditions=dict(method=['DELETE']))
    # rating
    dispatcher.connect('ratings_get', '/ratings/:mid',
            controller=ratingsController,
            action = 'GET', conditions=dict(method=['GET']))
    # recommendations
    dispatcher.connect('rec_delete', '/recommendations/',
            controller=recControllerI,
            action = 'DELETE', conditions=dict(method=['DELETE']))
    dispatcher.connect('rec_get_uid', '/recommendations/:uid',
            controller=recController,
            action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('rec_put_uid', '/recommendations/:uid',
            controller=recController,
            action = 'PUT', conditions=dict(method=['PUT']))
 


    conf = { 'global'   : {'server.socket_host': 'ash.campus.nd.edu',
                            'server.socket_port': 40127,
                            },
            '/'         : {'request.dispatch': dispatcher}
            }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)




if __name__=='__main__':
    start_service()

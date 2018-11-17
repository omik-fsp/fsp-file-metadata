import os

DBURI = 'sqlite:///' + os.path.abspath('./database.db')


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'BruceWayneIsBatman'
    JSON_SORT_KEYS = False
    '''
    By default Flask will serialize JSON objects in a way that the keys are ordered. 
    This is done in order to ensure that independent of the hash seed of the dictionary 
    the return value will be consistent to not trash external HTTP caches. You can 
    override the default behavior by changing this variable. This is not recommended 
    but might give you a performance improvement on the cost of cacheability.
    '''


class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DBURI
    #SECRET_KEY = os.environ['SECRET_KEY']


class Development(Config):
    DEBUG = True

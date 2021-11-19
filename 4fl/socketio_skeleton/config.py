import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'secret!' #os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    def __repr__(self):
    	return '<Post {}>'.format(self.SQLALCHEMY_DATABASE_URI)
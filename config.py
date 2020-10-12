import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'con.env'))

class Config:
    UPLOAD_PATH = os.path.join(basedir, 'app/static/uploads/')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fsdsf2few-23f'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    #REDIS
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

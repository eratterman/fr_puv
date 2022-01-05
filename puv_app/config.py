import os
import secrets


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_urlsafe(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL'
    ) or 'sqlite:///' + os.path.join(
        BASE_DIR,
        'app.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# config.py
class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://idea_user:your_password@localhost/idea_incubator'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

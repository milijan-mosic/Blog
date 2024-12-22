import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///blog.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER', 'your-email@gmail.com')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS', 'your-email-password')

    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')

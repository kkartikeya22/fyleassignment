import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///your_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # Set to True if you want to see SQL queries in the console

    # Optional: Other configurations
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # For session management or other purposes
    DEBUG = os.getenv('DEBUG', 'False') == 'True'  # Set debug mode from environment variable
    TESTING = os.getenv('TESTING', 'False') == 'True'  # Set testing mode from environment variable

    # Flask-Mail configuration (if using Flask-Mail)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', None)
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', None)
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')

    # Other optional configurations
    # LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    # STATIC_FOLDER = 'static'
    # TEMPLATES_FOLDER = 'templates'

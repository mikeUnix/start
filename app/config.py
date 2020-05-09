class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1@localhost/test1' #Access denied for user 'root'@'localhost'
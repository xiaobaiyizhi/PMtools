#!flask/bin/python
import sys
sys.path.append('..')
from migrate.versioning import api
from config.default import SQLALCHEMY_DATABASE_URI
from config.default import SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version:' + str(v))

#!flask/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from migrate.versioning import api
from config.default import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from PMtools import db


import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(
        SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_MIGRATE_REPO,
        api.version(SQLALCHEMY_MIGRATE_REPO))

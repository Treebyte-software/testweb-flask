# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from os import environ
import json
import os

class Config(object):
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None

class ConfigFromJson(object):
    def __init__(self):
        self.app_path = os.getcwd()

        with open(os.path.join(self.app_path, "config.json")) as json_config_file:
            data = json.load(json_config_file)

        # layouts path: directory that contains the XSL layouts files, without start or ending delimiter
        self.layouts_path = data["layouts_path"]

        # reports path: directory that contains the temporary report files, without start or ending delimiter
        self.reports_path = data["reports_path"]

        # iaengine: directory and filename of IAEngine.dll
        self.iaengine = data["iaengine"]

        # connection type: idenfity the database + dialect or driver according with SQLAlchemy format
        # connection string: username, password and link to db
        # database connection: the result of the two informations above.
        # the separator "://" is standard of SQLAlchemy AND MUST NOT BE OMITTED.
        self.connection_type = data["connection_type"]
        self.connection_string = data["connection_string"]
        self.database_connection = self.connection_type + "://" + self.connection_string

        # record_page_size: number of records fetched at every get.
        self.record_page_size = int(data["record_page_size"])

        # pool_size: size of database connection pool
        self.pool_size = int(data["pool_size"])

        # host: address listened by the service
        self.host = data["host"]

        # port: port listened by the service
        self.port = int(data["port"])

        # log_file_name: path and name of the service log.
        self.log_file_name = data["log_file_name"]

        # application name for authentication key
        self.app_name = data["app_name"]


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('APPSEED_DATABASE_USER', 'appseed'),
        environ.get('APPSEED_DATABASE_PASSWORD', 'appseed'),
        environ.get('APPSEED_DATABASE_HOST', 'db'),
        environ.get('APPSEED_DATABASE_PORT', 5432),
        environ.get('APPSEED_DATABASE_NAME', 'appseed')
    )


# class DebugConfig(Config):
#    DEBUG = True

class DebugConfig(ConfigFromJson):
    DEBUG = True

config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}

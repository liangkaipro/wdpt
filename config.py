# encoding: utf-8
import os


Debug = True

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/testing"
SQLALCHEMY_TRACK_MODIFICATIONS = False



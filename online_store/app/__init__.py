#!/usr/bin/env python3
# -*- coding: utf8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import flask_SQLalchemy

app = Flask(__name__)
Bootstrap(app)
from app import routes

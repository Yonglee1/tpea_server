# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
import pymysql
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:sysucc20@47.88.101.236:3306/tpga'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "xxx"

db = SQLAlchemy(app)


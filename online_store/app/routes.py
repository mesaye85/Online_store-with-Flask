#!/usr/bin/env python3
# -*- coding: utf8 -*-


from flask import g, request
from app import app
import sqlite3

DATABASE = "online_store"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_all_users():
    cursor = get_db().execute("selec * from user", ())
    results = cursor.fetchall()
    cursor.close()
    return results     


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)  
    if db is not None:
        db.close()

@app.route('/')
@app.route('/mesaye')
def index():
    return "hello,World"


@app.route('/users' , methods=["GET", "POST"])
def get_users():
    #creating an output dictinory
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        #get_all_users() returns all ecords from the user table
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict)
        out["body"] = body_list  
        return out  
    if "POST" in request.methods:
    # create a new user
        pass               



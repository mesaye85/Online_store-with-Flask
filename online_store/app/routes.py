#!/usr/bin/env python3
# -*- coding: utf8 -*-


from flask import g, request
from app import app
import sqlite3
from flask import render_template

DATABASE = "online_store"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def get_all_users():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return results


def update_user():
    cursor = get_db().execute("UPDATE user", ())
    results = cursor
    cursor.close()
    return results

def delete_user():
    cursor = get_db().execute("DELETE FROM user", ())
    results = cursor
    cursor.close()
    return results

def create_user():
    cursor = get_db().execute("INSERT into user values", ())
    results = cursor
    cursor.close()
    return results



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return "Hello,World"

@app.route('/about')
def about():
    return {
        "first_name": "Mesaye",
        "last_name": "Addisu",
        "hobby": "Gym"
    }


@app.route('/users', methods=["GET", "POST", "PUT","DELETE"])
def get_users():
    # creating an output dictinory
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        # get_all_users() returns all records from the user table
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

        return render_template(
        "base.html", first_name=out["body"] [0].get("first_name"),
                     last_name=out ["body"] [0].get("first_name"),
                     hobbies=out ["body"] [0].get("first_name")
                                        )
        

    if "POST" in request.methods:
       
        # create a new user
        pass
    

@app.route('/countdown/<int:number>')
def countdown(number):
    return"</br>".join([str(i) for i in range(number, 0, -1) ])


@app.route('/agent')
def agent():
    user_agent = request.headers.get("User_Agent")
    return "<p>Your user agent is %s</p>" % user_agent    



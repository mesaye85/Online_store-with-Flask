#!/usr/bin/env python3
# -*- coding: utf8 -*-


from flask import g, request
from app import app
import sqlite3
from flask import render_template
from getpass import getpass
import sys

from flask import current_app
from bull import app, bcrypt
from bull.models import User, db


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


def get_all_catalog():
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()
    cursor.close()
    return results


def update_catalog():
    cursor = get_db().execute("UPDATE product", ())
    results = cursor
    cursor.close()
    return results


def delete_catalog():
    cursor = get_db().execute("DELETE FROM product", ())
    results = cursor
    cursor.close()
    return results


def create_products():
    cursor = get_db().execute("INSERT into product values", ())
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


@app.route('/catalog')
def catalog():
    return {
        "Item": "Phone",
        "Quantity": "",
        "Price": "$20"
    }


@app.route('/users', methods=["GET", "POST", "PUT", "DELETE"])
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


return render_template(
            "about_me.html", first_name=out["body"][0].get("first_name"),
            last_name=out["body"][0].get("last_name"),
            hobbies=out["body"][0].get("hobbies")
)


@app.route('/products', methods=["GET", "POST"])
def get_catalog():
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "Item": item[0],
                "Price": item[1],
                "IMG": item[2]
            }
            body_list.append(temp_dict)
        body_list.append(temp_dict)


return render_template["Catalog.html", products= body_list]

        if 'post' in request.method:
            form = newProductForm()
            if form.validate_on sumbit():
                create_products(form.item, form.price, form.img)
            return render_template('Catalog.html')



    if "POST" in request.methods:
        # create a new user
        create_user()
        pass
    if "PUT" in request.method:
        # update code goes here
        update_user()
        pass






@app.route('/countdown/<int:number>')
def countdown(number):
    return"</br>".join([str(i) for i in range(number, 0, -1)])


@app.route('/agent')
def agent():
    user_agent = request.headers.get("User_Agent")
    return "<p>Your user agent is %s</p>" % user_agent


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/admin')
def main():
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print 'user already exists! Create another? (y/n):',
            create = raw_input()
            if create == 'n':
                return

        print 'Enter email address: ',
        email = raw_input()
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(
            email=email, 
            password=bcrypt.generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print 'User added.'
return render_template('admin.html')

if __name__ == '__main__':
    sys.exit(main())

import os.path
from sqlite3 import OperationalError, IntegrityError
import sqlite3
from App.Config import ROOT_DIR
from App.model.User import User
from App.model.Team import Team


def create_database():
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    with open(os.path.join(ROOT_DIR, "Database/schema.sql")) as script:
        content = script.read()
        script.close()
        try:
            cursor.executescript(content)
        except OperationalError as e:
            print(e)
            print("Could not create database")
    con.commit()
    con.close()


def insert_user(user_obj):
    query = f"INSERT INTO user (name, pass_hash, salt, last_login) VALUES ('{user_obj.get_name()}', '{user_obj.get_pass_hash()}'," \
            f" '{user_obj.get_salt()}', '{user_obj.get_last_login()}')"
    print(query)
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    try:
        cursor.execute(query)
    except IntegrityError:
        pass
    con.commit()
    con.close()


def reauth_user(user_obj: User):
    query = f"UPDATE user SET last_login = '{user_obj.get_last_login()}' WHERE id = '{user_obj.get_id()}'"
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    con.close()


def delete_user(user_id):
    user = read_user(user_id)
    query = f"DELETE FROM user WHERE id == {user_id}"
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    try:
        cursor.execute(query)
        con.commit()
        con.close()
        return user.__dict__()
    except OperationalError:
        print("Could not delete user!")
    return {}


def read_all_users():
    query = "SELECT * FROM user;"
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    result = cursor.execute(query).fetchall()
    # con.close()
    return [User(id=row[0], name=row[1], pass_hash=row[2], salt=row[3]).__dict__() for row in result]


def read_user(user_id):
    query = f"SELECT * FROM user WHERE id == {user_id}"
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    result = cursor.execute(query).fetchone()
    con.close()
    if result is not None:
        return User(id=result[0], name=result[1], pass_hash=result[2], salt=result[3])
    else:
        return None


def read_user_by_name(user_name):
    query = f"SELECT * FROM user WHERE name == '{user_name}'"
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    result = cursor.execute(query).fetchone()
    con.close()
    if result is not None:
        return User(id=result[0], name=result[1], pass_hash=result[2], salt=result[3])
    else:
        return None


def read_teams():
    query = "SELECT * FROM team"
    con = sqlite3.connect(os.path.join(ROOT_DIR, "local.db"))
    cursor = con.cursor()
    result = cursor.execute(query).fetchall()
    con.close()
    if result is not None:
        return [Team(id=row[0], name=row[1]) for row in result]

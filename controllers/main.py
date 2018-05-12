from flask import *
import hashlib
from extensions import db

main = Blueprint('main', __name__)\

@main.route("/")
def hello():
    return "Helloooooo!"

@main.route("/addcontact/<firstname>-<lastname>")
def addcontact(firstname, lastname):
    cur = db.cursor()
    m = hashlib.new('sha1')
    m.update((firstname.lower()+lastname.lower()).encode('utf-8'))
    name_hash = m.hexdigest()
    print("LENGTH: ", len(name_hash))

    query = "SELECT * FROM Contacts WHERE userid='"+name_hash+"';"
    cur.execute(query)

    if cur.rowcount != 0:
        return "ERROR: user already exists, "+query

    query = "INSERT INTO Contacts SET userid='"+name_hash+"', firstname='"+firstname+"', lastname='"+lastname+"';"
    cur.execute(query)

    return "Hello there, "+str(firstname).capitalize()+" "+str(lastname).capitalize()

@main.route("/removecontact/<firstname>-<lastname>")
def removecontact(firstname, lastname):
    cur = db.cursor()
    m = hashlib.new('sha1')
    m.update((firstname.lower()+lastname.lower()).encode('utf-8'))
    name_hash = m.hexdigest()

    query = "DELETE FROM Contacts WHERE userid='"+name_hash+"';"
    cur.execute(query)

    return str(firstname).capitalize()+" "+str(lastname).capitalize()+" deleted successfully"

@main.route("/displaycontact/<firstname>-<lastname>")
def displaycontact(firstname, lastname):
    cur = db.cursor()

    m = hashlib.new('sha1')
    m.update((firstname.lower()+lastname.lower()).encode('utf-8'))
    name_hash = m.hexdigest()

    query = "SELECT * FROM Contacts WHERE userid='"+name_hash+"';"
    cur.execute(query)

    if cur.rowcount == 0:
        return "ERROR: user not found, "+query

    users=list(cur.fetchall())
    return str(users[0])


import sqlite3
from os.path import exists

import click
from flask import g
from werkzeug.security import generate_password_hash

from config import users_db, gs_admin_password

# https://flask.palletsprojects.com/en/2.3.x/tutorial/database/

def init_db():
    # create database if it does not exist and create admin user
    if not exists(users_db):
        db = sqlite3.connect(users_db)
        db.execute("""CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            token TEXT UNIQUE,
            token_expiration INTEGER
        )""")
        db.execute('INSERT INTO user (username, password_hash) VALUES (?, ?)',
                         ('admin', generate_password_hash(gs_admin_password)))
        db.commit()
        print('Users Database Created')


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def get_db() -> sqlite3.Connection:
    if 'db' not in g:
        g.db = sqlite3.connect(users_db) #sqlite3.connect() method. This method establishes a connection to the specified database file. If the file does not exist, SQLite will automatically create it. 
    return g.db

# Use "flask init-db" in the terminal to create the db manually

@click.command('init-db') #define command line wrapper
def init_db_command():
    init_db()
    click.echo('Initialized the database ;D')

def init_app(app): 
    init_db()
    app.cli.add_command(init_db_command) #Clean integration with Flask’s app.cli
    app.teardown_appcontext(close_db)


from flask import (Blueprint, render_template)
# The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
import os
import sqlite3
from datetime import datetime

# CREATE TABLE
    # CREATE TABLE appointments(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name VARCHAR(200) NOT NULL,
    # start_datetime TIMESTAMP NOT NULL,
    # end_datetime TIMESTAMP NOT NULL,
    # description TEXT NOT NULL,
    # private BOOLEAN NOT NULL
    # );

#  Insert table data
    # INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
    # VALUES
    # ('My appointment', '2022-11-01 14:00:00', '22022-11-01 15:00:00',
    #  'An appointment for me', false);


bp = Blueprint('main', __name__, url_prefix='/')

DB_FILE = os.environ.get("DB_FILE")


@bp.route("/")
def main():
    # Create a SQLite3 connection with the connection parameters
    with sqlite3.connect(DB_FILE) as conn:
        # Create a cursor from the connection
        curs = conn.cursor()
        # Execute "SELECT id, name, start_datetime, end_datetime
        #          FROM appointments
        #          ORDER BY start_datetime;"
        curs.execute("""
            SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime
        """)
        # Fetch all of the records
        rows = curs.fetchall()
        # convert each time string to object here (extra)
        # print(rows)
        return render_template("main.html", rows=rows)
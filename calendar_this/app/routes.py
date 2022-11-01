from flask import (Blueprint, render_template, redirect)
# The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
import os
import sqlite3
from datetime import datetime
from .forms import AppointmentForm

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


@bp.route("/", methods=["GET", "POST"])
def main():
    form = AppointmentForm()

    # form validations
    if form.validate_on_submit():
     params = {
        'name': form.name.data,
        'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
        'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
        'description': form.description.data,
        'private': form.private.data
    }
        with sqlite3.connect(DB_FILE) as conn:
            curs = conn.cursor()
            curs.execute("""
                INSERT INTO appointments(name, start_datetime, end_datetime, description, private)
                VALUES (:name, :start_datetime, :end_datetime, :description, :private)
            """,
            {
                    "name": name,
                    "start_datetime": start_datetime,
                    "end_datetime": end_datetime,
                    "description": description,
                    "private": private

            }
            )
            redirect('/')


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
        return render_template("main.html", rows=rows, form=form)
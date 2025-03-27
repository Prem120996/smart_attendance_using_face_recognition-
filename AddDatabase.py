Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
AddDatatoDatabase.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
... })
... 
... ref = db.reference('Students')
... 
... data = {
...     "321654":
...         {
...             "name": "Elon musk",
...             "major": "Robotics",
...             "starting_year": 2017,
...             "total_attendance": 7,
...             "standing": "G",
...             "year": 4,
...             "last_attendance_time": "2024-12-11 00:54:34"
...         },
...     "852741":
...         {
...             "name": "Mark Zuckerberg",
...             "major": "Economics",
...             "starting_year": 2021,
...             "total_attendance": 12,
...             "standing": "B",
...             "year": 1,
...             "last_attendance_time": "2024-12-11 00:54:34"
...         },
...     "963852":
...         {
...             "name": "Virat Kohli",
...             "major": "Physics",
...             "starting_year": 2020,
...             "total_attendance": 7,
...             "standing": "G",
...             "year": 2,
...             "last_attendance_time": "2024-12-11 00:54:34"
...         }
... }
... 
... for key, value in data.items():
...     ref.child(key).set(value)

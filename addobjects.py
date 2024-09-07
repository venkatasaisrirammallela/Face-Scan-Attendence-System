import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(r"C:\Users\venka\Downloads\firebasepath.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancesystem-38a01-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "22071A7203":
    {
        "name" : "A.Abhishek" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7204":
    {
        "name" :  "Abhigna" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7205":
    {
        "name" : "Durga" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7207":
    {
        "name" : "Teja" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7211":
    {
        "name" : "Bhanu" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7215":
    {
        "name" : "Rohith" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7220":
    {
        "name" : "Harsh" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7223":
    {
        "name" : "Rthiesh" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7225":
    {
        "name" : "Nipun" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7227":
    {
        "name" : "Vicky" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7230":
    {
        "name" : "Siddhu" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7234":
    {
        "name" : "M.Bhanu" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    },
    "22071A7241":
    {
        "name" : "Varun" ,
        "branch" : "AI&DS" ,
        "starting_year" : 2024 ,
        "total_attendance" : 0 ,
        "standing" : "O" ,
        "year" : 2 ,
        "last_attendance_time" : "2024-12-11 00:54:34"
    }
}
try:
    ref.set(data)
    print("Student data has been successfully updated.")
except Exception as e:
    print(f"Error updating student data: {e}")
import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="smj_airline_reservation"
)
cursor = conn.cursor()

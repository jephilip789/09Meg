import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sunshine",
    database="smj_airline_reservation"
)
cursor = conn.cursor()
# Function to create a new reservation
def create_reservation():
    trip_type = trip_var.get()
    departure_date = departure_var.get()
    return_date = return_var.get()
    num_travelers = num_travelers_var.get()
    total_amount = 200.00 if trip_type == "one_way" else 300.00
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    date_of_birth = dob_entry.get()
    payment_card_number = card_entry.get()
    reservation_status = "success"
    try:
        sql = "INSERT INTO reservations (trip_type, departure_date, return_date, num_travelers, total_amount, first_name, last_name, date_of_birth, payment_card_number, reservation_status) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (trip_type, departure_date, return_date, num_travelers, total_amount, first_name, last_name, date_of_birth, payment_card_number, reservation_status)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Reservation created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

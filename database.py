import sqlite3

def create_table():
    with sqlite3.connect("Booking System.db") as db:
        cursor = db.cursor()
        sql= "create table Patient_Details(NHSNumber integer, FirstName text, LastName text, Address text, PhoneNumber integer, WeeksPregnant integer, DateOfBirth integer, Primary Key(NHSNumber))"
        cursor.execute(sql)
        db.commit()

        cursor = db.cursor()
        sql= "create table Appointment_Details(AppointmentID integer, AppointmentDate integer, AppointmentTime integer, ConsultationNotes string, Primary Key(AppointmentID))"
        cursor.execute(sql)
        db.commit()

        cursor = db.cursor()
        sql= "create table Midwife_Details(MidwifeID integer, FirstName text, LastName text, Primary Key(MidwifeID))"
        cursor.execute(sql)
        db.commit()

        cursor = db.cursor()
        sql= "create table Clinic_Details(ClinicName text, ClinicAddress text, ClincEmail text, ClinicPhoneNumber integer, Primary Key(ClinicName))"
        cursor.execute(sql)
        db.commit()




if __name__ == "__main__":
    create_table()
    


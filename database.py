import sqlite3

def create_table():
    with sqlite3.connect("Booking System.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        sql= "create table Patient_Details(NHSNumber integer, FirstName text, LastName text, Street text, HouseNumber integer, Postcode text, PhoneNumber integer, WeeksPregnant integer, DateOfBirth integer, HospitalNumber, Primary Key(NHSNumber))"
        cursor.execute(sql)

     
        sql= "create table Clinic_Details(ClinicName text, ClinicAddress text, ClincEmail text, ClinicPhoneNumber integer, Primary Key(ClinicName))"
        cursor.execute(sql)
        

        sql= "create table Midwife_Details(MidwifeID integer, NHSNumber integer, FirstName text, LastName text, Primary Key(MidwifeID), Foreign Key(NHSNumber)references Patient_Details(NHSNumber))"
        cursor.execute(sql)
   

        sql= """create table Appointment_Details(AppointmentID integer, NHSNumber integer, ClinicName string, MidwifeID integer, AppointmentDate integer, AppointmentTime integer, ConsultationNotes string,  
                Primary Key(AppointmentID), Foreign Key(NHSNumber)references Patient_Details(NHSNumber), Foreign Key(ClinicName)references Clinic_Details(ClinicName), Foreign Key(MidwifeID)references Midwife_Details(MidwifeID))"""
        cursor.execute(sql)

        db.commit()

if __name__ == "__main__":
    create_table()
    


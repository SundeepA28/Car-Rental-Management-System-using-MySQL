# Car Rental Management System using MySQL
This is a simple car rental management system built using the MySQL database. The system allows users to rent a car and return it when they are finished, while also allowing the management to keep track of the available cars and their status.

# Requirements
- Xampp
- Streamlit(pip install streamlit) for ***Front End***
- Python 3.8 or higher
# Execution Steps:
- Clone or download the repository to your web server directory
- connect to the MariaDB database from the Xampp control panel
- Create a new MySQL database and import the ***Database Structure.sql*** file to create the necessary tables
- import the ***Data.sql*** file to insert the initial data
- Import ***Queries.sql*** to perform a set of different queries that can be executed on the database
   - This file contains Join Operations,Aggregate Functions,SET Operations.
- Import ***Function_Procedure_Trigger.sql*** to perform a Function,View,Procedure,Trigger Operations on the database.

### Front End
- Open the terminal and navigate to the ***Front End*** directory
- Run the following command to start the streamlit server
```bash
streamlit run app.py
```
- On the front End you can perform ***CRED** Operations on the database. You will also be provided with a Command Prompt to perform SQL Queries on the database.

# Features
Booking: Allows users to rent a car for a specified duration
Car : Allows the management/User to know all the details of a specific Car.
Car Category : Allows the User/Management to Know the car that comes under a specific Category like Sedan, SUV, etc.
               This allows us to set a fixed price for a specific category of cars.
Car Insurance : Allows the User to buy Insurance for the Car.
Car Location : Allows the User/Management to view the Location of the Car.
Customer : Allows the Management to maintain all the details of the Customer.
Payment : Allows the User to make a payment for the Car.




# Contributing
We welcome contributions to the project. If you find a bug or would like to suggest a new feature, please open an issue or submit a pull request.

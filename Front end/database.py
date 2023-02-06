import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pes1ug20cs445_car_rental_project"
)
c = mydb.cursor()



def view_all_data(table):
    c.execute('SELECT * FROM {}'.format(table))
    data = c.fetchall()

    return data

def getcolumns(table):
    c.execute('desc {}'.format(table))
    data = c.fetchall()
    return data

# view tables
def view_table(table):
    c.execute('SELECT * FROM {}'.format(table))
    data = c.fetchall()
    return data


#--------------------------------------------------------------------------------------


# add  data
def add_data_Customer(Username,LicenseNo,Firstname,Lastname,Password,email,DOB,Address,Phone_no,Gender):
    c.execute('INSERT INTO Customer(UserName,LicenseNo,Firstname,Lastname,Password,email,DOB,Address,Phone_no,Gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
               (Username,LicenseNo,Firstname,Lastname,Password,email,DOB,Address,Phone_no,Gender))
    mydb.commit()

def add_data_Location(state,city,Area,pincode):
    c.execute('INSERT INTO Location(state,city,Area,pincode) VALUES (%s,%s,%s,%s)',
                (state,city,Area,pincode))
    mydb.commit()

def add_data_car_category(category_name,no_of_persons,cost_per_day,Delay_Fee_per_hour):
    c.execute('INSERT INTO car_category(category_name,no_of_persons,cost_per_day,Delay_Fee_per_hour) VALUES (%s,%s,%s,%s)',
                (category_name,no_of_persons,cost_per_day,Delay_Fee_per_hour))

def add_data_car_detail(Registration_No,Model,Make,Model_Year,Mileage,Category,Location):
    c.execute('INSERT INTO car_details(Registration_No,Model,Make,Model_Year,Mileage,Category,Location) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                (Registration_No,Model,Make,Model_Year,Mileage,Category,Location))

def add_data_car_Insurance(Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day):
    c.execute('INSERT INTO Car_Insurance(Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day) VALUES (%s,%s,%s)',
                (Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day))

def add_data_Booking_details(Customer_ID,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_ID):
    c.execute('INSERT INTO Booking_Details(Customer_ID,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (Customer_ID,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_ID))

def add_data_Payment(Total_Amount,Payment_Method):
    c.execute('INSERT INTO Payment(Total_Amount,Payment_Method) VALUES (%s,%s)',
                (Total_Amount,Payment_Method))




#---------------------------------------------------------------------------------------







#---------------------------------------------------------------------------------------
#To Delete Tables

#view only Customer_ID
def view_Cids():
    c.execute('SELECT Customer_ID from Customer')
    data = c.fetchall()
    return data

#Delete Customer
def delete_customer_data(cid):
    c.execute('DELETE FROM Customer WHERE Customer_ID="{}"'.format(cid))
    mydb.commit()

#View Only Location ID
def view_Lids():
    c.execute('SELECT Location_ID from Location')
    data = c.fetchall()
    return data

#Delete Location
def delete_location_data(Lid):
    c.execute('DELETE FROM Location WHERE Location_ID="{}"'.format(Lid))
    mydb.commit()

#View Only car Category
def view_Car_Category():
    c.execute('SELECT category_name from car_category')
    data = c.fetchall()
    return data

#Delete Car Category
def delete_category_data(car_name):
    c.execute('DELETE FROM car_category WHERE category_name="{}"'.format(car_name))
    mydb.commit()
    

#View Only Cars
def view_RegNo():
    c.execute('SELECT Registration_No from car_detail')
    data = c.fetchall()
    return data

#Delete car
def delete_car_data(regNo):
    c.execute('DELETE FROM car_detail WHERE Registration_No="{}"'.format(regNo))
    mydb.commit()

#View Ony Insurance  
def view_Iids():
    c.execute('SELECT Insurance_ID from Car_Insurance')
    data = c.fetchall()
    return data

#Delete Insurance
def delete_Insurance_data(Iid):
    c.execute('DELETE FROM Car_Insurance WHERE Insurance_ID="{}"'.format(Iid))
    mydb.commit()
    
#View Payment
def view_Pids():
    c.execute('SELECT Payment_ID from Payment')
    data = c.fetchall()
    return data

#Delete Payment
def delete_Payment_data(Pid):
    c.execute('DELETE FROM Payment WHERE Payment_ID="{}"'.format(Pid))
    mydb.commit()

#View Booking  
def view_Bookingids():
    c.execute('SELECT Booking_ID from Booking_Details')
    data = c.fetchall()
    return data

#Delete Booking
def delete_Booking_data(Bid):
    c.execute('DELETE FROM Booking_Details WHERE Booking_ID="{}"'.format(Bid))
    mydb.commit()


#--------------------------------------------------------------------------------------------------------------------
#Update Details :

#View Customer Details : 
def get_customer(cid):
    c.execute('SELECT * FROM Customer WHERE Customer_ID="{}"'.format(cid))
    data = c.fetchall()
    return data

# update Customer Details:
def edit_customer_data(new_UserName, new_LicenseNo, new_Firstname, new_Lastname, new_Password, new_email, new_DOB, new_Address, new_phone_no,new_Gender,UserName, LicenseNo, Firstname, Lastname, Password, email, DOB, Address, phone_no,Gender):  #new_Customer_ID,Customer_ID,
    c.execute("UPDATE Customer SET UserName=%s, LicenseNo=%s, Firstname=%s, Lastname=%s, Password=%s, email=%s, DOB=%s, Address=%s, phone_no=%s,Gender=%s WHERE UserName=%s and LicenseNo=%s and Firstname=%s and Lastname=%s and Password=%s and email=%s and DOB=%s and Address=%s and phone_no=%s and Gender=%s", (new_UserName, new_LicenseNo, new_Firstname, new_Lastname, new_Password, new_email, new_DOB, new_Address, new_phone_no,new_Gender,UserName, LicenseNo, Firstname, Lastname, Password, email, DOB, Address, phone_no,Gender))# Customer_ID=%s, Customer_ID=%s and ,new_Customer_ID,Customer_ID,
    mydb.commit()
    
#View Location Details : 
def get_Location(Lid):
    c.execute('SELECT * FROM Location WHERE Location_ID="{}"'.format(Lid))
    data = c.fetchall()
    return data

# update Location Details:
def edit_Location_data(new_state, new_city, new_Area, new_pincode,state,city,Area,pincode):
    c.execute("UPDATE Location SET state=%s, city=%s, Area=%s, pincode=%s WHERE state=%s and city=%s and Area=%s and pincode=%s", ( new_state, new_city, new_Area, new_pincode,state,city,Area,pincode))
    mydb.commit()

#View Car Category:
def get_category(CCategory):
    c.execute('SELECT * FROM car_category WHERE category_name="{}"'.format(CCategory))
    data = c.fetchall()
    return data

#update Car Category:
def edit_category_data(new_no_of_persons,new_cost_per_day,new_Delay_Fee_per_hour,no_of_persons,cost_per_day,Delay_Fee_per_hour):
    c.execute("UPDATE car_category SET no_of_persons=%s,cost_per_day=%s,Delay_Fee_per_hour=%s WHERE no_of_persons=%s and cost_per_day=%s and Delay_Fee_per_hour=%s",(new_no_of_persons,new_cost_per_day,new_Delay_Fee_per_hour,no_of_persons,cost_per_day,Delay_Fee_per_hour))
    mydb.commit()

#View Car
def get_car(CRegNo):
    c.execute('SELECT * FROM car_detail WHERE Registration_No="{}"'.format(CRegNo))
    data = c.fetchall()
    return data

#Update Car Details : 
def edit_Car_data(new_Model,new_Make,new_Model_Year,new_Mileage,new_Availability,new_Category,new_Location,Model,Make,Model_Year,Mileage,Availability,Category,Location):
    c.execute('UPDATE car_detail SET Model=%s,Make=%s,Model_Year=%s,Mileage=%s,Availability=%s,Category=%s,Location=%s WHERE Model=%s and Make=%s and Model_Year=%s and Mileage=%s and Availability=%s and Category=%s and Location=%s',(new_Model,new_Make,new_Model_Year,new_Mileage,new_Availability,new_Category,new_Location,Model,Make,Model_Year,Mileage,Availability,Category,Location))
    mydb.commit()

#View Insurance:
def get_Insurance(Insurance):
    c.execute('SELECT * FROM Car_Insurance WHERE Insurance_ID="{}"'.format(Insurance))
    data = c.fetchall()
    return data

#Update Insurance:
def edit_Insurance_data(new_Insurance_Name,new_Coverage_Type,new_Insurance_Cost_Per_Day,Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day):
    c.execute('UPDATE Car_Insurance SET Insurance_Name=%s,Coverage_Type=%s,Insurance_Cost_Per_Day=%s WHERE Insurance_Name=%s and Coverage_Type=%s and Insurance_Cost_Per_Day=%s',(new_Insurance_Name,new_Coverage_Type,new_Insurance_Cost_Per_Day,Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day))
    mydb.commit()

#View Payment:
def get_Payment(Payment):
    c.execute('SELECT * FROM Payment WHERE Payment_ID="{}"'.format(Payment))
    data = c.fetchall()
    return data

#Update Payment
def edit_Payment_data(new_Total_Amount,new_Payment_Method,Total_Amount,Payment_Method):
    c.execute("UPDATE Payment SET Total_Amount=%s,Payment_Method=%s WHERE Total_Amount=%s and Payment_Method=%s",(new_Total_Amount,new_Payment_Method,Total_Amount,Payment_Method))
    mydb.commit()

#View Booking Details:
def get_Booking(Booking):
    c.execute('SELECT * FROM Booking_Details WHERE Booking_ID="{}"'.format(Booking))
    data = c.fetchall()
    return data

#Update Booking Details:
def edit_Booking_data(new_Customer_ID,new_From_Date,new_Return_Date,new_Amount,new_Actual_Return_Date,new_Pickup_Location,new_Drop_Location,new_Insurance,new_Car_Reg_No,new_Payment_ID,Customer_ID,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_ID):
    c.execute("UPDATE Booking_Details SET Customer_ID=%s,From_Date=%s,Return_Date=%s,Amount=%s,Actual_Return_Date=%s,Pickup_Location=%s,Drop_Location=%s,Insurance=%s,Car_Reg_No=%s,Payment_ID=%s WHERE Customer_ID=%s and From_Date=%s and Return_Date=%s and Amount=%s and Actual_Return_Date=%s and Pickup_Location=%s and Drop_Location=%s and Insurance=%s and Car_Reg_No=%s and Payment_ID=%s",(new_Customer_ID,new_From_Date,new_Return_Date,new_Amount,new_Actual_Return_Date,new_Pickup_Location,new_Drop_Location,new_Insurance,new_Car_Reg_No,new_Payment_ID,Customer_ID,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_ID))
    mydb.commit()


#Command Prompt
def execute_query(query):
    str(query).replace(";", '')
    if "select" in str(query).lower():
        c.execute(query)
        res = c.fetchall()
        return res,c.description

    elif "insert" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "update" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "delete" in str(query).lower():
        c.execute(query)
        mydb.commit()

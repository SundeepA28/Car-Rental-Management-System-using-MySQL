import pandas as pd
import streamlit as st



from database import view_Cids,get_customer,edit_customer_data
from database import view_Lids,get_Location,edit_Location_data
from database import view_Car_Category,get_category,edit_category_data
from database import view_RegNo,get_car,edit_Car_data
from database import view_Iids,get_Insurance,edit_Insurance_data
from database import view_Pids,get_Payment,edit_Payment_data
from database import view_Bookingids,get_Booking,edit_Booking_data

from database import view_table


def update():
    list_of_tables=['Customer','Location','car_category','car_detail','Car_Insurance','Payment','Booking_Details']
    choice=st.selectbox("Select Table to UPDATE Data", list_of_tables)

    if choice == "Customer":
        result = view_table('Customer')
        df = pd.DataFrame(result, columns=['Customer ID','UserName','LicenseNo','Firstname','Lastname','Password','E-mail','DOB','Adddress','Phone No','Gender'])
        with st.expander("Current Customer Table"):
            st.dataframe(df)
        C_ids = [i[0] for i in view_Cids()]
        selected_cid = st.selectbox("Select Customer ID", C_ids)
        selected_result = get_customer(selected_cid)
        if selected_result:
            c_id = selected_result[0][0]
            Username = selected_result[0][1]
            LicenseNo = selected_result[0][2]
            Firstname = selected_result[0][3]
            Lastname = selected_result[0][4]
            Password = selected_result[0][5]
            email = selected_result[0][6]
            DOB = selected_result[0][7]
            Address = selected_result[0][8]
            Phone_no = selected_result[0][9]
            Gender = selected_result[0][10]

        ecol1,ecol2,ecol3 = st.columns(3)
        with ecol1:
            new_Username = st.text_input("UserName",Username)
            new_LicenseNo = st.text_input("License No",LicenseNo)
            new_FirstName = st.text_input("First Name",Firstname)
        
        with ecol2:
            new_LastName = st.text_input("Last Name",Lastname)
            new_Password = st.text_input("Password",Password)
            new_email = st.text_input("Email",email)

        with ecol3:
            new_DOB = st.text_input("DOB",DOB)
            new_Address = st.text_input("Address",Address)
            new_Phone_no = st.text_input("Phone No",Phone_no)
            new_Gender = st.text_input("Gender",Gender)
        
        if st.button("Update Customer"):
            edit_customer_data(new_Username,new_LicenseNo,new_FirstName,new_LastName,new_Password,new_email,new_DOB,new_Address,new_Phone_no,new_Gender,Username,LicenseNo,Firstname,Lastname,Password,email,DOB,Address,Phone_no,Gender)#new_c_id,c_id,
            st.success("Successfully Updated Customer with ID : {} ".format(c_id))

        result2 = view_table('Customer')
        df2 = pd.DataFrame(result2, columns=['Customer ID','UserName','LicenseNo','Firstname','Lastname','Password','E-mail','DOB','Adddress','Phone No','Gender'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "Location":
        result = view_table('Location')
        df = pd.DataFrame(result, columns=['Location ID','State','City','Area','Pincode'])
        with st.expander("Current Location Table"):
            st.dataframe(df)
        L_ids = [i[0] for i in view_Lids()]
        selected_Lid = st.selectbox("Select Location ID", L_ids)
        selected_result = get_Location(selected_Lid)
        if selected_result:
            Location_id = selected_result[0][0]
            state = selected_result[0][1]
            city = selected_result[0][2]
            Area = selected_result[0][3]
            pincode =selected_result[0][4]


        ecol1,ecol2 = st.columns(2)
        with ecol1:
            new_state = st.text_input("State",state)
            new_city = st.text_input("City",city)
        
        with ecol2:
            new_Area = st.text_input("Area",Area)
            new_pincode = st.text_input("Pincode",pincode)
        
        if st.button("Update Location"):
            edit_Location_data(new_state,new_city,new_Area,new_pincode,state,city,Area,pincode)
            st.success("Successfully Updated Location ID : {} ".format(Location_id))

        result2 = view_table('Location')
        df2 = pd.DataFrame(result2, columns=['Location ID','State','City','Area','Pincode'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice=="car_category":
        result = view_table('car_category')
        df = pd.DataFrame(result, columns=['Category Name','No of Persons','Cost Per Day','Delay Fee per Hour'])
        with st.expander("Car Category Table"):
            st.dataframe(df)
        category = [i[0] for i in view_Car_Category()]
        selected_category = st.selectbox("Select Location ID", category)
        selected_result = get_category(selected_category)
        if selected_result:
            category_name = selected_result[0][0]
            no_of_persons = selected_result[0][1]
            cost_per_day = selected_result[0][2]
            Delay_Fee_per_hour = selected_result[0][3]

            #new_category_name = st.text_input("Category Name",category_name)
            new_no_of_persons = st.text_input("No of Persons",no_of_persons)
            new_cost_per_day = st.text_input("Cost Per Day",cost_per_day)
            new_Delay_Fee_per_hour = st.text_input("Delay Fee Per Hour",Delay_Fee_per_hour)
        
        if st.button("Update Car Category"):
            edit_category_data(new_no_of_persons,new_cost_per_day,new_Delay_Fee_per_hour,no_of_persons,cost_per_day,Delay_Fee_per_hour)
            st.success("Successfully Updated Category with Name : {} ".format(category_name))

        result2 = view_table('car_category')
        df2 = pd.DataFrame(result2, columns=['Category Name','No of Persons','Cost Per Day','Delay Fee per Hour'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice=="car_detail":
        result = view_table('car_detail')
        df = pd.DataFrame(result, columns=['Registration No','Model','Make','Model_Year','Mileage','Availability','Category','Location'])
        with st.expander("Car Details Table"):
            st.dataframe(df)
        car = [i[0] for i in view_RegNo()]
        selected_car = st.selectbox("Select Car", car)
        selected_result = get_car(selected_car)
        if selected_result:
            Registration_No = selected_result[0][0]
            Model = selected_result[0][1]
            Make = selected_result[0][2]
            Model_Year = selected_result[0][3]
            Mileage = selected_result[0][4]
            Availability = selected_result[0][5]
            Category = selected_result[0][6]
            Location = selected_result[0][7]
            

        ecol1,ecol2 = st.columns(2)
        with ecol1:
            #new_Registration_No = st.text_input("Registration No",Registration_No)
            new_Model = st.text_input("Model",Model)
            new_Make = st.text_input("Model",Make)
            new_Model_Year = st.text_input("Model Year",Model_Year)

        with ecol2:
            new_Mileage = st.text_input("Mileage",Mileage)
            new_Availability = st.text_input("Availability",Availability)
            new_Category = st.text_input("Category",Category)
            new_Location = st.text_input("Location",Location)
        
        if st.button("Update Car Details"):
            edit_Car_data(new_Model,new_Make,new_Model_Year,new_Mileage,new_Availability,new_Category,new_Location,Model,Make,Model_Year,Mileage,Availability,Category,Location)
            st.success("Successfully Updated Car with Registration_No : {} ".format(Registration_No))

        result2 = view_table('car_detail')
        df2 = pd.DataFrame(result2, columns=['Registration No','Model','Make','Model_Year','Mileage','Availability','Category','Location'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice=="Car_Insurance":
        result = view_table('Car_Insurance')
        df = pd.DataFrame(result, columns=['Insurance ID','Insurance Name','Coverage Type','Insurance Cost Per Day'])
        with st.expander("Car Insurance Table"):
            st.dataframe(df)
        insurance = [i[0] for i in view_Iids()]
        selected_insurance = st.selectbox("Select Car Insurance", insurance)
        selected_result = get_Insurance(selected_insurance)
        if selected_result:
            Insurance_ID = selected_result[0][0]
            Insurance_Name = selected_result[0][1]
            Coverage_Type = selected_result[0][2]
            Insurance_Cost_Per_Day = selected_result[0][3]

            #new_Insurance_No = st.text_input("Insurance ID",Insurance_ID)
            new_Insurance_Name = st.text_input("Insurance_Name",Insurance_Name)
            new_Coverage_Type = st.text_input("Coverage_Type",Coverage_Type)
            new_Insurance_Cost = st.text_input("Insurance Cost Per Day",Insurance_Cost_Per_Day)

        
        if st.button("Update Car Insurance Details"):
            edit_Insurance_data(new_Insurance_Name,new_Coverage_Type,new_Insurance_Cost,Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day)
            st.success("Successfully Updated Car Insurance with ID : {} ".format(Insurance_ID))

        result2 = view_table('Car_Insurance')
        df2 = pd.DataFrame(result2, columns=['Insurance ID','Insurance Name','Coverage Type','Insurance Cost Per Day'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Payment':
        result = view_table('Payment')
        df = pd.DataFrame(result, columns=['Payment ID','Total Amount','Payment Method'])
        with st.expander("Car Payment Table"):
            st.dataframe(df)
        Payment = [i[0] for i in view_Pids()]
        selected_payment = st.selectbox("Select Car Insurance", Payment)
        selected_result = get_Payment(selected_payment)
        if selected_result:
            Payment_ID = selected_result[0][0]
            Total_Amount = selected_result[0][1]
            Payment_Method = selected_result[0][2]
            #Payment_status = selected_result[0][3]

            #new_Payment_ID = st.text_input("Payment ID",Payment_ID)
            new_Total_Amount = st.text_input("Total Amount",Total_Amount)
            new_Payment_Method = st.text_input("Payment Method",Payment_Method)
            #new_Payment_status = st.text_input("Payment Status",Payment_status)

        
        if st.button("Update Car Payment Details"):
            edit_Payment_data(new_Total_Amount,new_Payment_Method,Total_Amount,Payment_Method)
            st.success("Successfully Updated Payment Details with ID : {} ".format(Payment_ID))

        result2 = view_table('Payment')
        df2 = pd.DataFrame(result2, columns=['Payment ID','Total Amount','Payment Method'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Booking_Details':
        result = view_table('Booking_Details')
        df = pd.DataFrame(result, columns=['Booking ID','Customer ID','From Date','Return Date','Amount','Actual Return Date','Pick Up Location','Drop Location','Insurance','Car Registration No','Payment ID'])
        with st.expander("Current Booking Details Table"):
            st.dataframe(df)
        Booking_ids = [i[0] for i in view_Bookingids()]
        selected_Bookingid = st.selectbox("Select Booking ID", Booking_ids)
        selected_result = get_Booking(selected_Bookingid)
        if selected_result:
            Booking_id = selected_result[0][0]
            Customer_id = selected_result[0][1]
            From_Date = selected_result[0][2]
            Return_Date = selected_result[0][3]
            Amount = selected_result[0][4]
            #Booking_Status = selected_result[0][5]
            Actual_Return_Date = selected_result[0][5]
            Pickup_Location = selected_result[0][6]
            Drop_Location = selected_result[0][7]
            Insurance = selected_result[0][8]
            Car_Reg_No = selected_result[0][9]
            Payment_Booking_ID = selected_result[0][10]

        ecol1,ecol2,ecol3 = st.columns(3)
        with ecol1:
            #new_Booking_id = st.text_input("Booking ID",Booking_id)
            new_Customer_id = st.text_input("Customer ID",Customer_id)
            new_From_Date = st.text_input("From Date",From_Date)
            new_Return_Date = st.text_input("Return Date",Return_Date)
        
        with ecol2:
            new_Amount = st.text_input("Amount",Amount)
            #new_Booking_Status = st.text_input("Booking Status",Booking_Status)
            new_Actual_Return_Date = st.text_input("Actual Return Date",Actual_Return_Date)
            new_Pickup_Location = st.text_input("Pick Up Location",Pickup_Location)

        with ecol3:
            new_Drop_Location = st.text_input("Drop Location",Drop_Location)
            new_Insurance = st.text_input("Insurance",Insurance)
            new_Car_Reg_No = st.text_input("Car Registration No",Car_Reg_No)
            new_Payment_Booking_ID = st.text_input("Payment ID",Payment_Booking_ID)
        
        if st.button("Update Booking Details"):
            edit_Booking_data(new_Customer_id,new_From_Date,new_Return_Date,new_Amount,new_Actual_Return_Date,new_Pickup_Location,new_Drop_Location,new_Insurance,new_Car_Reg_No,new_Payment_Booking_ID,Customer_id,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_Booking_ID)
            st.success("Successfully Updated Booking with ID : {} ".format(Booking_id))

        result2 = view_table('Booking_Details')
        df2 = pd.DataFrame(result2, columns=['Booking ID','Customer ID','From Date','Return Date','Amount','Actual Return Date','Pick Up Location','Drop Location','Insurance','Car Registration No','Payment ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)     

    else:
        st.subheader("Select Table")   






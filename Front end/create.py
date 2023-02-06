import streamlit as st
from database import add_data_Customer,add_data_Location,add_data_car_category,add_data_car_detail,add_data_car_Insurance,add_data_Booking_details,add_data_Payment


def create():
    list_of_tables=['Customer','Location','car_category','car_detail','Car_Insurance','Payment','Booking_Details']
    choice=st.selectbox("Select Table to INSERT Data", list_of_tables)

    if choice == "Customer":
        st.text("Fill out the Customer Details")
        #ecol1,ecol2,ecol3 = st.columns(3)
        username = st.text_input("Username")
        LicenseNo = st.text_input("LicenseNo")
        Firstname = st.text_input("Firstname")
        Lastname = st.text_input("Lastname")
        password = st.text_input("Password",type="password")
        email = st.text_input("Email")
        dateofbirth = st.text_input("Date of Birth(YYYY-MM-DD)")
        Address = st.text_input("Address")
        phone_no = st.text_input("Phone No")
        Gender = st.text_input("Gender")       
        
        if st.button("Add Customer Details:"):
            add_data_Customer(username,LicenseNo,Firstname,Lastname,password,email,dateofbirth,Address,phone_no,Gender)
            st.success("Successfully added Employee : {} {}".format(Firstname,Lastname))


    elif choice == "Location":
        st.text("Fill the current Location Details:")

        state = st.text_input("State:")
        city = st.text_input("City:")
        Area = st.text_input("Area:")
        pincode = st.text_input("Pincode:")


        if st.button("Add Current Location Details:"):
            add_data_Location(state,city,Area,pincode)
            st.success("Successfully added the Location Details for Pincode : {}".format(pincode))

    
    elif choice == "car_category":
        st.text("Fill the details of car_category")

        category_name = st.text_input("Category Name:")
        noofperson = st.text_input("Number of Persons:")
        costperday = st.text_input("Cost Per Day:")
        delayfee = st.text_input("Delay Fee Per Hour:")

        
        if st.button("Add Car Category"):
            add_data_car_category(category_name,noofperson,costperday,delayfee)
            st.success("Successfully added the Car Category: {}".format(category_name))


    elif choice == "car_detail":
        st.text("Fill the Car Details:")

        reg_no = st.text_input("Registration No:")
        model = st.text_input("Model:")
        make = st.text_input("Make")
        model_year = st.text_input("Model Year")
        mileage = st.text_input("Mileage")
        Category = st.text_input("Category")
        location = st.text_input("Location")
       
        if st.button("Add Car Details:"):
            add_data_car_detail(reg_no,model,make,model_year,mileage,Category,location)
            st.success("Successfully added Car Details with Registration No: {}".format(reg_no))


    elif choice == "Car_Insurance":
        st.text("Fill the Car Insurance Details:")

        name = st.text_input("Insurance Name:")
        type = st.text_input("Insurance Type:")
        cost = st.text_input("Insurance Cost Per Day:")



        if st.button("Add Car Insurance"):
            add_data_car_Insurance(name,type,cost)
            st.success("Successfully added Insurance : {}".format(name))


    elif choice == "Booking_Details":
        st.text("Fill the Booking Details:")

        cutomer_id = st.text_input("Customer ID")
        fromdate = st.text_input("From Date")
        returndate = st.text_input("Return Date")
        amount = st.text_input("Amount")
        actualReturn = st.text_input("Actual Return Date:")
        pickup = st.text_input("Pick Up Location")
        drop = st.text_input("Drop Location")
        Insurance = st.text_input("Insurance")
        carReg = st.text_input("Car Registration No:")
        payment = st.text_input("Payment ID")

        if st.button("Add Booking Details"):
            add_data_Booking_details(cutomer_id,fromdate,returndate,amount,actualReturn,pickup,drop,Insurance,carReg,payment)
            st.success("Successfully added Booking Details for Customer ID : {}".format(cutomer_id))


    elif choice == "Payment":
        st.text("Fill the details of Payment")

        TotalAmount = st.text_input("Total Amount")
        PaymentMethod = st.text_input("Payment Method")
        #PaymentStatus = st.text_input("Payment Status")

        if st.button("Add Payment Details:"):
            add_data_Payment(TotalAmount,PaymentMethod)
            st.success("Successfully added Payment Details")

    else:
        st.subheader("Select Table")

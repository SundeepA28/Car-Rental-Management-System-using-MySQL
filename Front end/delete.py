import pandas as pd
import streamlit as st

from database import view_table
from database import view_Cids,delete_customer_data
from database import view_Lids,delete_location_data
from database import view_Car_Category,delete_category_data
from database import view_RegNo,delete_car_data
from database import view_Iids,delete_Insurance_data
from database import view_Pids,delete_Payment_data
from database import view_Bookingids,delete_Booking_data


def delete():
    list_of_tables=['Customer','Location','car_category','car_detail','Car_Insurance','Payment','Booking_Details']
    choice=st.selectbox("Select Table to DELETE Data", list_of_tables)

    if choice == "Customer":
        result = view_table('Customer')
        df = pd.DataFrame(result, columns=['Customer ID','UserName','LicenseNo','Firstname','Lastname','Password','E-mail','DOB','Adddress','Phone No','Gender'])
        with st.expander("Current data in Customer Table"):
            st.dataframe(df)
        
        C_ids = [i[0] for i in view_Cids()]
        selected_Cid = st.selectbox("Select Customer ID", C_ids)
        st.warning("Do you want to Delete Customer ID:: {} ".format(selected_Cid))
        if st.button("Delete Customer"):
            delete_customer_data(selected_Cid)            
            st.success("Customer has been deleted successfully")
        
        new_result = view_table('Customer')
        df2 = pd.DataFrame(new_result, columns=['Customer ID','UserName','LicenseNo','Firstname','Lastname','Password','E-mail','DOB','Adddress','Phone No','Gender'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "Location":
        result = view_table('Location')
        df = pd.DataFrame(result, columns=['Location ID','State','City','Area','Pincode'])
        with st.expander("Current data in Location Table"):
            st.dataframe(df)
        
        L_ids = [i[0] for i in view_Lids()]
        selected_Lid = st.selectbox("Select Location ID", L_ids)
        st.warning("Do you want to Delete Location ID:: {} ".format(selected_Lid))
        if st.button("Delete Location"):
            delete_location_data(selected_Lid)            
            st.success("Location has been deleted successfully")
        
        new_result = view_table('Location')
        df2 = pd.DataFrame(new_result, columns=['Location ID','State','City','Area','Pincode'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'car_category':
        result = view_table('car_category')
        df = pd.DataFrame(result, columns=['Category Name','No of Persons','Cost Per Day','Delay Fee per Hour'])
        with st.expander("Current data in Car Category Table"):
            st.dataframe(df)
        
        category_name = [i[0] for i in view_Car_Category()]
        selected_CategoryName = st.selectbox("Select Category Name", category_name)
        st.warning("Do you want to Delete Category:: {} ".format(selected_CategoryName))
        if st.button("Delete Category Name"):
            delete_category_data(selected_CategoryName)            
            st.success("Car Category has been deleted successfully")
        
        new_result = view_table('car_category')
        df2 = pd.DataFrame(new_result, columns=['Category Name','No of Persons','Cost Per Day','Delay Fee per Hour'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'car_detail':
        result = view_table('car_detail')
        df = pd.DataFrame(result, columns=['Registration No','Model','Make','Model_Year','Mileage','Availability','Category','Location'])
        with st.expander("Current data in Car Details Table"):
            st.dataframe(df)
        
        detail_name = [i[0] for i in view_RegNo()]
        selected_detailName = st.selectbox("Select Car", detail_name)
        st.warning("Do you want to Delete Car:: {} ".format(selected_detailName))
        if st.button("Delete Car"):
            delete_car_data(selected_detailName)            
            st.success("Car has been deleted successfully")
        
        new_result = view_table('car_detail')
        df2 = pd.DataFrame(new_result, columns=['Registration No','Model','Make','Model_Year','Mileage','Availability','Category','Location'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Car_Insurance':
        result = view_table('Car_Insurance')
        df = pd.DataFrame(result, columns=['Insurance ID','Insurance Name','Coverage Type','Insurance Cost Per Day'])
        with st.expander("Current data in Car Insurance Table"):
            st.dataframe(df)
        
        Insurance = [i[0] for i in view_Iids()]
        selected_Insurance = st.selectbox("Select Insurance", Insurance)
        st.warning("Do you want to Delete Insurance:: {} ".format(selected_Insurance))
        if st.button("Delete Insurance"):
            delete_Insurance_data(selected_Insurance)            
            st.success("Insurance has been deleted successfully")
        
        new_result = view_table('Car_Insurance')
        df2 = pd.DataFrame(new_result, columns=['Insurance ID','Insurance Name','Coverage Type','Insurance Cost Per Day'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Payment':
        result = view_table('Payment')
        df = pd.DataFrame(result, columns=['Payment ID','Total Amount','Payment Method'])
        with st.expander("Current data in Payment Table"):
            st.dataframe(df)
        
        payment = [i[0] for i in view_Pids()]
        selected_Payment = st.selectbox("Select Payment", payment)
        st.warning("Do you want to Delete Payment:: {} ".format(selected_Payment))
        if st.button("Delete Payment"):
            delete_Payment_data(selected_Payment)            
            st.success("Payment has been deleted successfully")
        
        new_result = view_table('Payment')
        df2 = pd.DataFrame(new_result, columns=['Payment ID','Total Amount','Payment Method'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Booking_Details':
        result = view_table('Booking_Details')
        df = pd.DataFrame(result, columns=['Booking ID','Customer ID','From Date','Return Date','Amount','Actual Return Date','Pick Up Location','Drop Location','Insurance','Car Registration No','Payment ID'])
        with st.expander("Current data in Booking Table"):
            st.dataframe(df)
        
        Booking = [i[0] for i in view_Bookingids()]
        selected_Booking = st.selectbox("Select Insurance", Booking)
        st.warning("Do you want to Delete Booking:: {} ".format(selected_Booking))
        if st.button("Delete Booking Details"):
            delete_Booking_data(selected_Booking)            
            st.success("Booking Info has been deleted successfully")
        
        new_result = view_table('Booking_Details')
        df2 = pd.DataFrame(new_result, columns=['Booking ID','Customer ID','From Date','Return Date','Amount','Actual Return Date','Pick Up Location','Drop Location','Insurance','Car Registration No','Payment ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)


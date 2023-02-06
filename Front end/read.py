import pandas as pd
import streamlit as st
from database import view_all_data,getcolumns

def read():
    list_of_tables=['Customer','Location','car_category','car_detail','Car_Insurance','Payment','Booking_Details']
    choice=st.selectbox("Select Table to View Data", list_of_tables)
    result = view_all_data(choice)
    cols = [i[0] for i in getcolumns(choice)]
    df = pd.DataFrame(result,columns=cols)
    if st.button("View"):
        st.table(df)



# import pandas as pd
# import streamlit as st
# from database import view_table


# def read():
#     list_of_tables=['Customer','Location','car_category','car_detail','Car_Insurance','Payment','Booking_Details']
#     choice=st.selectbox("Select Table to View Data", list_of_tables)

#     if choice == "Customer":
#         st.text("Displaying Customer table")
#         res=view_table('Customer')
#         df = pd.DataFrame(res, columns=['Customer ID','UserName','LicenseNo','Firstname','Lastname','Password','E-mail','DOB','Adddress','Phone No'])
#         st.dataframe(df)
#         st.success("Successfully fetched Customer Details")

#     elif choice == "Location":
#         st.text("Displaying Location table")
#         res=view_table('Location')
#         df = pd.DataFrame(res, columns=['Location ID','State','City','Area','Pincode'])
#         st.dataframe(df)
#         st.success("Successfully fetched Location table")

#     elif choice == "car_category":
#         st.text("Displaying Car Category table")
#         res=view_table('car_category')
#         df = pd.DataFrame(res, columns=['Category Name','No of Persons','Cost Per Day','Delay Fee per Hour'])
#         st.dataframe(df)
#         st.success("Successfully fetched Car Category table")

#     elif choice == "car_detail":
#         st.text("Displaying Car Detail table")
#         res=view_table('car_detail')
#         df = pd.DataFrame(res, columns=['Registration No','Model','Make','Model_Year','Mileage','Availability','Category','Location'])
#         st.dataframe(df)
#         st.success("Successfully fetched Car Details table")

#     elif choice == "Car_Insurance":
#         st.text("Displaying Car Insurance table")
#         res=view_table('Car_Insurance')
#         df = pd.DataFrame(res, columns=['Insurance ID','Insurance Name','Coverage Type','Insurance Cost Per Day'])
#         st.dataframe(df)
#         st.success("Successfully fetched Car Insurance table")

#     elif choice == "Payment":
#         st.text("Displaying Payments table")
#         res=view_table('Payment')
#         df = pd.DataFrame(res, columns=['Payment ID','Total Amount','Payment Method','Payment Status'])
#         st.dataframe(df)
#         st.success("Successfully fetched Payment table")

#     elif choice == "Booking_Details":
#         st.text("Displaying Booking Details table")
#         res=view_table('Booking_Details')
#         df = pd.DataFrame(res, columns=['Booking ID','Customer ID','From Date','Return Date','Amount','Booking Status','Actual Return Date','Pick Up Location','Drop Location','Insurance','Car Registration No','Payment ID'])
#         st.dataframe(df)
#         st.success("Successfully fetched Booking Details table")

#     else:
#         st.subheader("Select Tables")




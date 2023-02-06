import pandas as pd
import streamlit as st

from database import execute_query

def command():
    st.text("Enter Command to be Executed in MySQL")
    q = st.text_area("Command")
    if st.button("Execute"):
        if 'select' in str(q).lower():
            res,desc=execute_query(q)
            st.success("Successfully Executed the Query")
            st.table(pd.DataFrame(res, columns=[col[0] for col in desc]))
        
        else:
            execute_query(q)
            st.success("Successfully Executed the Query")

# Import python packages
import streamlit as st
import requests
#from snowflake.snowpark.functions import col

# from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Customer Your Smoothie :cup_with_straw:")
st.write("Choose the fruits you want in your custom Smoothie" )



cnx = st.connection ("snowflake")
session = cnx.session()
# session = get_active_session()

    

# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Customer Your Smoothie :cup_with_straw:")
st.write("Choose the fruits you want in your custom Smoothie")

from snowflake.snowpark.functions import col
session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))

#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose Upto 5 Ingredients:'
    ,my_dataframe)

if ingredients_list:
    sqlstatement = ''
    ingredients_string=''
    for  furit_choosen in ingredients_list:
        ingredients_string +=   furit_choosen + '    ';

    sqlstatement = """ insert into smoothies.public.orders(ingredients)
                values ('""" + ingredients_string + """')""";

    time_to_insert = st.button("Submit Order")
    
    if time_to_insert:

        session.sql(sqlstatement).collect()
        st.success('Your Smoothie is ordered!', icon="✅")




# Import python packages
import streamlit as st
import requests

# from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Customer Your Smoothie :cup_with_straw:")
st.write("Choose the fruits you want in your custom Smoothie")


from snowflake.snowpark.functions import col
cnx = st.connection ("snowflake")
session = cnx.session()
# session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))
#my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('SEARCH_ON'))
st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list = st.multiselect(
    'Choose Upto 5 Ingredients:'
    ,my_dataframe)

if ingredients_list:
    sqlstatement = ''
    ingredients_string=''
    for  fruit_choosen in ingredients_list:
        ingredients_string +=   fruit_choosen + ' '  
        st.subheader(fruit_choosen + ' Nutrition Information')
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choosen)
        fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width= True)
        
    sqlstatement = """ insert into smoothies.public.orders(ingredients)
                values ('""" + ingredients_string + """')""";

    time_to_insert = st.button("Submit Order")
    

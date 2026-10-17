#Basic Streamlit Topics
#what is streamlit?
#streamlit is a library for creating web applications.
#it is a free and open-source library for creating web applications.

import streamlit as st 

st.write("This is normal Text using write function")  #to write text to the screen  
st.title("This is a title using title function")  #to create a title
st.header("This is a header using header function")  #to create a header
st.subheader("This is a subheader using subheader function")  #to create a subheader
st.text("This is a text using text function")  #to create a text
st.markdown("This is a markdown using markdown function")  #to create a markdown
st.code("This is a code using code function")  #to create a code
#st.quote("This is a quote using quote function")  #to create a quote

#Advanced Streamlit Topics with valid syntax    for radio, selectbox, multiselect, slider, number_input, text_input, text_area#print with the correct function instead of Click me like radio, selectbox, multiselect, slider, number_input, text_input, text_area
st.radio("radio", ["Option 1", "Option 2", "Option 3"])  #to create a radio
st.selectbox("selectbox", ["Option 1", "Option 2", "Option 3"])  #to create a selectbox
st.multiselect("multiselect", ["Option 1", "Option 2", "Option 3"])  #to create a multiselect
st.slider("slider", 0, 100, 1)  #to create a slider
st.number_input("number_input", 0, 100, 1)  #to create a number input
st.text_input("text_input")  #to create a text input
st.text_area("text_area", "This is a text area")  #to create a text area

#
#how to run a streamlit app?
#streamlit run your_script.py

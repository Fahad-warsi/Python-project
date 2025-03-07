#BMI Calculator

import streamlit as st

st.title("WelCome to BMI Calculator")
weight = st.number_input("Enter your weight in (kgs)")

height_selection = st.radio("Select your height format", ("cms", "feet", "meter"))
st.write(height_selection)
height_selected = st.number_input(f"Enter your height in {height_selection}")

if st.button("Calculate BMI"):
    if height_selection == "cms":
        ht = height_selected / 2.54 / 39.36
        bmi_calc = weight / (ht * ht)
        
        
    elif height_selection == "feet":
        ht = height_selected  * 12 / 39.36
        bmi_calc = weight / (ht * ht)
    elif height_selection == 'meter':
        bmi_calc = weight / (height_selected * height_selected)
        
    st.write(f"Your BMI Index is : {bmi_calc}")
    
    if bmi_calc <= 18.5:
        st.warning(f"underweight")
    elif bmi_calc >= 18.5 and bmi_calc <= 24.9:
        st.success(f"Normal weight")
    elif bmi_calc >= 25 and bmi_calc < 29.9:
        st.warning(f"Overweight")
    elif bmi_calc >= 30:
        st.warning(f"Extremely Overweight")
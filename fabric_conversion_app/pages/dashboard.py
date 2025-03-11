import streamlit as st

hide_sidebar_css = '''
    <style>
    section[data-testid='stSidebar'] {
        display: none;
    }
    .main .block container {
        max-width: 100%
    }
    </style>

'''
st.markdown(hide_sidebar_css,unsafe_allow_html=True)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You are not logged in. Please log in to access the dashboard.")
    st.switch_page("pages/login.py")


st.title("Fabric Measurement Conversion Dashboard")
st.write("Welcome to the Fabric Conversion App! Use this tool to convert fabric measurements between meters and kilograms.")

# Logout button
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = None
    st.success("You have been logged out.")
    st.switch_page("pages/login.py")
    
tab1, tab2 = st.tabs(["Fabric MTR to KGS","Fabric KGS to MTR"])
with tab1:
    st.header("Convert Fabric Length (Meters) to Weight (Kilograms)")
    st.write("Enter the fabric details to calculate the weight in kilograms.")
    
    st.write(f"Please provide the details below:")
    fabric_total_length = st.number_input(f"Fabric Total Length:",help="Length of the fabric in meters.")
    fabric_gsm = st.number_input(f"Fabric GSM: ",help="Weight of the fabric in grams per square meter.")
    
    fabric_width = st.selectbox("Please select fabric width in Meter or Inch ",["METER", "INCH"])
    selected_width = st.number_input(f"Please Enter width in {fabric_width}", help="Unit of measurement for fabric width.")
    
    if st.button("Convert"):
        if fabric_total_length > 0:
            if fabric_gsm > 0:
                if selected_width > 0:
                     if fabric_width == "METER":
                        total_kgs = fabric_total_length * (fabric_gsm/1000) * selected_width 
                     else:
                        total_kgs = fabric_total_length * (fabric_gsm/1000) * (selected_width/39.36) 
        
                     st.success(f"Fabric required  **{total_kgs:.2f}** KGS for {fabric_total_length} MTR ")
                else: 
                    st.error(f"Please input the fabric width in METER or INCH")
            else: 
                st.error("Please input the Fabric GSM: ")
        else:
            st.error(f"Please input the total length of Fabric (i.e: Required METER:)") 
   
with tab2:
    st.header("Convert Fabric Weight (Kilograms) to Length (Meters)")
    st.write("Enter the fabric details to calculate the length in meters.")
    
    fabric_total_kgs = st.number_input(f"Fabric Total weight in KGS:",help="Length of the fabric in meters.")
    fabric_gsm = st.number_input(f"Fabric GSM: ",key="kgs_to_meter_gsm",help="Weight of the fabric in grams per square meter.")
    
    fabric_width = st.selectbox("Please select fabric width in Meter or Inch ",["METER", "INCH"],key="kgs_to_meter_width")
    selected_width = st.number_input(f"Please Enter width in {fabric_width}",key="kgs_to_meter_selected_width", help="Unit of measurement for fabric width.")
    
    if st.button("Convert",key="kgs_to_meter_button"):
        if fabric_total_kgs > 0:
            if fabric_gsm > 0:
                if selected_width > 0:
                     if fabric_width == "METER":
                        total_mtr = fabric_total_kgs / ((fabric_gsm/1000) * selected_width) 
                     else:
                        total_mtr = fabric_total_kgs / ((fabric_gsm/1000) * (selected_width/39.36))
        
                     st.success(f"Fabric required  **{total_mtr:.2f}** MTR for {fabric_total_kgs} KGS ")
                else: 
                    st.error(f"Please input the fabric width in METER or INCH")
            else: 
                st.error("Please input the Fabric GSM: ")
        else:
            st.error(f"Please input the total KGS of Fabric (i.e: Required KGS:)") 

        
    
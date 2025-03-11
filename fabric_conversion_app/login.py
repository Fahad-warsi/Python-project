import streamlit as st
import sqlite3
import hashlib

hide_sidebar_css = """
    <style>
        section[data-testid="stSidebar"] { 
            display: none;
           } 
        .main .block container{
            max-width=100%l
        }
    </style>
"""


st.markdown(hide_sidebar_css,unsafe_allow_html=True)


st.title("Welcome to Fabric conversion PRO")

# if st.button("LOGIN PAGE"):
#     st.switch_page("pages/login.py")
# if st.button("SIGN-UP PAGE"):
#     st.switch_page("pages/signup.py")
    
# # if not st.session_state.logged_in:
# #     st.switch("pages/login.py")
#Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#fuction to verify user
def verify_user(user_name,password):
    try:
        with sqlite3.connect("auth.db") as conn:
            c = conn.cursor()
            c.execute("SELECT username FROM users WHERE username = ?",(user_name,))
            result = c.fetchone()
            if result:
                c.execute("SELECT password FROM users WHERE username = ?", (user_name,))
                stored_password = c.fetchone()
                password = hash_password(password)
                if stored_password[0] == password:
                    st.session_state.logged_in = True
                    st.session_state.username = user_name
                    st.success(f"login successfully... redirecting to dashboard!!!!")
                    st.switch_page("pages/dashboard.py")  # Redirect to dashboard
                    # st.experimental_rerun()  # Refresh the page to redirect
                    
                else:
                    st.error("Invalid password or user name")
            else:
                st.error(f"User not exists....")
    except sqlite3.Error as e:
        st.write(f"Database Error = {e}")
    finally:
        if c:
            c.close()
            
def login_page():            
    st.title("Welcome to LOGIN Page")

    user_name = st.text_input(f"User Name: ")
    password = st.text_input(f"Password: ", type="password")


    if st.button("LOGIN"):
        if user_name and password:
            verify_user(user_name,password)
        else:
            st.error(f"Please enter both user name and password....")
            

# Main Logic for Login Page
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page() # Show login page if not logged in
else:
     st.switch_page("pages/dashboard.py")  # Redirect to dashboard if logged in     

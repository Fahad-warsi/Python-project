import streamlit as st
import hashlib
import sqlite3


hide_sidebar_css = """
    <style>
        section[data-testid="stSidebar"] { 
            display: none;
           } 
        .main .block container{
            max-width=100%
        }
    </style>
"""

st.markdown(hide_sidebar_css,unsafe_allow_html=True)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

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
                    # store_login_state(user_name)  # Save login session                    
                    st.success("Login successful! Redirecting to dashboard...")                    
                    # st.rerun()  # Refresh the page to go to dashboard
                    st.switch_page("pages/dashboard.py")
                    
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
            




if not st.session_state.logged_in:
    login_page()
else:
    st.switch_page("pages/dashboard.py")
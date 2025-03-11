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
st.title("Welcome to SIGN-UP Page")
new_user = st.text_input(f"Please Enter your name: ")
new_password = st.text_input(f"Please Enter your password:", type="password")

#Function to hash Password
def hash_password(new_password):
    return hashlib.sha256(new_password.encode()).hexdigest()

#Add new user and hash the password
def add_user(new_user,new_password):
    try: 
        with sqlite3.connect("auth.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users WHERE username = ?",(new_user,))
            result = cursor.fetchone()
            if result:
                    st.error(f"User Already exists")
            else:
                password = hash_password(new_password)
                cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(new_user,password))
                conn.commit()
                st.write("Added user successfully")
    except sqlite3.Error as e:
        st.error(f"Database Error = {e}")
    finally:
        if conn:
            conn.close()

if st.button("SIGN UP"):
    if new_user and new_password:
        add_user(new_user,new_password)
    else:
        st.error(f"Please enter both user name and password")
        

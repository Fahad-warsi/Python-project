import streamlit as st #import streamlit libiries
import re #import regex libiries for seraching exact string
import random
import string

#Sidebar for navigation and description
# Sidebar for "About This App"
st.sidebar.title("🔐 Password Tools")
st.sidebar.markdown("---")  # Horizontal line for separation

# About This App Section
st.sidebar.markdown("""
    ### About This App
    This application provides two tools:
    1. **Password Strength Meter**: Check the strength of your password.
    2. **Password Generator**: Generate a strong and secure password.

    #### Password Strength Meter
    It evaluates your password based on the following criteria:
    - **Length**: At least 8 characters.
    - **Uppercase and Lowercase Letters**: Must contain both.
    - **Numbers**: At least one digit (0-9).
    - **Special Characters**: At least one special character (!@#$%^&*).
    - **Blacklist Check**: Ensures your password is not common or blacklisted.

    #### Password Generator
    It generates a strong password that includes:
    - Uppercase and lowercase letters.
    - Numbers.
    - Special characters.
    - Customizable length (8 to 20 characters).
""")

st.sidebar.markdown("---")  # Horizontal line for separation

# How to Use Section
st.sidebar.markdown("""
    ### How to Use
    1. **Password Strength Meter**:
        - Enter your password in the input field.
        - Click the **Check Password Strength** button.
        - View the results and feedback to improve your password.

    2. **Password Generator**:
        - Select the desired password length.
        - Click the **Generate Password** button.
        - Copy the generated password and use it.
""")

st.sidebar.markdown("---")  # Horizontal line for separation

st.title("🔐 PASSWORD STRENGTH METER & 🔑 GENERATOR")
st.write("Generate a strong password or check the strength of your existing password.")
#Creating two tab
tab1,tab2 = st.tabs(["🔐PASSWORD STRENGTH METER", "🔑PASSWORD GENERATOR"])
# Display content based on the selected tab

with tab1:    
    st.write(f"### 🔐PASSWORD STRENGTH METER")
    st.subheader(f"Enter your password below to see how secure it is:")
        #input password field
    password = st.text_input(f"Please Enter your password", type="password")
        #function for password strength check
    def password_check(password):
        score = 0
        feedback = []
            #list of common password
        blacklist_password = ['password123', '12345678', "87654321", '12312312',
                                'admin123', 'user1234', 'pakistan', 'karachi', 'lahore12']
        if password in blacklist_password: #check password in blacklist password list
            st.write(f"Your password is not strong enough. It's either too common or blacklisted. Try a more secure option.")
            return 0, ["Password is too common or blacklisted."]

        if len(password) > 8:
            score += 1
        else:
            feedback.append(f"❌ Password should be at least 8 characters long.")
        if re.search(r'[a-z]',password) and re.search(r'[A-Z]',password):
            score += 1
        else:
            feedback.append(f"❌ Include both uppercase and lowercase letters.")
        if re.search(r'[\d]',password):
            score += 1
        else:
            feedback.append(f"❌ Add at least one number (0-9).")
        if re.search(r'[!@#$%^&*]',password):
            score += 1
        else:
            feedback.append(f"❌ Include at least one special character (!@#$%^&*).")
        return score, feedback
            
        #click button for call password check password
    if st.button("🔎Check password strength"):
            if len(password) > 0:
                score, feedback = password_check(password)
                
                # Display strength rating with progress bar and color-coded text
                st.write("### 📊 Password Strength Meter")

                # Progress bar
                progress = score / 4
                st.progress(progress)
                
                #strength rating 
                if score == 4:
                    st.success(f"✅ Your password is strong!")
                elif score == 3:
                    st.warning(f"⚠️ Your password is moderate. Consider improving it.")
                else:
                    st.error(f"❌ Your password is weak. Please follow the feedback below.")
                
            #feedback print
                if feedback:
                    st.write(f"Feedback to improve your password:")
                    for item in feedback:
                        st.write(item)
            
            else:
                st.error(f"** Please enter a password to check its strength. ** ")
            
#password generator section

    with tab2:
        st.write("### 🔑 PASSWORD GENERATOR")
        password_length = st.slider("Please select password length:", max_value= 20, min_value=8, value=12)
        uppar_case = st.checkbox("Include Uppar-Case Letters", value=True)
        lower_case = st.checkbox("Include Lower-Case Letters",value=True)
        digit = st.checkbox("Include Number",value=True)
        special_character = st.checkbox("Include special character",value=True)
        
        def password_generator(password_length=12,uppar_case=True,lower_case=True,digit=True,special_character=True):
            uppar_case = string.ascii_uppercase if uppar_case else ""
            lower_case = string.ascii_lowercase if lower_case else ""
            digit = string.digits if digit else ""
            special_character = "!@#$%^&*" if special_character else ""
            
            all_character = uppar_case + lower_case + digit + special_character
            password = []
            
            for _ in range(password_length):
                password.append(random.choice(all_character))
                
            random.shuffle(password)
            return "".join(password)
        
        if st.button("🔑Password Generator"):
            password = password_generator(password_length,uppar_case,lower_case,digit,special_character)
            st.write(f"**Password Generated:** {password}")
        
        
    
#Footer section 
st.markdown("---")                
st.markdown(
    """
    <style>
        .footer{
            position: fixed,
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: black;
            padding: 10px;
            text-align: center;
        }
    </style>
    <div class="footer">
        Develop by <strong>Fahad Warsi</strong>
    </div>
    """,
    unsafe_allow_html=True
    
)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def password_generator(length=12):
    #     #declare the set of character
    #     lowercase = string.ascii_lowercase
    #     uppercase = string.ascii_uppercase
    #     digits = string.digits
    #     special_character = "!@#$%^&*"
        
    #     all_combined = lowercase + uppercase + digits + special_character
    #     password = [
    #         random.choice(lowercase),
    #         random.choice(uppercase),
    #         random.choice(digits),
    #         random.choice(special_character)
    #     ]
    #     for _ in range(length - 4):
    #         password.append(random.choice(all_combined))
    #     random.shuffle(password)
    #     return ''.join(password)
    
    # if st.button("🔑Password Generator"):
    #     new_password = password_generator()
    #     st.success(f"**Generated Password:**: {new_password}")
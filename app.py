import streamlit as st
import streamlit_authenticator as stauth

# hashed_passwords = stauth.Hasher(['iotracx@2023']).generate()
# print(hashed_passwords)

import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.write(f'Welcome *{name}*')
    st.title('Some content')
    authenticator.logout('Logout', 'main', key='unique_key')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

# Password Reset
# if authentication_status:
#     try:
#         if authenticator.reset_password(username, 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)

# User Registeration
# try:
#     if authenticator.register_user('Register user', preauthorization=False):
#         st.success('User registered successfully')
# except Exception as e:
#     st.error(e)

#Forgot Password widget
# try:
#     username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password('Forgot password')
#     if username_of_forgotten_password:
#         st.success('New password sent securely')
#         # Random password to be transferred to user securely
#     else:
#         st.error('Username not found')
# except Exception as e:
#     st.error(e)
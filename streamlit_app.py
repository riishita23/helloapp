import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Air Quality Index", layout="wide")

# Initialize session state for users if it doesn't exist
if "users" not in st.session_state:
    st.session_state["users"] = {"admin": "password123"}  # Pre-defined admin user

# Initialize session states for authentication and navigation
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "show_signup" not in st.session_state:
    st.session_state["show_signup"] = False

def show_login_page():
    """Display the login page."""
    st.markdown(
        """
        <h1 style="text-align: center; color: skyblue;">
             Login to Access the Dashboard
        </h1>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<hr>", unsafe_allow_html=True)

    # Input fields for username and password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        # Authentication logic
        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.session_state["authenticated"] = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password!")

    # Button to navigate to the sign-up page
    if st.button("Sign Up"):
        st.session_state["show_signup"] = True
        st.rerun()

def show_signup_page():
    """Display the sign-up page."""
    st.markdown(
        """
        <h1 style="text-align: center; color: green;">
             Sign Up to Create an Account
        </h1>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<hr>", unsafe_allow_html=True)

    # Input fields for new username and password
    new_username = st.text_input("New Username:")
    new_password = st.text_input("New Password:", type="password")
    confirm_password = st.text_input("Confirm Password:", type="password")

    if st.button("Create Account"):
        # Check if the username is already taken
        if new_username in st.session_state["users"]:
            st.error("Username already exists! Try a different one.")
        elif new_password != confirm_password:
            st.error("Passwords do not match!")
        else:
            # Add new user to session state
            st.session_state["users"][new_username] = new_password
            st.success("Account created successfully! You can now log in.")
            st.session_state["show_signup"] = False
            st.rerun()

    # Button to navigate back to the login page
    if st.button("Back to Login"):
        st.session_state["show_signup"] = False
        st.rerun()

def show_dashboard():
    """Display the dashboard page."""
    st.markdown(
        """
        <h1 style="text-align: center; color: black;">
             AIR QUALITY INDEX
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Power BI Dashboard URL
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMjNmZTk3NDgtY2Y5MS00ODIwLWFmZWMtYjdlYTg2NzE2ODE1IiwidCI6IjljNWMxZjUyLTRjNTgtNDJlMy05OGVjLWYzMWVmMzk1ZWViMiJ9"

    # Embed Power BI dashboard using an iframe
    st.markdown(
        f"""
        <iframe 
            src="{power_bi_url}" 
            width="100%" 
            height="800"
            frameborder="0" 
            allowfullscreen="true">
        </iframe>
        """,
        unsafe_allow_html=True,
    )

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

# Authentication state management
if st.session_state["authenticated"]:
    show_dashboard()
elif st.session_state["show_signup"]:
    show_signup_page()
else:
    show_login_page()

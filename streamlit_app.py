import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Air Quality Index", layout="wide")


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
        # Simple authentication logic
        if username == "admin" and password == "password123":
            st.session_state["authenticated"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password!")


def show_dashboard():
    """Display the dashboard page."""
    # Title
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

    # Logout buttons
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.experimental_rerun()


# Authentication state management
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state["authenticated"]:
    show_dashboard()
else:
    show_login_page()

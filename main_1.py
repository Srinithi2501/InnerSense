import streamlit as st
import subprocess

# Define function to launch Streamlit app
def launch_streamlit_app(app_name):
    subprocess.Popen(["streamlit", "run", f"D:\Abel\old_abel\gemini\{app_name}.py"])

# Main Streamlit application
def main():
    # Set Streamlit page configuration
    st.set_page_config(layout="wide", page_title="InnerSure", page_icon=":brain:")

    # Define custom CSS styles
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #E6F3FF; /* Light blue */
        }
        body {
            color: black; /* Foreground color */
            background-color: white; /* Background color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display main page content
    st.title("InnerSure!!")
    st.video("D:\Abel\old_abel\Satwa\welcome_new.mp4")

    # Sidebar with navigation buttons
    st.sidebar.title("Navigation")
    selected_option = st.sidebar.radio("Go to:", ("Core", "Reports", "Rehabilitation Centre"))

    # Launch the corresponding Streamlit app based on the selected option
    if selected_option == "Core":
        launch_streamlit_app("core")
    elif selected_option == "Reports":
        launch_streamlit_app("rep")
    elif selected_option == "Rehabilitation Centre":
        launch_streamlit_app("rehab")

if __name__ == "__main__":
    main()


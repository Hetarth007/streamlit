import streamlit as st
import subprocess

# Title of the application
st.title('Run focus1.py Web Application')

# Button to run the script
if st.button('Run focus1.py'):
    # Run the focus1.py script and capture the output
    result = subprocess.run(['python', 'focus1.py'], capture_output=True, text=True)
    # Display the output in the web app
    st.text(result.stdout)
    st.text(result.stderr)

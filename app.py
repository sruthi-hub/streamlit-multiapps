import streamlit as st
from multiapp import MultiApp
from apps import about, main_app # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("About", about.app)
app.add_app("Network entropy calculator", main_app.app)

# The main app
app.run()

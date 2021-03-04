import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, main_app # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Network entropy calculator", main_app.app)

# The main app
app.run()

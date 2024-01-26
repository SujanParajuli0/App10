import streamlit as st
import plotly.express as px
import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("/Users/sujanparajuli/PycharmProjects/App10/data.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM temperatures")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature FROM temperatures")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figure = px.line(x=date, y=temperature,
                 labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)

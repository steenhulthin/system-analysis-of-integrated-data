import streamlit as st
import time

about = "SAID the game is a survival game in on the harshes and mentally demanding places in the world - the office."

def stream_data():
    for word in about.split(" "): # split the text into tokens based on the specified delimiter " " with the split() function
        yield word + " "
        time.sleep(0.12)



st.write_stream(stream_data)

# Initialize session state
if 'health' not in st.session_state:
    st.session_state.health = 100
if 'skills' not in st.session_state:
    st.session_state.skills = []

# Display health bar
st.write("Health:")
st.progress(st.session_state.health / 100)

# Skill tree
st.write("Skill Tree:")
if st.button("Unlock Fireball"):
    st.session_state.skills.append("Fireball")
if st.button("Unlock Shield"):
    st.session_state.skills.append("Shield")

st.write("Unlocked Skills:", st.session_state.skills)

# Story interaction
st.write("You encounter a wild beast!")
if st.button("Fight"):
    st.session_state.health -= 20
    st.write("You fought bravely but lost some health.")
elif st.button("Run"):
    st.write("You escaped safely.")
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import pickle

with open(r"C:\Users\kwabe\OneDrive\Desktop\ai\model.pkl", "rb") as file:
    model = pickle.load(file)
with open(r"C:\Users\kwabe\OneDrive\Desktop\ai\scaler_obj.pkl", "rb") as scaler:
    scale = pickle.load(scaler)

st.set_page_config(
    page_title="PLAYER RATING PREDICTIONS",
    page_icon=":sports_medal:",
    layout="centered",
    initial_sidebar_state="expanded",
  
)
st.header("Welcome Soccer Fans")
st.subheader("Rate your Favourite Players Today with AI!!",divider="violet")
player_name = st.text_input("Which player are you rating today?")

if player_name:
    age = st.text_input(f"How old is {player_name}?")
    value_eur = st.text_input(f"What is {player_name}'s monetary value in euros??", 0)
    release_clause_eur = st.text_input(f"How much is {player_name}'s release clause in euros?", 0)
    potential = st.slider("What is their potential on a scale of one to hundred?", 1, 100)
    movement_reactions = st.slider("How fast are his movement reactions on a scale of 1-100?", 1, 100)

    user_input = [value_eur, release_clause_eur, age, potential, movement_reactions]
    column_names = [ "value_eur", "release_clause_eur", "age", "potential", "movement_reactions"]
    button= st.button("Predict")

    if button:
        hello = pd.DataFrame([user_input], columns= column_names)
        scaled_data = scale.transform(hello)
        prediction = model.predict(scaled_data)[0]
        predict = round(prediction)
        st.text(f" Our AI says, {player_name}'s rating is {predict}!!")




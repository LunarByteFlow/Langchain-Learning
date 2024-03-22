import langchain_helper as lh
import streamlit as st 

st.title("Ask me Name for your Pet, According to Your Pet white[cool]")
user_animal_type = st.sidebar.selectbox("What is your pet?",("Cat","Dog","Hamster","Cow","Horse","Turtle"))

if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label = "What Color is Your Cat" ,max_chars = 15)

if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label = "What Color is Your Dog" ,max_chars = 15)

if user_animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label = "What Color is Your Hamster" ,max_chars = 15)


if user_animal_type == "Cow":
    pet_color = st.sidebar.text_area(label = "What Color is Your Cow" ,max_chars = 15)

if user_animal_type == "Horse":
    pet_color = st.sidebar.text_area(label = "What Color is Your Horse" ,max_chars = 15)

if user_animal_type == "Turtle":
    pet_color = st.sidebar.text_area(label = "What Color is Your Turtle" ,max_chars = 15)

if pet_color:
    response = lh.generate_pet_name(user_animal_type, pet_color)
    st.text(response)




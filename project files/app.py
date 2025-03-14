import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyCeHSulUwiSERD4duNkfujVXn74mixPj1Q"))

# Function to Generate Blog Content
def generate_blog(topic, word_count):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content(f"Write a {word_count}-word blog about {topic}")
    return response.text

# Streamlit UI
st.title("📝 BlogMaster: AI-Powered Blog Generator")

st.image("Blogmaster.jpg", use_column_width=True)  # Ensure this line is present


st.write("### 🤖 Hello! I’m BlogMaster, your AI writing assistant. Let's create an amazing blog!")

# User Input
topic = st.text_input("Enter Blog Topic:", "")
word_count = st.number_input("Number of Words:", min_value=100, max_value=5000, value=1000, step=50)

if st.button("Generate Blog"):
    if topic and word_count:
        blog_content = generate_blog(topic, word_count)
        st.write(blog_content)
    else:
        st.error("Please provide both the topic and the number of words.")
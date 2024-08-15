
import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

genai.configure(api_key = google_gemini_api_key)

# Set up the generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Set up safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Setting up the model
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


# Title and Configuration of the Streamlit App
st.set_page_config(layout="wide")
st.title("WriteWise: Your Intelligent Writing Assistant 📝🤖")
st.subheader("Create flawless blogs with AI assistance. WriteWise is your new AI-powered blog companion.")
# Sidebar for User Input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.header("Enter Details of the Blog You Want to Generate")

    # Input fields for Blog Title, Keywords, and Number of Words
    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_of_words = st.slider("Number of Words", min_value=250, max_value=1000, step=10)

    # Submit Button
    st.markdown("""
       <style>
       .stButton>button {
           width: 100%;
           display: flex;
           justify-content: center;
       }
       </style>
       """, unsafe_allow_html=True)
    submit_button = st.button("Generate Blog")

    # Create prompt based on user input
    prompt = f"Generate a comprehensive and engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Ensure to incorporate these keywords throughout the blog post. The post must be approximately \"{num_of_words}\" words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
# Generate content based on the prompt when the button is clicked
if submit_button:
    response = model.generate_content(prompt)
    st.write(response.text)

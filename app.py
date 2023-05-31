import streamlit as st
from transformers import pipeline

st.title("Text Generation with EleutherAI/gpt-neo-2.7B")

# Load the text generation model
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# Generate text based on user input
user_input = st.text_input("Enter a prompt:", "EleutherAI has")
output_length = st.slider("Output Length", min_value=10, max_value=100, value=50, step=10)

if st.button("Generate"):
    with st.spinner("Generating text..."):
        generated_text = generator(user_input, do_sample=True, min_length=output_length)[0]['generated_text']
    st.success("Text generated successfully!")
    st.write(generated_text)

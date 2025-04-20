# These are our imports of This project

""" This project is demonststing the Power of Using Machine Learning and NLP in the creation of making a Fake News
 Dection software in which a user can copy and paste a URL into the UserInterface in which they will be able to Get a fact Check
 on Reasoning why its Real or Fake, Demonstating the true power of this detection software...
"""

import streamlit as st
from newspaper import Article
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from openai import OpenAI
from huggingface_hub import login
from dotenv import load_dotenv
import os

# --- This is the Tokken COnfiguration Phase ---
load_dotenv()  

openai_api_key = os.getenv("OPENAI_API_KEY") # Apply OpenAI Tokken here in seperate folder
hf_token = os.getenv("HF_TOKEN") # Apply HuggingFace Tokken here in seperate folder
         
client = OpenAI(api_key=openai_api_key)
login(token=hf_token)

model_name = "jy46604790/Fake-News-Bert-Detect"  # This is an open-Source model than can be replaces with a better model as preferred
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# --- This is our User Interface Phase using StreamLit ---
st.set_page_config(page_title="Fake News Detector 🕵️", layout="centered")
st.title("🕵️‍♂️ Fake News Detector & Fact Checker")
st.caption("Check if a news article is fake or real, and extract key factual claims.")

url = st.text_input("📥 Paste the URL of a news article:")

if st.button("🔍 Analyze This Article"):
    try:
        article = Article(url)
        article.download()
        article.parse()

        st.subheader("📰 Article Details...")
        st.write(f"**Title:** {article.title}")
        st.write(article.text[:500] + "..." if len(article.text) > 500 else article.text)

        # Prediction of fake or real
        inputs = tokenizer(article.text[:512], return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()
        label = "✅ This Article is REAL NEWS" if predicted_class == 0 else "🕵️‍♂️ This Article is FAKE NEWS"
        st.success(f"Result: **{label}**")

        # Extract factual claims with GPT-4
        st.subheader("📌 Factual Claims")
        with st.spinner("Extracting factual claims using GPT-4..."):
            prompt = f"Extract 2–3 factual claims from this article:\n{article.text[:1000]}"
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            claims = response.choices[0].message.content
            st.write(claims)

    except Exception as e:
        st.error(f"❌ Error: {e}")

# To run this program we will be Running this Command: streamlit run app.py

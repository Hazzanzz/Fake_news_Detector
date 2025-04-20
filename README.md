# 🕵️‍♂️ Fake News Detector & Fact Checker

An AI-powered web app that detects fake news from any online article and extracts factual claims using large language models.

---

## 🚀 Features

- 📰 **Paste any news article URL**
- 🧠 **Classifies article as Real or Fake** using a fine-tuned BERT model
- 🤖 **Extracts 2–3 factual claims** from the article using GPT-4
- 🎨 **Modern, aesthetic web UI** built with Streamlit
- 🔒 **Secure API integration** with environment variables

---

## 🧠 Technologies Used

| Tech | Purpose |
|------|---------|
| 🧪 `Transformers (Hugging Face)` | Fake news classification using `jy46604790/Fake-News-Bert-Detect` |
| 🤖 `OpenAI GPT-4` | Factual claim extraction |
| 📜 `newspaper3k` | Scraping and parsing full news articles from URLs |
| 💻 `Streamlit` | Frontend UI for seamless user interaction |
| 🔐 `dotenv` | Secure API key management |

---

## 🖼️ Demo Screenshot

![Fake News Detector UI]([file:///C:/Users/hassz/OneDrive/Pictures/Screenshot%202025-04-19%20212429.png](https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22Screenshot%202025-04-19%20212429.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-04-19T01%3A25%3A43.855Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F9c8897d3321944ba%2FScreenshot%25202025-04-19%2520212429.png%3FExpires%3D1839720344%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3Dclruenp44-sLG3ffD~LeLdiciFfixNG5LJdE73lT5J~DPB73Hix-U7Um02KEXCCV5VJXbQ9FmakKufJ0RZCWVlyayhiP5Y3EcmY2EH-5UTVzCnA2ptxZAssN5RshmIKNuAEebxhtGjZx1hZP-EmgXG8KZd6z1LgugLRHKsEGO-t3GJBrPJvFyhtPxiZF0pL2Yq9IiCM2lCsEIBKe6pYsCB~Zopbx79UrhIhrPP9dxg0729tSrBSF6z-4BmAkzw03kiYkmHyYbL2tsIFnVX6HqHk4rp5p0P8eGj~BJ-oNTDhHxon0UCsNy9eNKfbzWVqm6cB1TP4DUqW8XRKmJnDxfQ__%22%7D)) 

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Hazzanzz/Fake_news_Detector.git
cd Fake_news_Detector

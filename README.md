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

![Fake News Detector UI](https://cdn.corenexis.com/view/?img=mm/ap20/Kx52yv.png). 

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Hazzanzz/Fake_news_Detector.git
cd Fake_news_Detector


# 🤖 Clarifai DeepSeek Chatbot

A lightweight and powerful chatbot built using [Clarifai's gRPC API](https://www.clarifai.com/) and the **DeepSeek-AI** model. This project leverages **Streamlit** for a fast and interactive web UI, enabling seamless real-time conversations with an advanced LLM served via Clarifai.

---

## 🚀 Features

- 🔥 Integrates **DeepSeek-AI** via Clarifai's gRPC API  
- 💬 Real-time chat interface built with **Streamlit**  
- 🔐 Secure with personal access token (PAT) authentication  
- 🧠 Easily adaptable to any Clarifai-hosted model  
- ♻️ One-click **Clear Chat** to reset conversations

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/clarifai-deepseek-chatbot.git
cd clarifai-deepseek-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your credentials

Edit the script and replace placeholders with your actual Clarifai credentials:

```python
PAT = 'your_pat_id_here'
USER_ID = 'deepseek-ai'
APP_ID = 'deepseek-chat'
MODEL_ID = 'your_model_id_here'
MODEL_VERSION_ID = 'your_model_version_id_here'
```

---

## 💡 How to Use

```bash
streamlit run chatbot.py
```

Then visit `http://localhost:8501` in your browser. Type a message and start chatting!

---

## 📦 Tech Stack

- **Python**
- **Clarifai gRPC API**
- **Streamlit**
- **DeepSeek-AI**

---

## 🤯 Future Ideas

- Support voice input/output  
- Add memory for multi-turn context  
- Plug-in multiple models dynamically  
- Analytics dashboard for conversation insights

---

## 📄 License

MIT License — feel free to fork, modify, and build on it.

---

## 👋 Let's Connect

If you find this useful or have any cool ideas to collaborate on, reach out or star ⭐ the repo!

---

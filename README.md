# 📞 Calling Agent AI Project

This project is an **AI-powered outbound calling agent** that automatically places phone calls to customers using the [Vapi AI API](https://vapi.ai/).  
It reads customer phone numbers (and names) from a CSV file and makes automated calls through a virtual assistant. 

---

## 🚀 Features
- ✅ Reads phone numbers and names from a CSV file (`demo.csv`)
- ✅ Cleans and formats numbers automatically (adds +91 if missing)
- ✅ Uses [Vapi AI](https://vapi.ai/) API for outbound calls
- ✅ Customizable **Assistant ID** and **Phone Number ID** from twilio
- ✅ 2-second delay between calls to avoid spamming
- ✅ Easy to extend and integrate with other CRM systems

---

## 🛠️ Tech Stack
- **Python**
- **Requests library** for API calls
- **CSV module** for reading data
- **Twilio** for phone number
- **Vapi AI API** for making phone calls

---

## 📂 Project Structure
### 📦 calling-agent-ai

📜 demo.csv - CSV file with phone numbers & names

📜 main.py - Main Python script

📜 README.md - Project documentation

## 📋 Prerequisites
pip install requests

## 🔑 Configuration

### Open main.py and update the following variables with your credentials:

API_KEY = "your-api-key-here"

ASSISTANT_ID = "your-assistant-id-here"

PHONE_NUMBER_ID = "your-phone-number-id-here"

## ▶️ Usage

Run the script in your terminal:

#### python main.py

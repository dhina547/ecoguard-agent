# 🌱 EcoGuard Agent  
## A Multi-Agent AI System for Sustainable Crop Disease Detection and Decision Support

EcoGuard Agent is a **multi-agent AI system** designed to assist farmers with **early plant disease detection**, **climate-aware risk analysis**, and **eco-friendly treatment recommendations**.

This project was developed as part of the **Agents Intensive Capstone Project** and demonstrates how **agent-based architectures** can solve real-world sustainability challenges in agriculture.

---

## 🚜 Problem Statement

Plant diseases and climate variability significantly affect agricultural productivity.  
Farmers often face difficulties in:

- Identifying crop diseases at an early stage  
- Understanding how temperature and humidity influence disease spread  
- Choosing sustainable treatment options instead of excessive chemical usage  

Delayed diagnosis and uninformed treatment decisions result in crop loss and environmental harm.

---

## 🧠 Why Agents?

This problem involves **multiple reasoning steps** that are best handled by **specialized AI agents** rather than a single monolithic model.

EcoGuard uses agents to:
- Separate perception (vision) from reasoning (climate + treatment)
- Improve clarity and interpretability of decisions
- Enable scalable and modular system design
- Demonstrate real-world agent orchestration

---

## 🧠 Solution Overview

EcoGuard follows a **sequential multi-agent pipeline**, where each agent performs a focused task and passes structured outputs to the next agent.

### 🔄 Agent Pipeline
1. Vision Disease Agent (Gemini Vision)
2. Climate Risk Agent (Rule-based)
3. Sustainability Recommendation Agent (Gemini)
4. Memory Agent
5. Orchestration Layer

---

## 🏗 System Architecture

![EcoGuard System Architecture](architecture/ecoguard_architecture.png)

---

## ⚙️ Agent Descriptions

### 🟢 Vision Disease Agent
- Uses **Gemini Vision**
- Analyzes plant leaf images
- Outputs:
  - Disease status
  - Disease name
  - Confidence score
  - Visual symptoms

---

### 🌦 Climate Risk Agent
- Evaluates temperature and humidity
- Identifies climate-driven disease risks
- Uses interpretable rule-based logic

---

### 🌱 Sustainability Recommendation Agent
- Powered by **Gemini**
- Generates eco-friendly treatment guidance
- Avoids harmful chemical overuse

---

### 🧠 Memory Agent
- Maintains recent disease analyses
- Enables session continuity and traceability

---

## ▶️ Demo

### ✅ Input
- **Leaf Image:** Plant leaf with visible disease symptoms  
- **Climate Data:**  
  - Temperature: 29°C  
  - Humidity: 78%

### ✅ Output
- Disease Detection: *Leaf Spot*
- Climate Risk: High humidity accelerates disease spread
- Sustainable Recommendations:
  - Copper-based fungicides
  - Improved airflow
  - Avoid overhead irrigation

### 📓 Kaggle Notebook Demo
🔗 *(https://www.kaggle.com/code/dhinagar547/ecoguard-agent-sustainable-agriculture-final)*

---

## 🧪 Features Demonstrated

- ✅ Multi-agent system
- ✅ LLM-powered agents (Gemini)
- ✅ Sequential agent orchestration
- ✅ Context engineering
- ✅ Session memory
- ✅ Sustainability-focused AI application

---

## 🛠 Installation & Setup

```bash
git clone https://github.com/dhina547/ecoguard-agent.git
cd ecoguard-agent
pip install -r requirements.txt

# Tentative bol.com E-commerce-chatbot-assistant
# Project Overview

The project aims to develop and deploy an AI-powered chatbot to enhance the user experience for Bol's e-commerce platform. The chatbot will assist users with frequently asked questions (FAQs) and product inquiries, driving engagement and customer satisfaction.

## Chatbot development in Streamlit
Objective: Build a chatbot in Streamlit with core functionalities for FAQs and product inquiries.
Deliverables:
1. FAQ Data Ingestion into Chromadb – Efficient ingestion and vectorization of frequently asked questions into the Chromadb vector database.
2. Streamlit Chatbot Frontend – Develop an interactive and user-friendly chatbot interface using Streamlit.
3. Route Support:
- FAQs – The chatbot must retrieve answers from the FAQ database.
- Product Inquiries – Product and pricing information will be pulled from an SQLite database.
Tech Stack:
- Language Model: LLama3.3 LLM - Frontend: Streamlit
- Database: Chromadb (vector database) and SQLite (product and pricing storage) - Routing: Semantic router

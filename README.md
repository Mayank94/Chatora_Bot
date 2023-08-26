# Chatore_bot
 ChatBot for Food Outlet

 ## NLP based Chatbot with Dialogflow, FastAPI, and MySQL

## Overview

This project demonstrates the implementation of an NLP-based chatbot using Dialogflow, FastAPI, and MySQL. The chatbot is designed to handle user interactions, process natural language, and provide responses based on predefined intents and user input. The backend is built using FastAPI, while MySQL is used to store and retrieve relevant data.

## Features

- Utilizes Dialogflow for NLP capabilities and intent recognition.
- FastAPI serves as the backend to handle incoming webhook requests and communicate with the chatbot.
- MySQL is used to store and manage data related to user orders, interactions, etc.
- Implements various chatbot actions like adding items to orders, tracking orders, etc.
- Supports both text-based through Dialogflow.
- Provides robust error handling and user-friendly responses.

## Getting Started

### Directory structure

Backend: Contains Python FastAPI backend code
db: contains the dump of the database. you need to import this into your MySQL db by using MySQL workbench tool
dialogflow_assets: this has training phrases etc. for our intents
frontend: website code

### Install these modules
pip install mysql-connector
pip install "fastapi[all]"

OR just run pip install -r backend/requirements.txt to install both in one shot


### Running the Backend

#### To start fastapi backend server

1. Go to backend directory in your command prompt
2. Run this command: uvicorn main:app --reload

#### ngrok for https tunneling

1. To install ngrok, go to https://ngrok.com/download and install ngrok version that is suitable for your OS
2. Extract the zip file and place ngrok.exe in a folder.
3. Open windows command prompt, go to that folder and run this command: ngrok http 8000

NOTE: ngrok can timeout. you need to restart the session if you see session expired message.

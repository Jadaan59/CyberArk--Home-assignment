# 🧠 Work Process Report

## 1. 📖 Reading the Assignment and Choosing a Model
I started by carefully reading the assignment. The first step was to decide which model to use. After reviewing the suggestions, I realized that the phi4 model was not suitable for my hardware. Therefore, I decided to use gemma3, and after checking several versions, I chose gemma3:4b, which fit my requirements in terms of size and resources.

## 2. 🐍 Choosing the Programming Language
I chose Python because it is well-suited for working with LLMs. I discovered that there is a Python module that allows sending requests directly to the Ollama server, which made communication with the model much easier.

## 3. ⬇️ Installing the Model and Initial Run
I researched how to download the model locally using Ollama, installed it, and ran it locally to understand how it works. Then, I built the main Python script to interact with the model.

## 4. ✂️ Splitting the Code File for Analysis
During development, I noticed that analyzing large files all at once was problematic. I considered splitting by code blocks, but realized that a block could be too large. Therefore, I decided to split the file by a fixed number of lines to better control the size of each chunk sent for analysis.

## 5. 🐳 First Attempt with Docker
I tried to run everything in Docker right away, even though I didn't have much experience with it. I encountered many difficulties and issues, and at first, I couldn't figure out the cause. At this stage, I continued working without Docker.

## 6. 🕵️ Solving the Docker Port Issue
After further investigation, I realized the problem was with the port configuration in Docker—the container was not listening on the correct port, so the script didn't work. I reached out to friends who are more experienced with Docker, got some tips, and learned about Docker Compose. After correctly configuring the port and using Docker Compose, everything worked as expected.

## 7. ✅ Completion and Submission
After making sure everything worked—both locally and in Docker—I finished development and prepared the project for submission.
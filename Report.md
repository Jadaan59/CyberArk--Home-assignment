# 🧠 Work Process Report
## 1. 📖 Understanding the Task
Two days ago, I received a task. I started by reading it carefully to understand the requirements. The first thing I noticed: I needed to download a language model.
## 2. 🔍 Exploring Options
I explored different tools and came across Ollama, which seemed like a great way to download and run language models locally. That led me to the next decision.
## 3. 🐍 Choosing Python
Since the task involved analyzing documents and scripts—and I needed to interact with the Ollama server—I decided to use Python. It's perfect for scripting and flexible enough for server communication.
## 4. 🧠 Picking the Right Model
At first, I considered using Microsoft's phi-4 model, as the task suggested. But after a bit of research, I realized it was too heavy for my setup and would likely slow down development. Instead, I went with gemma3:4b. It’s smaller, lighter, and runs locally without needing a dedicated GPU — perfect for quick iteration and offline usage. It still provides strong results and seemed like the right balance between performance and practicality.
## 5. 🛠 Prompting for Fixes
While designing the prompt sent to the model, I made sure to not only ask for vulnerability detection but also to suggest possible fixes. That way, the tool doesn't just identify problems — it helps solve them too. This made the output more actionable and developer-friendly.
## 6. 🐳 First Try with Docker
I tried running everything inside a Docker container from the start. But... I hit a wall. As someone not too familiar with Docker, I ran into lots of small (and frustrating) problems, mainly that the python script was not triggered.  
## 7. 🔄 Changing Strategy
After a few hours of struggling, I pivoted. I set up a Python virtual environment, installed all the dependencies there, and ran the code outside of Docker. It worked!
## 8. ✂️ Handling Limitations
The Ollama server had some limitations. To deal with that, I wrote logic to split the input (chunking) into smaller parts. This made processing more efficient and customizable depending on the model and the hardware.
## 9. ✅ Initial Success
Once the virtual environment setup was working, I shared the tool with a few friends—it worked for them too. That gave me the green light to continue.
## 10. 🧪 Planning for Docker + Automation
With a working version ready, I turned my focus back to Docker, planning to integrate it later with some automation.
## 11. 🧩 Final Touches 
I built a precise process for chunking and analysis to ensure performance and reliability. It also prevented the model from consuming too much time or memory.
## 12. 🚀 Ready for Submission
With everything tested and working smoothly, I finalized the code and got it ready for submission. Mission accomplished!
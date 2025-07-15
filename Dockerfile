FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && apt-get install -y \
    python3.12 \
    python3.12-venv \
    curl \
    wget \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12


WORKDIR /app
COPY data /app

RUN pip install -r deps/requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama in background, wait until it's ready, then pull the model
RUN nohup ollama serve > /tmp/ollama.log 2>&1 & \
    sleep 10 && \
    ollama pull gemma3:4b && \
    pkill ollama

# Expose default Ollama port
EXPOSE 11434:11434
ENV OLLAMA_HOST=0.0.0.0:11434

# Default command
CMD ["ollama", "serve"]
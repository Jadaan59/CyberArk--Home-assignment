# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
RUN pip install --no-cache-dir ollama

# Install curl (needed for Ollama install)
RUN apt-get update && apt-get install -y curl gnupg && apt-get clean

# Download and install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Expose port for Ollama server
EXPOSE 11434

# Run Ollama in background and analyzer.py (entrypoint can be changed)
CMD ["bash"]

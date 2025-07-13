# Dockerfile

# בסיס: אובונטו 22.04
FROM ubuntu:22.04

# התקנת כלים חיוניים
RUN apt update && apt install -y \
    git \
    build-essential \
    cmake \
    curl \
    unzip \
    ninja-build \
    libcurl4-openssl-dev

# הורדת llama.cpp והתקנת llama-cli
RUN git clone https://github.com/ggerganov/llama.cpp /llama.cpp && \
    cd /llama.cpp && mkdir build && cd build && \
    cmake .. -DLLAMA_BUILD_EXAMPLES=OFF -DLLAMA_BUILD_TESTS=OFF -G Ninja && \
    ninja && \
    ln -s /llama.cpp/build/bin/llama-cli /usr/local/bin/llama-cli

# הגדרת ספריית העבודה
WORKDIR /app

# העתקת המודל, הסקריפט, ודוגמת קובץ C
COPY model/ model/
COPY src/ src/
COPY library.c .

# קובץ שמריץ את הכלי כברירת מחדל
ENTRYPOINT ["bash", "src/analyzer.sh"]


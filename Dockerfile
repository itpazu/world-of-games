FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome browser
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable
WORKDIR /app
COPY ./e2e ./e2e
COPY main_score.py .
COPY requirements.txt .
COPY Score.txt .
COPY score.py .
COPY utils.py .
COPY ./static ./static
COPY ./templates ./templates
RUN pip install -r requirements.txt
CMD ["python3", "./main_score.py"]
EXPOSE 5000
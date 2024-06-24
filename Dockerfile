FROM python:3.9-slim

# Install necessary packages and Chrome with verbose output
RUN apt-get update -y -v && apt-get install -y -v \
    wget \
    gnupg \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*
# Add Google Chrome's signing key and repository
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome with verbose output
RUN apt-get update -y -v && apt-get install -y -v google-chrome-stable
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
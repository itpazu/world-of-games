FROM python:3-alpine
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
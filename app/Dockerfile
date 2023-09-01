FROM python:3.10.6-slim
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
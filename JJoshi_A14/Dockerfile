# Start with a base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files from the host to the container
COPY . /app

# Install dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Specify the command to run the app when the container starts
CMD ["python", "app.py"]

FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

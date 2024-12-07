# Start with a base image that includes Python 3.8
FROM python:3.8-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all the files from the current directory (where Dockerfile is) to /app inside the container
COPY . /app

# Install the dependencies listed in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the app (assuming the entry point is app.py)
CMD ["python", "app.py"]


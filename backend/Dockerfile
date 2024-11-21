# Use the official Python image from the Docker Hub
FROM python:3.8.0-slim

# Set the working directory in the container
WORKDIR /app
COPY . /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

CMD ["python", "./src/app.py"]
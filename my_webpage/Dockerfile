# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Run the command to install any necessary dependencies
RUN pip install  flask psycopg2-binary

# Copy the current directory contents into the container at /app
COPY . /app

# Run hello.py when the container launches
CMD ["python", "app.py"]

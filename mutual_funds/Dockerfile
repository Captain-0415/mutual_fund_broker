# Use the official Python image as a base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app/mutual_funds/app

# Copy the requirements file to the container
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the FastAPI app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["ls"]
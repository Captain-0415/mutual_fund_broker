# Use the official Python image as a base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /mutual_fund

# Copy the requirements file to the container
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the FastAPI app runs on
EXPOSE 8000

ENV PYTHONUNBUFFERED=1

WORKDIR /mutual_fund/app


# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
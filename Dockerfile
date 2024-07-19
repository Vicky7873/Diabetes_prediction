# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install build tools and HDF5 dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 8888 available to the world outside this container
EXPOSE 8999
COPY src/ /app/src
COPY saved_models/ /app/saved_models

RUN mkdir -p /app/saved_models
COPY saved_models/xgb_model.pkl /app/saved_models/xgb_model.pkl

# Set PYTHONPATH to include src folder
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# AWS 

# Run app.py when the container launches
CMD ["python", "app.py"]

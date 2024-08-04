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

# Install DVC
RUN pip install dvc

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY src/ /app/src
COPY saved_models/ /app/saved_models
COPY .dvc /app/.dvc  

COPY app.py /app/app.py

# Make port 8999 available to the world outside this container
EXPOSE 8080

# Set PYTHONPATH to include src folder
ENV PYTHONPATH="/app/src"

# Pull DVC models
RUN dvc pull -v

# Run app.py when the container launches
CMD ["python", "app.py"]



### new docker 
# FROM python:3.8.5-slim-buster

# WORKDIR /app

# COPY . /app

# RUN pip install -r requirements.txt

# EXPOSE 8080

# CMD ["python3", "app.py"]
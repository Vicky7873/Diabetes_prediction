# # Use an official Python runtime as a parent image
# FROM python:3.12-slim

# # Set the working directory in the container
# WORKDIR /app

# # Install build tools and HDF5 dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     pkg-config \
#     libhdf5-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN python -m pip install --no-cache-dir -r requirements.txt

# # Copy the application code into the container
# COPY src/ /app/src
# COPY saved_models/ /app/saved_models
# COPY app.py /app/app.py

# # Make port 8999 available to the world outside this container
# EXPOSE 8999

# # Set PYTHONPATH to include src folder
# ENV PYTHONPATH="/app/src"

# # Run app.py when the container launches
# CMD ["python", "app.py"]


### new docker 
FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8999

CMD ["python3", "app.py"]
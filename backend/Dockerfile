# Use an official Python runtime as a parent image
FROM python:3.10.12-slim


# Set the working directory in the container
WORKDIR /usr/src/app/backend

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Ensure pip is up-to-date
RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y libglib2.0-0
# Copy the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .


EXPOSE 8000  

# Run the Django server
CMD ["python", "simplifai/manage.py", "runserver", "0.0.0.0:8000"]

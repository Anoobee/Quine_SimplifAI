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

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Install additional Python packages
# RUN pip install Django==5.0.6
# RUN pip install djangorestframework==3.15.2
# RUN pip install django-cors-headers
# RUN pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
# RUN pip install langchain_community
# RUN pip install paddleocr
# RUN pip install transformers

# Run the Django server
CMD ["python", "simplifai/manage.py", "runserver", "0.0.0.0:8000"]

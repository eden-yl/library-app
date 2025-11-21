# Use an official lightweight Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the dependencies file into the container
COPY requirements.txt ./

# Install Python dependencies. --no-cache-dir saves space.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port Gunicorn will listen on
EXPOSE 8000

# Command to run the application using Gunicorn when the container starts
# We use port 8000 here, which is standard for containerized apps.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
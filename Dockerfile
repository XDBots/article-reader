# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the container
COPY bot.py scraper.py url_validator.py .

# Run the Python script when the container launches
CMD ["python", "bot.py"]


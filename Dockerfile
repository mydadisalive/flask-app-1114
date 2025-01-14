FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 inside the container
EXPOSE 5000

# Default CMD
CMD ["python", "./app.py"]

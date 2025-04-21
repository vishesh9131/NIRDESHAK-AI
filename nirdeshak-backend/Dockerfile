# Step 1: Use a minimal Python image
FROM python:3.10-slim

# Step 2: Set environment variables to prevent Python from writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set working directory inside the container
WORKDIR /app

# Step 4: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy project files into the container
COPY . .

# Step 7: Expose Flask port
EXPOSE 5000

# Step 8: Start Flask app
CMD ["python", "app.py"]
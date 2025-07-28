# 1. Use a base Python image
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy everything else into the container
COPY . .

# 5. Set the default command
CMD ["python", "app/main.py"]

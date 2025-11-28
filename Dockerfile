# Use official python
FROM python:3.10

# Create working dir
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 7860

# Run fastapi server
CMD ["uvicorn", "api.index:app", "--host", "0.0.0.0", "--port", "7860"]

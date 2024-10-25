FROM python:3.10

# Set a working directory
WORKDIR /code

# Copy requirements first to leverage Docker cache when dependencies don’t change
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Set entrypoint and command for running the server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

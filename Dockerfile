FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port 5000
EXPOSE 5000

# # Copy the entrypoint script
# COPY entrypoint.sh /usr/local/bin/
# RUN chmod +x /usr/local/bin/entrypoint.sh

# # Command to run the application
# CMD ["entrypoint.sh"]
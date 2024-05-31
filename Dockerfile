FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/djangobnb_backend

# Install netcat
RUN apt-get update && apt-get install -y netcat

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Copy requirements file and install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint script and set permissions
COPY ./entrypoint.sh /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh

# Copy the entire project directory
COPY . .

# Set the entrypoint command
ENTRYPOINT [ "/usr/src/entrypoint.sh" ]

# Pull Python image
FROM python:3

# Install pillow globally.
ENV LIBRARY_PATH=/lib:/usr/lib

# Directory to put code in app folder
WORKDIR /app

# add everything to app folder
ADD . /app

# Add requirements.txt before rest of repo for caching.
COPY ./requirements.txt /app/requirements.txt

# Install project dependencies before copying the rest of the codebase.
RUN pip install -r requirements.txt

# Copy this directory to the image.
COPY . /app

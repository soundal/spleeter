# Use the official Python image as a parent image
FROM python:3.8-slim

# Set the working directory in the container to / (root)
WORKDIR /

# Copy the dependencies file to the working directory
COPY pyproject.toml poetry.lock* /

# Install any dependencies
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Copy the content of the local src directory to the working directory
COPY . /


# Specify the command to run on container start
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
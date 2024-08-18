ARG PORT=443
FROM cypress/included:latest

# Ensure system is up to date and install Python and pip
RUN apt-get update && apt-get install -y python3-pip

# Print the user base directory for Python packages (just for verification)
RUN echo $(python3 -m site --user-base)

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set the PATH environment variable to include the user base's binary directory
ENV PATH /root/.local/bin:${PATH}

# Copy the application code
COPY . .

# Run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]

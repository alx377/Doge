

# Use an official Python runtime as a parent image
FROM python:3.7

# ffmpeg
RUN apt-get update
RUN apt-get install ffmpeg -y
RUN apt-get install frei0r-plugins -y

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip install -r requirements.txt

# RUN apt-get install -y supervisor
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# CMD ["/usr/bin/supervisord"]

# Run app.py when the container launches
# CMD ["python", "doge.py"]
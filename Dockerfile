FROM ubuntu:18.04

RUN apt-get update && apt-get install -y nginx vim   git python3   python3-pip  curl 
RUN  pip3 install requests flask 

# Set the working directory
WORKDIR   /var/www/appjohn/

# Copy the repository contents into the container
COPY . /var/www/appjohn/

EXPOSE  5000
CMD ["python3", "app.py"]

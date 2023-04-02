# init a base image (Alpine is small Linux distro)
#FROM python:3.9-alpine
FROM python:3

#  MUST Install Python 3 && upgrade pip
# RUN apk add --no-cache python3   && pip install --upgrade pip
RUN pip install --upgrade pip

# define the present working directory
WORKDIR /hr_system

# copy the contents of current folder "." into the working dir of the docker image
ADD . /hr_system

# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# define the command to start the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
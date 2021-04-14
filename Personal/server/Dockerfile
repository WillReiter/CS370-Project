# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY ./requirements.txt .

COPY ./scraper.py .

COPY ./info.txt .

# install dependencies
RUN pip install -r ./requirements.txt

RUN python3 ./scraper.py


# copy the content of the local src directory to the working directory
COPY ./app/ .

# command to run on container start
CMD [ "python3", "./server.py", "--host=0.0.0.0" ]

# Run SNAB as Docker container
# docker run -dit --name snab-container -v $(pwd)/settings.cfg:/opt/snab/settings.cfg -p 8080:8080 snab

FROM python:3.8-slim-buster
MAINTAINER Artur Nebot
RUN apt-get update -y

COPY ./requirements.txt /opt/snab/requirements.txt
COPY ./settings.example.cfg /opt/snab/settings.cfg

WORKDIR /opt/
RUN pip3 install -r snab/requirements.txt
RUN pip3 install waitress

COPY ./snab /opt/snab

ENV SNAB_SETTINGS=/opt/snab/settings.cfg

ENTRYPOINT ["waitress-serve","--call","snab.factory:create_app"]

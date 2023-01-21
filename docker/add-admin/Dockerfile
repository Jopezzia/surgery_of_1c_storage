FROM python:slim-bullseye
WORKDIR /tmp
RUN apt-get update
RUN apt-get install curl -y
RUN curl -L https://github.com/Jopezzia/surgery_of_1c_storage/releases/download/v1.0/surgery_of_1c_storage.tar.gz --output surgery_of_1c_storage.tar.gz
RUN tar -xvf surgery_of_1c_storage.tar.gz
RUN mv surgery_of_1c_storage /opt
RUN apt-get update
WORKDIR /opt/surgery_of_1c_storage
ENTRYPOINT [ "./starter init-config -n config.ini && ./starter add-admin" ]
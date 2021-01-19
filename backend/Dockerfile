FROM python:3.8.7-buster

ARG USERNAME=python
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME 

COPY ./app/requirements.txt /src/
WORKDIR /src
RUN pip install -r requirements.txt

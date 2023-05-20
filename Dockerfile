FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN pip install -r requirements.txt

#add Your bot token here -
ENV BOT_TOKEN=ENTER_YOUR_BOT_TOKEN__

#optional - 
ENV HTTP_PROXY=None
ENV HTTPS_PROXY=None

COPY . /usr/app/src
CMD python3 bot.py
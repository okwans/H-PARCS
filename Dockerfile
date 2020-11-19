FROM ubuntu:bionic

RUN apt-get update --fix-missing
RUN apt-get install -y vim

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb

RUN apt-get install -y libgbm1
#RUN pip3 install scikit-build
#RUN pip3 install cmake
#RUN pip3 install numpy
#RUN pip3 install opencv-python

# install chromedriver and google-chrome
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

RUN CHROME_SETUP=google-chrome.deb && \
    wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP && \
    apt-get install -y -f && \
    rm $CHROME_SETUP

RUN pip3 install selenium
RUN pip3 install pyvirtualdisplay
RUN pip3 install behave
RUN pip3 install requests
RUN pip3 install Appium-Python-Client

RUN pip3 install beautifulsoup4
RUN pip3 install jsonpath

RUN apt-get update && apt-get install -y python2.7
RUN apt-get install -y python-pip

RUN pip2 install behave2cucumber

RUN curl -sL http://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs
RUN npm install cucumber-html-reporter

RUN apt-get install -y ssh

#
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN apt-get install -y tzdata
#

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

ENV RUN_TIME_ENV=staging
#ENV REMOTE_STATION_IP=59.12.187.40
ENV REMOTE_STATION_IP=220.117.186.216
# Test Category
ENV TEST_CATEGORY=API

WORKDIR /root
USER $ID_NAME


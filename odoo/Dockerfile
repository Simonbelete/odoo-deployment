FROM ubuntu:20.04

## How many CPUs do you have?
RUN grep -c ^processor /proc/cpuinfo

## Scritp Helpers
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt install -y python3.8

RUN apt install -y git-all

RUN apt install -y python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
    libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev

RUN apt install -y wget && \
    wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb && \
    apt install -y ./wkhtmltox_0.12.6-1.focal_amd64.deb

RUN cd /home && \
    git clone https://github.com/odoo/odoo.git --depth 1 -b 15.0

RUN pip3 install setuptools wheel && \
    pip3 install -r requirements.txt
#!/bin/sh

## Install ubuntu common software properties
# apt-get update && \
#     apt-get install -y software-properties-common && \
#     rm -rf /var/lib/apt/lists/*

## Install Python >= 3.7 and venv
# add-apt-repository ppa:deadsnakes/ppa && \
#     apt update && \
#     apt install -y python3.8
    
## Install git
# apt install -y git-all

## Install and setup PostgreSQL
#apt install -y postgresql postgresql-client && \
systemctl status psql
postgres createuser -s odoo15_user && \
    createdb odoo15_user

## Install Dependencies
# apt install -Y python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
#     libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
#     liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev

## Install Wkhtmltopdf = 0.12.5
# apt install -y wget && \
#     wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb && \
#     apt install -y ./wkhtmltox_0.12.6-1.focal_amd64.deb

## Clone odoo
# cd /home && \
#     git clone https://github.com/odoo/odoo.git --depth 1 -b 15.0

## Setup venv and Install odoo requirements
cd /home/odoo && \
    python3 -m venv venv && \
    source venv/bin/activate && \
    pip3 install setuptools wheel && \
    pip3 install -r requirements.txt && \
    deactivate

## Custom Modules
cd /home/odoo && \
    mkdir -p custom_modules

## Setup Systemd Unit File
# odoo.service /etc/systemd/system/odoo.service
systemctl daemon-reload && \
    systemctl start odoo && \
    systemctl enable odoo && \
    systemctl status odoo
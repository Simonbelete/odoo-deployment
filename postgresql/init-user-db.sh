#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER odoo15_user;
    CREATE DATABASE odoo15_db;
    GRANT ALL PRIVILEGES ON DATABASE odoo15_db TO odoo15_user;
EOSQL
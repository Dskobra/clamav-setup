#! /usr/bin/bash

# This script setups clamav "service user account" 
# as per the official docs.
# https://docs.clamav.net/manual/Installing/Add-clamav-user.html

# create the clamav group
sudo groupadd clamav

# create hidden clamav account for running as a service
sudo useradd -g clamav -s /bin/false -c "Clam Antivirus" clamav


# Assign the service account as owner of the database
# folder
sudo chown -R clamav:clamav /usr/local/share/clamav

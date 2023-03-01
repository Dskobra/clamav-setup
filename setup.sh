#! /usr/bin/bash

menu(){
    echo "================================================"
    echo "Menu"
    echo "1. Install clamav 2. Setup Clamav User Account"
    echo "3. Create config files"
    echo "0. Exit"
    echo "================================================"
    printf "Option: "
    read input
    
    if [ $input -eq 1 ]
    then
        sudo dnf remove -y clamav*
        wget https://www.clamav.net/downloads/production/clamav-1.0.1.linux.x86_64.rpm
        sudo rpm -i clamav*.rpm
        rm clamav*.rpm
    elif [ $input -eq 2 ]
    then
        # This script setups clamav "service user account" 
        # as per the official docs.
        # https://docs.clamav.net/manual/Installing/Add-clamav-user.html

        # create the clamav group
        sudo groupadd clamav

        # create hidden clamav account for running as a service
        sudo useradd -g clamav -s /bin/false -c "Clam Antivirus" clamav


        # Assign the service account as owner of the database
        # folder
        sudo mkdir /usr/local/share/clamav
        sudo chown -R clamav:clamav /usr/local/share/clamav
    elif [ $input -eq 3 ]
    then
        sudo python config-tool.py
    elif [ $input -eq 0 ]
    then
	    exit
    else
	    echo "error."
    fi
    menu
}
menu
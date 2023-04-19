#! /usr/bin/bash

menu(){
    echo "================================================"
    echo "Uninstall ClamAV Script"
    echo "This will remove clamav from your system,"
    echo "clamav system account, databases"
    echo "and configuration files"
    echo "Type y/n or exit"
    echo "================================================"
    printf "Option: "
    read input
    
    if [ $input == "y" ] || [ $input == "Y" ]
    then
        sudo killall -u clamav
        sudo dnf remove -y clamav*
        sudo rm -r /usr/local/share/clamav

        sudo rm /usr/local/etc/clamd.conf
        sudo rm /usr/local/etc/freshclam.conf

        sudo rm /usr/local/etc/clamd.conf.sample
        sudo rm /usr/local/etc/freshclam.conf.sample
        sudo userdel -r clamav
    elif [ $input == "n" ] || [ $input == "N" ]
    then
        echo "Chose not to remove."
    elif [ $input == "exit" ]
    then
	    exit
    else
	    menu
    fi
}
menu

#!/bin/bash

function check_if_application_is_running { 

    netstat -ntpl | grep [0-9]:${1:-8000} -q ; 

    if [ $? -eq 1 ]
    then 
        python manage.py runserver 0.0.0.0:8000
    else 
        echo "Application is running"
    fi
}


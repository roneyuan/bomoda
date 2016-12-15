#!/bin/bash
echo "Installing Python..."
sudo apt-get install python2.7.10
sudo apt-get install python-pip
echo "Installing Django..."
pip install Django
echo "Installing all dependencies and libraries"
echo "Installing REST Framework..."
pip install djangorestframework
pip install markdown 
pip install django-filter
echo "Installing the rest of dependencies..."
pip install datetime
pip install os.path
pip install atexit
pip install json

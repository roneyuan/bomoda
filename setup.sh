#!/bin/bash

# Install Python-2.7.10
mkdir -p ~/local
wget http://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
tar xvzf Python-2.7.10.tgz
cd Python-2.7.10
./configure
make
make altinstall prefix=~/local
ln -s ~/local/bin/python2.7.10 ~/local/bin/python
cd ..

# Install setuptools
wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz#md5=7df2a529a074f613b509fb44feefe74e
tar xvzf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
~/local/bin/python setup.py install

# Install pip 
cd ..
wget https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz#md5=35f01da33009719497f01a4ba69d63c9
tar xvzf pip-9.0.1.tar.gz
cd pip-9.0.1
~/local/bin/python setup.py install

# Install Django
~/local/bin/pip install django

# Install all dependencies
~/local/bin/pip install djangorestframework
~/local/bin/pip install markdown 
~/local/bin/pip install django-filter
~/local/bin/pip install datetime
~/local/bin/pip install os.path
~/local/bin/pip install atexit
~/local/bin/pip install json

#!/bin/bash
#Скрипт установщик tf 2.3 для решений на базе jetson nano, так же работает на Ubuntu 20.04

# sudo apt-get install python-pip python3-pip
# # remove old versions, if not placed in a virtual environment (let pip search for them)
# sudo pip uninstall tensorflow
# sudo pip3 uninstall tensorflow

#Если нет python 3.6 на PC
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt-get update
# sudo apt-get install python3.6
# sudo apt-get install python3-virtualenv
# virtualenv -p /usr/bin/python3.6 env

# install the dependencies (if not already onboard)
sudo apt-get install -y gfortran
sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev
sudo apt-get install -y libatlas-base-dev libopenblas-dev libblas-dev
sudo apt-get install -y liblapack-dev


env/bin/pip3 install -U testresources numpy
# upgrade setuptools 39.0.1 -> 50.3.2
env/bin/pip3 install --upgrade setuptools
env/bin/pip3 install pybind11 protobuf google-pasta
env/bin/pip3 install -U six mock wheel requests gast
env/bin/pip3 install Cython==0.29.21
# install h5py with Cython version 0.29.21 (± 6 min @1950 MHz)
env/bin/pip3 install h5py==2.10.0
env/bin/pip3 install keras_applications --no-deps
env/bin/pip3 install keras_preprocessing --no-deps
# install gdown to download from Google drive
env/bin/pip3 install gdown
# download the wheel
# gdown https://drive.google.com/uc?id=1oeSnkgJpwyudtTx-f5CE84B7e-Vkv3yK
# если не работает gdown в командной строке то python3 gettf.py 
# install TensorFlow (± 12 min @1500 MHz)
# env/bin/pip3 install tensorflow-2.3.1-cp36-cp36m-linux_aarch64.whl

#если на PC 
env/bin/pip3 install tensorflow==2.3.1
#objdetect
#git clone https://github.com/tensorflow/models.git
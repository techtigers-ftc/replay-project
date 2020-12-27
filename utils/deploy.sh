#!/bin/bash

if [ -z "${PORT}" ]
then
    echo "Serial port not set"
    exit 1
fi

if [ ! -z "${1}" ]
then
    echo "Deleting files from device"
    ampy -p ${PORT} rmdir magik
    ampy -p ${PORT} rm main.py 
fi

echo "Copying files to device"
ampy -p ${PORT} put ~/projects/fll/replay-project/main.py
ampy -p ${PORT} put ~/projects/fll/replay-project/magik

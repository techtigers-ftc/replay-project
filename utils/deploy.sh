#!/bin/bash

if [ -z "${PORT}" ]
then
    echo "Serial port not set"
    exit 1
fi

if [ "${1}" = "clean" ]
then
    echo "Deleting files from device"
    ampy -p ${PORT} rmdir magik
    ampy -p ${PORT} rm start.py 
    echo "Copying files to device"
    ampy -p ${PORT} put ~/projects/fll/replay-project/start.py
    ampy -p ${PORT} put ~/projects/fll/replay-project/magik
elif [ "${1}" = "lib" ]
then
    echo "Copying library to device"
    ampy -p ${PORT} put ~/projects/fll/replay-project/magik
else
    echo "Copying game program to device"
    ampy -p ${PORT} put ~/projects/fll/replay-project/start.py
    ampy -p ${PORT} put ~/projects/fll/replay-project/magik/test_game.py
fi

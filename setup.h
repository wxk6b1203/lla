#!/bin/bash

cd ./src
clang -c -fPIC MC.c
clang -shared -O2 MC.o -o mc.so
rm *.o
echo "Dynamic library compiled."
hash python3 2>/dev/null || { echo >&2 "Python3 is required but not installed. Please install in advanced."; exit 1;  }
if [[ ! -d "/usr/local/lib/python3.5/site-packages/xlrd" ]]; then
    echo -e "xlrd not installed."
    python3 -m pip install xlrd
    echo -e "^[32mOK![37m"
fi
if [[ ! -d "/usr/local/lib/python3.5/site-packages/requests" ]]; then
    echo -e "requests not installed"
    python3 -m pip install requests
    echo -e "OK!"
fi
if [[ ! -d "/usr/local/lib/python3.5/site-packages/xlwt" ]]; then
    echo -e "xlwt not installed"
    python3 -m pip install requests
    echo -e "OK!"
fi
echo -e "All dependency installed!"
cd ..


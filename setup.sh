#!/bin/bash

cd ./src
clang -c -fPIC MC.c
clang -shared -O2 MC.o -o mc.so
rm *.o
echo -e "\033[32mDynamic library compiled.\033[0m"
echo -e "\033[32m........................\033[0m"
hash python3 2>/dev/null || { echo >&2 "Python3 is required but not installed. Please install in advanced."; exit 1;  }
if [[ ! -d "/usr/local/lib/python3.5/site-packages/xlrd" ]]; then
    echo -e "\033[33;33m xlrd not installed. \033[0m"
    python3 -m pip install xlrd
    echo -e "\033[32mOK!\033[0m"
fi
if [[ ! -d "/usr/local/lib/python3.5/site-packages/requests" ]]; then
    echo -e "\033[33mrequests not installed\033[0m"
    python3 -m pip install requests
    echo -e "OK!"
fi
if [[ ! -d "/usr/local/lib/python3.5/site-packages/xlwt" ]]; then
    echo -e "\033[33mxlwt not installed\033[0m"
    python3 -m pip install xlwt
    echo -e "OK!"
fi
echo -e "\033[32mAll dependency installed! \033[0m"
cd ..


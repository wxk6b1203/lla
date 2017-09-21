# Latitude and longitude to Address

#### Introduction
LLA(Latitude and longitude to Address) is a little script convert Latitude and longitude position to address using baidu API, which uses a tool to convert ll to MC address, and then get data from Baidu. All the core logic is based on [saitjr's blog](http://www.saitjr.com/uncategorized/baidu-location-picker-interface.html) and [his repo](https://github.com/saitjr/STConvertLL2MC). The command line interface is done by myself.

It may only usable in Mainland China.

#### Usage
```
usage: main.py [-h] [-i] [-rt TXT] [-rx XLS] [-ox OX] [-ot OT] [-a]

Lati tude and longitude to Address

optional arguments:
  -h, --help          show this help message and exit
  -i, --intereactive  Interactive mode.
  -rt TXT, --txt TXT  Read from txt(see docs for format)
  -rx XLS, --xls XLS  Read from xls
  -ox OX              Write to xls
  -ot OT              Write to txt
  -a                  Appending mode(write out only)

```
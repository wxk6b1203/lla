# Latitude and longitude to Address
**developing.....**
#### Introduction
LLA(Latitude and longitude to Address) is a little script convert Latitude and longitude position to address using baidu API, which uses a tool to convert ll to MC address, and then get data from Baidu. All the injected logic is based on [saitjr's blog](http://www.saitjr.com/uncategorized/baidu-location-picker-interface.html) and [his repo](https://github.com/saitjr/STConvertLL2MC). The command line interface is done by myself.

It may only usable in Mainland China.

#### Instant method
1. Interactive mode: input a longitude and latitude, which is seperated by space, and then output a address.
2. TXT mode: input a directory of a txt file, which is formatted into particular format. Output to a file or append it to the back of each line.
	format:
	```
	longitude latitude
	123 55
	```
3. xls mode: read ll from xls, then output address. The xls should include two pure colums, which refer to longitude and latitude.
4. Both txt mode and xls mode should give param "file", or "-a" regard appending to each line.

#### Usage

##### Install dependency
Before using this script, you should install **python3.5** or later version. Then run script `setup.h`
```bash
	chmod a+x setup.sh
	./setup.sh
```
This script will compile the dynamic lib and check your dependency of python module. If it can't be used, you could install module manually, including `requests`, `json`, `xlrd`, `xlwt`.
```
python3 -m pip install MODULE
```

Then is the usage.
```
usage: python3 main.py [-h] [-i] [-rt TXT] [-rx XLS] [-ox XLSDEST] [-ot TXTDEST] [-a] [-v]

Lati tude and longitude to Address

optional arguments:
  -h, --help          show this help message and exit
  -i, --intereactive  Interactive mode. Input 'q' to quick
  -rt TXT, --txt TXT  Read from txt(see docs for format)
  -rx XLS, --xls XLS  Read from xls
  -ox XLSDEST         Write to xls
  -ot TXTDEST         Write to txt
  -a                  Appending mode(write out only)
  -v, --version       show program's version number and exit
```

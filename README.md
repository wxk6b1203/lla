# Latitude and longitude to Address
**Everything is developing.....**
### Introduction
LLA(Latitude and longitude to Address) is a little script convert Latitude and longitude position to address using baidu API, which uses a tool to convert ll to MC address, and then get data from Baidu. All the injected logic is based on [saitjr's blog](http://www.saitjr.com/uncategorized/baidu-location-picker-interface.html) and [his repo](https://github.com/saitjr/STConvertLL2MC). The command line interface is done by myself.

It may only usable in Mainland China.

### Instant method
1. Interactive mode: input a longitude and latitude, which is seperated by space, and then output a address.  
	*Notes: both space and comma are okey. Because it is parsed by regex*
	**At this moment interactive is ready to be used**  
	```
	$python3 main.py -i
	113.658023 23.098621
	广东省东莞市东莞市市辖区觉华路32
	113.658023,23.098621
	广东省东莞市东莞市市辖区觉华路32
	113.800681,23.039038
	广东省东莞市东莞市市辖区振兴路100号
	```
	You could input any other thing causing an error to quit.:(
2. TXT mode: input a directory of a txt file, which is formatted into particular format. Output to a file or append it to the back of each line.
	format:
	```
	longitude latitude
	123 55
	```
	The first line must include header, if not, it will cause an error and exit.
3. xls mode: read ll from xls, then output address. The xls should include two colums, which refer to longitude and latitude.
	format:
	```
	    (A)   	  (B)
	(1) longitude latitude
	(2) 123       55
	```
	Format is important!
4. Both txt mode and xls mode should give param "file", or "-a" regard appending to each line.

### Usage

##### Install dependency
Before using this script, you should install **python3.5** or later version. Then run script `setup.sh`
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
#### Notes
 - *xlsx is currently not supported.*
 - Three args of `-i`, `-rt` and `-ox` could be parsed with one. Otherwise, they are **relevantly exclusive**.
 - `ox`, `ot` are obay the same rule as above.
# -*- coding: utf-8 -*-
from ctypes import *
import os
import re
import json
import xlrd
import requests

"""
TODO: parse the json obj to py obj
"""


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


class MC(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]


def parseAndRequest(lon, lag):
    """parse longtitude and latitude then send request

    :lon: Longitude
    :lag: latitude
    :returns: address

    """
    # Load Library of MC convertor
    libtest = cdll.LoadLibrary(os.getcwd() + '/src/mc.so')
    libtest.convertLL2MC.restype = MC
    libtest.convertLL2MC.argtypes = (c_double, c_double)
    pos = libtest.convertLL2MC(lon, lag)
    res = {"x": pos.x, "y": pos.y, "qt": "rgc", "dis_poi": 1}
    r = requests.get('http://api.map.baidu.com/', params=res)
    resUltimateJson = json.loads(r.text, object_hook=JSONObject)

    return resUltimateJson.content.address


def interv():
    """Interactive mode for getting address
    :returns: TODO

    """
    while 1:
        getStr = input()
        lon = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',
                         getStr)[0][0]
        lag = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',
                         getStr)[1][0]
        lon = float(lon)
        lag = float(lag)
        res = parseAndRequest(lon, lag)
        print(res)


def getPos(inFormat, inFile, outFormat, outFile, append):
    """TODO: get pos of MC

    :inFormat: input format
    :inFile: input File
    :outFormat: output file
    :outFile: output file
    :append: append mode chosen
    """
    # Get the result
    res = []

    if inFormat is "txt":
        inf = open(inFile, 'rt')
        try:
            readLine = inf.readline()
            while 1:
                readLine = inf.readline()
                lon = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',
                                 readLine)[0][0]
                lag = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',
                                 readLine)[1][0]
                res.append(parseAndRequest(lon, lag))
        except Exception as e:
            inf.close()
            print("Read done.")
    elif inFormat is "xls":
        data = xlrd.open_workbook(inFile)
        table = data.sheets()[0]
        x = table.col_values(0)
        y = table.col_values(1)
        del x[0]
        del y[0]
        for item in range(0, len(x)):
            res.append(parseAndRequest(x[item], y[item]))

    if outFormat is "txt":
        if append is True:
            with open(inFile, 'w+') as outf:
                outf.readline()
                for item in range(0, len(x)):
                    line = outf.readline()
                    line = line + res[item]

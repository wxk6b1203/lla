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
    :lag: lagitude
    :returns: address

    """
    # Load library
    libtest = cdll.LoadLibrary(os.getcwd() + '/mc.so')
    libtest.convertLL2MC.restype = MC
    libtest.convertLL2MC.argtypes = (c_double, c_double)
    it = libtest.convertLL2MC(lon, lag)
    res = {"x": it.x, "y": it.y, "qt": "rgc", "dis_poi": 1}
    r = requests.get('http://api.map.baidu.com/', params=res)
    resUltimateJson = json.loads(r.text, object_hook=JSONObject)
    return resUltimateJson.content.address


def getPos(mode, target, infile, outfile):
    """TODO: get pos of MC

    :x: TODO
    :y: TODO
    :returns: TODO

    """
    res = []
    # Load Library of MC convertor
    if mode is "txt":
        inf = open(infile, 'rt')
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
            pass
    elif mode is "xls":
        data = xlrd.open_workbook(infile)
        table = data.sheets()[0]
        x = table.col_values(0)
        y = table.col_values(1)
        del x[0]
        del y[0]

    #  table = data.sheets()[1]
    # x = table.col_values(0)
    #  del x[0]
    #  y = table.col_values(1)
    #  del y[0]
    #  res = []
    # print(it.x, it.y)

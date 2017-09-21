# -*- coding: utf-8 -*-
from ctypes import *
import os
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


def getPos(mode, target, infile, outfile):
    """TODO: get pos of MC

    :x: TODO
    :y: TODO
    :returns: TODO

    """
    libtest = cdll.LoadLibrary(os.getcwd() + '/mc.so')
    libtest.convertLL2MC.restype = MC
    libtest.convertLL2MC.argtypes = (c_double, c_double)
    table = data.sheets()[1]
    # x = table.col_values(0)
    del x[0]
    y = table.col_values(1)
    del y[0]
    res = []
    # print(it.x, it.y)
    for i in range(0, len(x)):
        it = libtest.convertLL2MC(y[i], x[i])
        res.append({"x": it.x, "y": it.y, "qt": "rgc", "dis_poi": 1})
        r = requests.get('http://api.map.baidu.com/', params=res[i])
        resTest = json.loads(r.text)
        # print(resTest)
        resUltimateJson = json.loads(r.text, object_hook=JSONObject)
        # print(resUltimateJson)
        print(resUltimateJson.content.address)

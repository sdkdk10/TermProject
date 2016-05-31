# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:04:47 2016

@author: 박지희
"""
loopFlag = 1
from xml.etree import ElementTree
import http.client

def extractBookData(strXml):
    tree = ElementTree.fromstring(strXml)
    
    itemElements = tree.getiterator("item")
    print(itemElements)
    print("item")
    for item in itemElements:
        #if(item.find("infoType")).text == "1":
        code = item.find("code")
        sname = item.find("sname")

        print(str(code.text) + "\t" + str(sname.text))
        
        
def GetCityCode():

    key = "GH9cfIKgPs69CGQioE5A2dYp9V1P8OCywu%2BnaanIOWiTue3FlroqDCEuWo4k8ekz%2F91Wlhpx%2Bwl6kfHWTG0EAg%3D%3D"
    
    conn = http.client.HTTPConnection("openapi.tago.go.kr")
    conn.request("GET", "/openapi/service/ArvlInfoInqireService/getCtyCodeList?ServiceKey=" + key)
    
    req = conn.getresponse()
    print(req.status)
    cLen = bytearray(req.getheader("Content-Length"), 'utf-8')
    
    if int(req.status) == 200:
        print("Complete!!!")
        extractBookData(req.read().decode('utf-8'))
    else:
        print("Failed!!retry")
    
    
def printMenu():
    print("막차시간정보")
    print("========Menu==========")
    print("도시코드:  l")
    print("========Menu==========")
    
    
def launcherFunction(menu):
    if menu ==  'l':
        GetCityCode()

    else:
        print ("error : unknow menu key")

while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
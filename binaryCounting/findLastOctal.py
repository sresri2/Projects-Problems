#!/bin/python3

import math
import os
import random
import re
import sys

def findLastOctal(s):
    binaryStr = ""
    for i in s:
        asci = ord(i)
        b = bin(int(asci)).strip()
        b = b[2:]
        if len(b) < 8:
            x = 8-len(b)
            x = "0"*x
            b = x+b

        binaryStr += b

    nextFind = "0"
    while True:
        x = len(nextFind)
        found= False
        for pos in range(0,len(binaryStr)):
            a = binaryStr[pos:pos+x]
            if a == nextFind:
                found = True
                break
        if not found:
            break
        else:
            binaryStr = binaryStr[0:pos] + binaryStr[pos+x:]


        found = False
        for pos in range(0,len(binaryStr))[::-1]:
            a = binaryStr[pos:pos+x]
            if a == nextFind:
                found = True
                break
        if found:
            binaryStr = binaryStr[0:pos] + binaryStr[pos+x:]
        nextFind = bin(int(nextFind,2)+1).strip()[2:]
        
        
    binaryStr = int(binaryStr,2)
    octalStr = oct(binaryStr)[2:]

    nextFind = "0"
    while True:
        if octalStr == "":
            return int(oct(int(nextFind,8)-1).strip()[2:],8)
        x = len(nextFind)
        found= False
        for pos in range(0,len(octalStr)):
            a = octalStr[pos:pos+x]
            if a == nextFind:
                found = True
                break
        if not found:
            if nextFind == "0":
                return -1
            return int(oct(int(nextFind,8)-1)[2:],8)
        else:
            octalStr = octalStr[0:pos] + octalStr[pos+x:]
        if octalStr == "":
            return nextFind
        found= False
        for pos in range(0,len(octalStr))[::-1]:
            a = octalStr[pos:pos+x]
            if a == nextFind:
                found = True
                break
        if found:
            octalStr = octalStr[0:pos] + octalStr[pos+x:]
        nextFind = oct(int(nextFind,8)+1).strip()[2:]
    

print(findLastOctal("hruhuiwfirenufuw."))

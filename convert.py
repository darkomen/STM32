#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "SLP"
import os
import sys
import argparse
from shutil import copyfile

class Convert():
    def __init__(self):
        # Geting the config file from ArgumentParser
        parser = argparse.ArgumentParser(description='Script to convert a STM32cube mx project to a platformio project. In this version, is necesary create both projects before execute this script')
        parser.add_argument('-s','--stm32cube', help='SMT32cube project folder', required=True)
        parser.add_argument('-p','--platformio', help='PlatformIO project folder', required=True)
        args = vars(parser.parse_args())
        self.__cubeRoot = args['stm32cube']
        self.__cubeInc = self.__cubeRoot + "/Inc"
        self.__cubeSrc = self.__cubeRoot + "/Src"
        self.__platRoot = args['platformio']
        self.__platSrc = self.__platRoot + "/src"

    def run(self):
        self.initPlatform()
        self.copyRoot()
        self.copyInc()
        self.copySrc()

    def copyRoot(self):
        files = os.listdir(self.__cubeRoot)
        self.__ldfile = [f for f in files if f[-2:] == "ld"]
        srcname = os.path.join(self.__cubeRoot, self.__ldfile[0])
        dstname = os.path.join(self.__platRoot, self.__ldfile[0])
        copyfile(srcname, dstname)

    def copyInc(self):
        files = os.listdir(self.__cubeInc)
        print(files)
        for f in files:
            srcname = os.path.join(self.__cubeInc, f)
            dstname = os.path.join(self.__platSrc, f)
            copyfile(srcname, dstname)

    def copySrc(self):
        files = os.listdir(self.__cubeSrc)
        for f in files:
            srcname = os.path.join(self.__cubeSrc, f)
            dstname = os.path.join(self.__platSrc, f)
            copyfile(srcname, dstname)

if __name__ == "__main__":
    project = Convert()
    project.run()

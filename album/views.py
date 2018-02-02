# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

import os
from PIL import Image


def raw2Png(filePath):
    fileName, fileExt = os.path.splitext(filePath)
    if ".raw" != fileExt:
        return

    with open(filePath, "rb") as f:
        rawData = f.read()
        # img = Image.fromstring("L", )
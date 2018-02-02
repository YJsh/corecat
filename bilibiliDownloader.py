# -*- coding: utf-8 -*-

def mergeFlv():
    with open("res.flv", "wb") as out:
        with open("28904285-1-80.flv", "rb") as flv:
            out.write(flv[:9])
            i = 9

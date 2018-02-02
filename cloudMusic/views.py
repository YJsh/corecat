import base64

from django.shortcuts import render
from Crypto.Cipher import AES
import json
import os
# Create your views here.


def createSecretKey(size):
    return (''.join(map(lambda x: (hex(ord(x))[2:]), os.urandom(size))))[:16]


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(text.encode('hex'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text += pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    cipherText = encryptor.encrypt(text)
    cipherText = base64.b64encode(cipherText)
    return cipherText


def login(nonce, pubKey, modulus):
    url = "http://music.163.com/weapi/login/cellphone"
    text = {
        "username": "15267002566",
        "password": "zx37294631",
        "rememberLogin": "true",
    }
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {
        'params': encText,
        'encSecKey': encSecKey
    }

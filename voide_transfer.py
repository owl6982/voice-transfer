import wave
from tkinter import INSERT
from pyaudio import PyAudio,paInt16
import chardet
import json
import base64
import os
import requests
import time
import re

def vtransfer(text):
    
    #获取tokent
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    client_id = "x4uFCgHD4T1EzFCfPudfzfUY"
    #Secret Key
    client_secret = "dF7E8ebCXEL3ES2RGrWb2dIWpBWN6Ekn"

    #拼url
    url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
    #print(url)
    #获取token
    res = requests.post(url)
    #print(res.text)
    token = json.loads(res.text)["access_token"]
    #print(token)
    #24.b891f76f5d48c0b9587f72e43b726817.2592000.1524124117.282335-10958516
    #设置格式
    RATE = "16000"
    FORMAT = "wav"
    CUID="wate_play"
    DEV_PID="1536"

    #以字节格式读取文件之后进行编码
    with open(r'TPO55综合听力.wav', "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf8')
    size = os.path.getsize(r'16k.wav')
    headers = { 'Content-Type' : 'application/json'} 
    url = "https://vop.baidu.com/server_api"
    data={

            "format":FORMAT,
            "rate":RATE,
            "dev_pid":DEV_PID,
            "speech":speech,
            "cuid":CUID,
            "len":size,
            "channel":1,
            "token":token,
        }

    req = requests.post(url,json.dumps(data),headers)
    
    result = json.loads(req.text)
    print(type(result))
    
    text.insert(INSERT,result['result'])

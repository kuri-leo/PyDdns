'''
DDNS Script
'''
# !/usr/bin/python
# -*- coding:utf-8 -*-

import os
import requests

ID = ""  # your ID
TOKEN = ""  # Your Token
DOMAIN_NAME = "" # your domain
SUB_DOMAIN = "" # your sub domain


DATA = {
    "sub_domain": "",
    "login_token": "",
    "format": "json",
    "domain_id": "",
    "record_id": "",
    "record_line": "默认",
    "value": ""
}


def update():
    # update DATA
    DATA['sub_domain'] = SUB_DOMAIN
    DATA['login_token'] = ("%s,%s" % (ID, TOKEN))
    DATA['domain_id'] = getDomain_id(DOMAIN_NAME)
    DATA['record_id'] = getRecord_id(SUB_DOMAIN, DATA['domain_id'])
    DATA['value']=getLocalIp()

def check():
    # check if everything in DATA is legal
    return DATA['login_token'] != None and DATA['domain_id'] != None and DATA['record_id'] != None and DATA['value'] != None


def getLocalIp():
    # get your router's IP
    f = os.popen(
        r'ifconfig pppoe-netkeeper | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
    return f.read()


def doPost(url, data):
    # method for sending your data via POST
    # and return response data in JSON
    header = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/json"
    }
    response = requests.post(url=url, data=data, headers=header)
    json = response.json()
    return json


def getDomain_id(DOMAIN_NAME):
    # get your domain_id
    url = "https://dnsapi.cn/Domain.List"
    data = {"login_token": ("%s,%s" % (ID, TOKEN)),
            "format": "json"
            }
    response = doPost(url, data)
    for domain in response['domains']:
        if DOMAIN_NAME == domain['punycode']:
            return domain['id']
    return None


def getRecord_id(SUB_DOMAIN, domain_id):
    # get your record_id
    # curl 'https://dnsapi.cn/Record.List' -d 'login_token=<your_login_token>&format=json&domain_id=<your_domain_id>'
    url = "https://dnsapi.cn/Record.List"
    data = {"login_token": ("%s,%s" % (ID, TOKEN)),
            "format": "json", "domain_id": domain_id}
    response = doPost(url, data)
    # print(response)
    for record in response['records']:
        if SUB_DOMAIN == record['name']:
            return record['id']
    return None


def ddns():
    # do ddns
    url = "https://dnsapi.cn/Record.Ddns"
    update()
    if check():
        response = doPost(url, DATA)
        print(response)
        return response['status']['code']==1
    else:
        return False


if __name__ == "__main__":
    ddns()


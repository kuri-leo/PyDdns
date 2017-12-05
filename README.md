# PyDdns
DDns script for dnspod.cn and written in Python3

# Install
~~Write for router(Openwrt/LEDE), but it could be used in any Linux machine~~

## Prepare your router
1. ```opkg update```
2. install python3: ```opkg install python3```
3. install pip:
    - download ```https://bootstrap.pypa.io/get-pip.py```
    - install ```python get-pip.py```
4. install requests: ```pip install requests```

## Prepare python file
1. in ```ddns.py``` file
```
ID = ""  # your ID
TOKEN = ""  # Your Token
DOMAIN_NAME = "" # your domain
SUB_DOMAIN = "" # your sub domain
```
2. upload file to router
3. create a file in ```/etc/ppp/ip-up.d``` ,and add ```python3 /root/script/ddns.py > /tmp/log/dnspod.log``` to file.
**DO NOT USE crontab!**
4. ```chmod 777 /etc/ppp/ip-up.d/<your_script_name>```

## Why not crontab?
Dnspod.cn declare a limitation that every user can only upload 5 times in an hour if remote IP address and local IP address is same.

They also sugget that build a script when you create a new dial-up connection, run the script to update your IP address.

So it is in ```/etc/ppp/ip-up.d``` folder, that every time you use ```pppoe``` to connect to the Internet and you will receive a new IP address. Then every time ```pppoe``` runs, the OS will run every script in ```/etc/ppp/ip-up.d``` folder.

## Future plan
1. move all personal parameters to a config file.
2. simplify code

## LICENSE
WFTDPL
```
You just DO WHAT THE FUCK YOU WANT TO.
```
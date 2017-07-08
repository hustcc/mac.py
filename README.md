# Mac.py

A python lib to search Manufacturer of mac address. With method `search`.
You can update the mac address dictionary with method `update_dictionary_online` from http://standards-oui.ieee.org/oui/oui.txt.
Also, you can update the mac address dictionary with method `update_dictionary` offline.

一个用于利用物理地址查询网卡所属厂商的Python库，使用`search`方法进行查找。
可以使用`update_dictionary_online`方法从 http://standards-oui.ieee.org/oui/oui.txt 更新mac地址字典。
或者使用`update_dictionary`方法指定oui.txt文件对mac地址字典进行离线更新。

[![Build Status](https://travis-ci.org/hustcc/mac.py.svg?branch=master)](https://travis-ci.org/hustcc/mac.py) [![PyPi Status](https://img.shields.io/pypi/v/mac.py.svg)](https://pypi.python.org/pypi/mac.py) [![Python Versions](https://img.shields.io/pypi/pyversions/mac.py.svg)](https://pypi.python.org/pypi/mac.py) [![PyPi Downloads](https://img.shields.io/pypi/dm/mac.py.svg)](https://pypi.python.org/pypi/mac.py)

## Install

```sh
pip install mac.py
```

## Usage

```py
from macpy import Mac

mac = Mac()
## run method update_dictionary_online ensures that you get the latest results
## Warging, that may take a long time ,depends on your network speed。
# mac.update_dictionary_online()
mac.search('00016C')
mac.search('00:01:6C:06:A6:29')
mac.search('00-01-6C-06-A6-29')
mac.search('00') # None
mac.search('') # None

```

## Output

search result will be

```py
{
	're': 'Brea  CA  92821', 
	'com': 'FOXCONN', 
	'addr': '105 S Puente St.', 
	'co': 'US'
}
```
or `None`

What's the meaning of `result dict key`:

 - `com`: company name
 - `re`: company region
 - `addr`: company address
 - `co`: company country


## Online Search

 - [http://www.atool.org/mac.php](http://www.atool.org/mac.php)

Welcome to issue or pr.

# Mac.py

A python lib to search Manufacturer of mac address. With only one method `search`.

一个用于利用物理地址查询网卡所属厂商的Python库，只有一个Api方法。

[![Build Status](https://travis-ci.org/hustcc/mac.py.svg?branch=master)](https://travis-ci.org/hustcc/mac.py) [![PyPi Status](https://img.shields.io/pypi/v/mac.py.svg)](https://pypi.python.org/pypi/mac.py) [![Python Versions](https://img.shields.io/pypi/pyversions/mac.py.svg)](https://pypi.python.org/pypi/mac.py) [![PyPi Downloads](https://img.shields.io/pypi/dm/mac.py.svg)](https://pypi.python.org/pypi/mac.py)

## Install

```sh
pip install mac.py
```

## Usage

```py
from macpy import Mac

mac = Mac()
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

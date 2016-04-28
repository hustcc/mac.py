# Mac.py

A python lib to search Manufacturer of mac address. With only one method `search`.

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
mac.search('00')
mac.search('')

```


## Result

search result will be

```py
{
	're': 'Brea  CA  92821', 
	'com': 'FOXCONN', 
	'addr': '105 S Puente St.', 
	'co': 'US'
}
```
or None

What's the meaning of `result dict key`:

 - `com`: company name
 - `re`: company region
 - `addr`: company address
 - `co`: company country

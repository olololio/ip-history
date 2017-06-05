import requests
from bs4 import BeautifulSoup
import json

def validateIP(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def getIPfrom2IP():
	session = requests.Session()
	session.encoding = 'utf-8'
	resp = session.get('http://2ip.ru', timeout=2)
	if resp.status_code != 200:
		return None
	soup = BeautifulSoup(resp.text, "html.parser")
	ip = soup.findAll('big', {'id':'d_clip_button'})[0].next
	if validateIP(ip):
		return ip
	else:
		return None

def getIPfromHttpBinOrg():	
	session = requests.Session()
	session.encoding = 'utf-8'	
	resp = session.get('http://httpbin.org/ip', timeout=2)
	if resp.status_code != 200:
		return None
	json_data = json.loads(resp.text)
	if 'origin' in json_data:
		ip = json_data.get('origin')
		if validateIP(ip):
			return(ip)
		else:
			return None
	else:
		return None
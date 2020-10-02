import requests, datetime, os, random, sys
from bs4 import BeautifulSoup

headers_useragents = list ()

def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)
	
def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def initHeaders():
	useragent_list()
	global headers_useragents
	headers = {
				'User-Agent': random.choice(headers_useragents),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}

	return headers

def get_proxy (url):
	r = requests.get (url)

	soup = BeautifulSoup (r.text, 'lxml')
	line = soup.find ('table', id = 'theProxyList').find ('tbody').find_all ('tr')	

	file = open ('proxies.txt', 'w+')

	for tr in line:
		td = tr.find_all ('td')

		ip = td[1].text
		port = td[2].text

		file.write ('http://' + ip + ':' + port + '\n')

get_proxy ('http://foxtools.ru/Proxy?al=True&am=True&ah=True&ahs=True&http=True&https=False')


#####################################################################################
############################   Example of use  #####################################
#####################################################################################
def RequestsGet(URL):
    proxy = 'proxies.txt'
    get_proxy ('http://foxtools.ru/Proxy?al=True&am=True&ah=True&ahs=True&http=True&https=False')
    proxies = open (proxy, 'r').read().splitlines()
    prox = {}
    
    for p in proxies:
        headers = initHeaders()	
        prox['http'] = p
        response = requests.get(URL,proxies=prox, headers = headers)
        return response
print(RequestsGet('https://github.com/'))

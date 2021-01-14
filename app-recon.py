import requests
import re

def app_recon_baidu():
	header = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
	}
	apps = []
	for pn in range(0,6):
		pn = pn * 10
		url = 'https://www.baidu.com/s?ie=utf-8&wd=site%3Aapp.mi.com%20%E5%8C%97%E4%BA%AC%E4%BA%94%E5%85%AB%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&pn={}'.format(pn)
		res = requests.get(url,headers=header).text
		pattern = re.compile(r'data-tools=\'{\"title\":\"(.*?)-')
		app = re.findall(pattern,res)
		apps += set(app)
	return apps

def subscription_recon_sougou():
	header = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
	}
	subscriptions = []
	for pn in range(0,6):
		url = 'https://weixin.sogou.com/weixin?query=58&ie=utf8&page={}'.format(pn)
		res = requests.get(url,headers=header).text
		pattern = re.compile(r'beg-->(.*?)</a>')
		subscription = re.findall(pattern,res)
		subscriptions += set(subscription)
	return subscriptions

def mini_program_recon():
	url = "https://mp.weixin.qq.com/wxa-cgi/innersearch/subsearch"
	data = r'query=58&offset_buf={"page_param":[{"subsys_type":1,"server_offset":0,"server_limit":120,"index_step":3000,"index_offset":30}],"client_offset":0,"client_limit":8}&from_h5=0&begid=0&longitude=0&latitude=0&h5version=65900700&subsys_type=1&sub_type=1&q_highlight=&search_id=c19ee740-2d06-e6d4-cfb3-06c114a47b08&source=0&scene=70&search_scene=1&session_id=437d8cd4-0a13-9621-415b-2b47bb7fa6b7&ext_buf=&business_type=105&cookie=cpx3VhudKBXDnwAq6sgvwRHWUEyKRQJg7XBfBEjAjBwnb9jbGkYnB6isAeLPjqN8n%252F43P9HwWva2AAOyYRpomw%253D%253D%257C%257C%257C08dffbbda3660591e95cacdab0c3c8058e6eeb0dd9368c8a469957e359b4587f3c3fead271fc8e11b0b14a611d8cf92cae776f02127aca28016a8029a8ec0c0c5b3b22c48a17f2403603278ff3fce32644b5ef1e9161f71d62dc974a6f295b84943c020aa7deb78708d0024a6632c3de31d853855233b667832181fd4cbd5b8d&client_version=1660944639&device=15&sugtype=3&sugid=11462302230123654519&sugpos=0&prefixsug=58&sugbuf='
	res = requests.post(url,params=data).text
	pattern = re.compile(r'nickName":"(.*?)","path')
	mini_program = re.findall(pattern,res)
	return mini_program			

if __name__ == '__main__':
	app_recon = app_recon_baidu()
	print("APP资产：","\n",app_recon)
	subscription_recon = subscription_recon_sougou()
	print("微信订阅号资产：","\n",subscription_recon)
	mini_program_recon = mini_program_recon()
	print("微信小程序资产：","\n",mini_program_recon)



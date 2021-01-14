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
	data = r'' # 搜索抓包，替换为你的请求内容，index_step参数控制结果中小程序的数量
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



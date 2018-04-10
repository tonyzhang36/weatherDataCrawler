# -*- encoding=utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
import fileDownloader
import dirMaker
import xlwt
import json

def crawlData(baobeiUrl):
	sizeList=[]
	colorList=[]
	firstMainImg=''
	firstMainImgPath=''
	#无颜色图片的链接
#	baobeiUrl='https://detail.1688.com/offer/42201709111.html?spm=a360q.7751291.0.0.ldp7Cj'
	print '------------------------------>'
	print u'数据抓取开始，链接为：%s' % (baobeiUrl)
	#请求页面内容
	try:
		response=urllib2.urlopen(baobeiUrl)
	except BaseException as e:
		print 'urlopen failed'
		return False
	finally:
		pass
	htmlDoc = response.read()
	#保存原始网页内容
	htmlFile = open("%soriginal.html"%'weather_','w+')
	htmlFile.write(htmlDoc)
	htmlFile.close()


	#初始化网页解析器对象
	soup = BeautifulSoup(htmlDoc,'html.parser',from_encoding = 'utf-8')

	#print soup.body


	#找到车辆限行信息
	'''
	<div class="sk">
	<div class="zs limit">
	<i></i>
	<span>限行</span><em><b>4</b>和<b>9</b></em>
	</div>
	</div>
	'''

	itemName = soup.find('div', class_ = 'zs limit')
	if not itemName == None:
		name = itemName.get_text()
		print name
	else:
		print 'can\'t find itemName! stop'
		print u'数据抓取失败，可能原因：网络异常'
		print '------------------------------<'
		return False

	#
	print u'限行数据抓取完毕'
	
	print '------------------------------<'
	return True
crawlData(r'http://www.weather.com.cn/weather1d/101010300.shtml')

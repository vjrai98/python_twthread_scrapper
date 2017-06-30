import urllib
import urllib.request
import urllib.parse
import re
import os
from bs4 import BeautifulSoup
#def get_images(n, dir): #n is number of images, dir is directory name
url = "https://twitter.com/weeditiotic/status/870668769940484096"
thepage= urllib.request.urlopen(url)
soup= BeautifulSoup(thepage,"html.parser")

'''print(soup.title)
for img in soup.findAll('img'):
	print(img.get('src'))'''
j=1
temp=(soup.findAll("div",{"class":"AdaptiveMedia-photoContainer"}))
#print(temp)
dir="alexandra"
for img in temp:
	img=str(img)
	t=list(re.findall('src="(.*?)"',img))
	for i in t:
		print(i)
		if not os.path.exists(dir):
			os.makedirs(dir)
		urllib.request.urlretrieve(i, dir+"/"+ (str(j)+".jpg"))
		j=j+1

	
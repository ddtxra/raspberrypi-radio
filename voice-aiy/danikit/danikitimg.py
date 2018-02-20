from bs4 import BeautifulSoup as Soup
import sys
import json
import os
import urllib
import urllib.request
from urllib.request import urlopen
from scipy import misc

directory = "/home/pi/color-images"
if not os.path.exists(directory):
    os.makedirs(directory)

def download_image(query_string, file):
    url = 'https://api.qwant.com/api/search/images?count=1&offset=1&q=' + query_string
    print ("downloading from ... " + url)
    req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0'})
    f = urllib.request.urlopen(req)
    data = f.read()
    encoding = f.info().get_content_charset('utf-8')
    res = json.loads(data.decode(encoding))
    print(data)
    imgUrl = "https:" + str(res["data"]["result"]["items"][0]["thumbnail"])
    print (imgUrl)
    response = urllib.request.urlopen(imgUrl)
    with open(file, 'wb' ) as fo:
        fo.write( response.read() )

def get_image_color(query_string):
    file = directory + "/" + query_string + ".jpg"
    if not os.path.isfile(file):
        download_image(query_string, file)
     
    rgb = misc.imread(file).mean(axis=(0,1))
    print(query_string + ":" + str(rgb))
    return rgb

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        get_image_color(sys.argv[1])
    else:
        get_image_color("sun")

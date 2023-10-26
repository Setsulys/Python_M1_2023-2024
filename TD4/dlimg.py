

from urllib.request import urlopen, urlretrieve
from html.parser import HTMLParser
from time import strftime
import sys
import os


class URLLister(HTMLParser):
    def reset(self):                              
        HTMLParser.reset(self)
        self.urls = []

    def handle_starttag(self, tag, attrs):    
        if tag =="img":
            href = [v for k, v in attrs if k=='src']
            if href:
                self.urls.extend(href)


def script(url):
    html = urlopen(url).read().decode('utf8')
    p = URLLister()
    p.feed(html)
    p.close()
    for u in p.urls: 
        try:
            filename = os.path.join("./imgs",strftime("%Y-%m-%d_%H-%M-%S")+u)
            urlretrieve(url,filename)
        except:
            pass



if __name__ == "__main__":
    if(len(sys.argv)<2):
        raise Exception("no good")
    script(sys.argv[1])


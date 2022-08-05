from bs4 import BeautifulSoup
import urllib.request
import requests
import urllib
#website from which we download all images
website = "https://store.steampowered.com/digitalgiftcards/"
html_page = urllib.request.urlopen(website)
soup = BeautifulSoup(html_page, "html.parser")
images = []
links = []

def get_images(website):
    for img in soup.findAll('img'):    
        images.append(img.get('src'))    
    for link in images:
        if link[:1] == "/" or "\\":
            links.append(link)
        else: links.append(link)
        for i in links:
            dawd = i[i.rfind("/") +1:] or i[i.rfind("\\") +1:]
            dawd = dawd[:dawd.find(".")+4]
            urllib.request.urlretrieve(i, dawd)  
    print("The links:" + str(links))
    
get_images(website)
import os
import re
import urllib

from bs4 import BeautifulSoup
from selenium import webdriver

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

driver = webdriver.Chrome(executable_path=f"{dir_path}/chromedriver")
driver.get('https://anomalab.io/')

html = driver.page_source

URL = urllib.request.urlopen('https://anomalab.io/')
soup = BeautifulSoup(html, features='lxml')

data = soup.findAll(text=True)


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


result = filter(visible, data)

mails = []
for r in result:
    if '@' in r:
        mails.append(r)


def is_backwards(mail):
    if '.' in mail[2:4]:
        return True
    else:
        return False


def flip_if_backwards(mail):
    if is_backwards(mail):
        flipped = mail[len(mail)::-1]   # slicing
        return flipped


print(flip_if_backwards(mails[0]))

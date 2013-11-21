from bs4 import BeautifulSoup
from urllib2 import urlopen
import time
import re 

def parser(text):
    ans = []
    for x in re.split(' |\n|,',text):
        if not len(x) <1:
            ans.append(x)
    ans = " ".join(ans)
    return ans


def uniSearch(keywords):
    default="https://www.myedu.com/search/?search_term=%s&doctype=school&school=1565"
    key = []
    ans = []
    for x in keywords.split(' '):
        if not len(x) < 1:
            key.append(x)
    key = "+".join(key)
    request= urlopen(default %(key))
    soup = BeautifulSoup(request)
    for x in soup.find_all(class_="school"):
        for i in x.find_all("a",limit=1):
            ans.append([u'https://www.myedu.com'+i.get('href'),parser(i.get_text()),u'https://www.myedu.com'+i.get('href')+'/professor/by-department'])
    request.close()
    return ans


def imgSearch(link): #pass in link to certain university's info pg
    request = urlopen(link)
    soup = BeautifulSoup(request)
    ans = []
    for x in soup.find(id='admissions').find_all('img'):
        ans.append(x.get('src'))
    return ans

def depSearch(link): #pass in the link to a certain university's department pg
    request = urlopen(link)
    soup = BeautifulSoup(request)
    ans = []
    for x in soup.find_all(class_='name'):
        ans.append(['https://www.myedu.com'+x.get('href'),x.get_text()])
    request.close()
    return ans
                

    
def profSearch(link):
    request = urlopen(link)
    soup = BeautifulSoup(request)
    ans = []
    for x in soup.find_all(class_='name'):
        name = x.get_text()
        if name.find(',') !=-1:
            ans.append(['https://myedu.com'+x.get('href'),parser(name)])
    request.close()
    return ans

def courseSearch(link):
    request = urlopen(link)
    soup = BeautifulSoup(request)
    ans = []
    for x in soup.find_all():
        name = parser(x.get_text())
        for i in x.find_all('img'):
            link = i.get('src')
            ans.append([name,link])
    request.close()
    return ans


if __name__ == "__main__":
    
    start = time.time()
    url = uniSearch("      yale  university")
    print(imgSearch(url[0][0]))
    dep = depSearch(url[0][2])
    prof = profSearch(dep[0][0])
    end = time.time() - start
    print(end)


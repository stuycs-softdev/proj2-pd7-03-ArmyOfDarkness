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

#pass in a string that the user searched up
#return [[<url to first university's default pg(stats)>,<name of university>,<url to university's list of departments>],[<the next university's stuff>],[<etc>]]
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
    for x in soup.find_all("ul",id="search-results",limit=1):
        for j in x.find_all(class_="school"):
            for i in j.find_all("a",limit=1):
                ans.append([u'https://www.myedu.com'+i.get('href'),parser(i.get_text()),u'https://www.myedu.com'+i.get('href')+'/professor/by-department'])
    request.close()
    return ans


#pass in link to university x's info pg
#returns [<img 1: of enrollment rates>,<img 2: of avg std test scores>]
def imgSearch(link): 
    request = urlopen(link)
    soup = BeautifulSoup(request)
    ans = []
    for x in soup.find(id='admissions').find_all('img'):
        ans.append(x.get('src'))
    return ans

#pass in the link to university x's list of departments
#returns [[<url to the first department's list of profs>,<name of department>],[<the next department's stuff>],[<etc>]]
def depSearch(link): 
    request = urlopen(link)
    soup = BeautifulSoup(request)
    ans = []
    for x in soup.find_all(class_='name'):
        ans.append(['https://www.myedu.com'+x.get('href'),x.get_text()])
    request.close()
    return ans
                
#pass in link to university X's department Y's list of professors
#returns [[<url to the first prof's pg>,<prof's name>],[<the next prof's stuff>],[<etc>]]
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

# pass in url to x university's y department's z professor's list of courses
# returns [<name of course>,<img with avg grade>]
def courseSearch(link): 
    request = urlopen(link)
    soup = BeautifulSoup(request)
    ans = []
    for x in soup.find_all(<fill>):
        name = parser(x.get_text())
        for i in x.find_all('img'):
            link = i.get('src')
            ans.append([name,link])
    request.close()
    return ans
   

if __name__ == "__main__":
    
    start = time.time()
    url = uniSearch("      yale  university")
    img = imgSearch(url[0][0])
    dep = depSearch(url[0][2])
    prof = profSearch(dep[0][0])
    end = time.time() - start
    
    print(end)


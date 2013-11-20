from urllib2 import urlopen
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.myedu.com/search/?search_term=university+of+michigan+ann+arbor&school=1565"
    request = urlopen(url)
    soup = BeautifulSoup(request)
    data = {}
    for x in soup.find(class_="school").find_all("a",limit=1):
        data['_url']= u"https://www.myedu.com"+x.get("href")
    data['_departmentURL']= data['_url'] + "/professor/by-department"
    request.close()

    request = urlopen(data['_url'])
    soup = BeautifulSoup(request)
    data['_image'] = []
    for x in soup.find(id="admissions").find_all("img"):
        data['_image'].append(x.get('src'))
    request.close()

    request = urlopen(data['_departmentURL'])
    soup = BeautifulSoup(request)
    data['_departments'] = []
    for x in soup.find_all(class_="name"):
        data['_departments'].append(["https://myedu.com"+x.get('href'),x.get_text()])
    request.close()
    a="""
    data['_professors'] = {}
    for department in data['_departments']:
        request = urlopen(department[0])
        soup = BeautifulSoup(request)
        data['_professors'][department[1]]=[]
        for x in soup.find_all(class_="name",limit=2):
            name = x.get_text()
            if name.find(',')!=-1:
                name = name.split(',')
                name[0]=name[0].strip()
                name[1]=name[1].strip()
                name = ','.join(name)
                data['_professors'][department[1]].append(("https://myedu.com"+x.get('href'),name))
        request.close()
"""
    print(data)
    print(len(data['_departments']))

    


if __name__ == "__main__":
    print("testing myedu.com scraping\n")
    scrape()

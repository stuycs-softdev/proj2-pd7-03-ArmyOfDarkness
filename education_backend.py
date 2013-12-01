#!/usr/bin/python

#goal: to create an ability to export data from the education api 
#and host it on our website. 

import json #download json and then import it in order to access functionality.
from urllib2 import urlopen

def run():
    key = "2db9eedc16ba9389991b223c4fb97df8"
    key1 = "7d733591e1f66640dc372fcb658fe38d"
    url = "http://api.education.com/service/service.php?f=schoolSearch&key=7d733591e1f66640dc372fcb658fe38d&sn=sf&v=4&city=san+francisco&state=ca&resf=json"
    print url
    input1 = urlopen(url)
    json_raw = input1.read() 
    json_data = json.loads(json_raw)

    print json_data
    #for x in range (0, len(json_data)):
     #   entry = json_data[x]
      #  entry_info = entry['school']
       # print "School #" + str(x) + ': ' + str(entry_info) 

# entry_info['city'], entry_info['schooldistrictname'], entry_info['website']

def citysearch(city, state, zipcode):
    key = "2db9eedc16ba9389991b223c4fb97df8"
    key1 = "7d733591e1f66640dc372fcb658fe38d"
    url = "http://api.education.com/service/service.php?f=schoolSearch&key=7d733591e1f66640dc372fcb658fe38d&sn=sf&v=4"

    #&city=san+francisco&state=ca&resf=json"

   # print url
    if city != "": 
        url = url + "&city=" + city
    if state != "":
        url = url + "&state=" + state
    if zipcode != "":
        url = url + "&zip=" + zipcode
    url = url + "&resf=json"
    
    input1 = urlopen(url)
    json_raw = input1.read() 
    json_data = json.loads(json_raw)
    
    #return json_data
    #print json_data
    #for x in range (0, len(json_data)):
    #entry = json_data[x]
    #entry_info = entry['school']
    #print "School #" + str(x) + ': ' + str(entry_info) 

    results = []

    for entry in json_data:
        data  = []
        school = entry['school']

        try: 
            data.append(school['schoolname'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['schooldistrictname'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['schooltype'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['gradelevel'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['gradesserved'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')

        #special case
        try:
            students = school['enrollment']
            data.append(students['total'])
        except: 
            data.append ('None Available')

        try:             
            students = school['studentteacherratio']
            data.append(students['total'])
        except: 
            data.append ('None Available')
            
        #end of special case
            
        try:
            data.append(school['state'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try:             
            data.append(school['city'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['zip'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['address'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['phonenumber'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['website'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['url'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['latitude'])
        except: 
            data.append ('None Available')
        try: 
            data.append(school['longitude'])
        except:
            data.append ('None Available')
        try: 
            data.append(school['districtid'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['districtleaid'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['schoolid'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['nces_id'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['testrating_image_small'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['testrating_year'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['testrating_image_large'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')
        try: 
            data.append(school['testrating_text'].encode ('ascii', 'ignore'))
        except: 
            data.append ('None Available')     
        
        results.append(data)
            
    print results
    return results

if __name__ == '__main__':
    #run()
    citysearch("new+york", "ny", "10022")



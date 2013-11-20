#goal: to create an ability to export data from the education api 
#and host it on our website. 

import json #download json and then import it in order to access functionality.
from urllib2 import urlopen


def run():
    key = "2db9eedc16ba9389991b223c4fb97df9"
    url = "http://api.education.com/service/service.php?f=schoolSearch&key=2db9eedc16ba9389991b223c4fb97df8&sn=sf&v=4&city=san+francisco&state=ca&resf=json"
    print url
    input1 = urlopen(url)
    json_raw = input1.read() 
    json_data = json.loads(json_raw)

    for x in range (0, len(json_data)):
        entry = json_data[x]
        entry_info = entry['school']
        print "School #" + str(x) + ': ' + entry_info['city'], entry_info['schooldistrictname'], entry_info['website']

if __name__ == '__main__':
    run()

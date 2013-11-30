- Education.com - returns in json
    - to get high school rankings  
    - reviews of different school  
    - statistics regarding the student body  
    - teachers, and high school reputation  
    
- LinkedIn.com - supports json  
    - API link: https://developer.linkedin.com/documents/authentication  
    - search by "company" (university) and find all staff assiciated with it  
    - search by name and current workplace/position to find background info and possible achievement  
    - requires OAUTH  
        - link to python OAUTH library: https://github.com/synedra/python-oauth2  
        - link to python OAUTH documentation: https://github.com/synedra/python-oauth2/blob/master/example/client.py  
    
- Collegematch.com - supports json,xml,php  
    - API link: http://www.matchcollege.com/college-data-api  
    - search up universities based on state, major, size of student body, cost, etc  
    - returns each university's list of offered programs, history, atheletic teams, acceptance rates, avg sat/act scores,etc  
    
- Wikipedia.com - json is supported  
    - API link: http://www.mediawiki.org/wiki/API:Main_page  
    - can be used to search up the awards or notible accomplishments of professors at certain universities  
    - for example, searching Nobel laureates on wikipedia returns a chart of all laureates, the year, and field of the prize  
    
- ratemyprofessor.com , ratemyteacher.com  
    - requires page scraping since no api for any of the above sites  
    - returns student reviews of professors in the form of comments, helpfulness, clarity, etc  
    - also gives a list of other professors teaching the same major at that university  
    
- myedu.com  
    - requires scraping  
    - claims to communicate with the universities and obtains data from them  
    - has a list of all professors at an university sorted by major  
    - has list of courses provided at each university and the average grade given  
    
- collegeprowler.com  
    - requires scraping  
    - completely student based data  
    - has polls and surveys about academic flexibility, campus resources, career services, online courses, student body, tuition & financial aid, worth the money, low-stress course load, etc  
    

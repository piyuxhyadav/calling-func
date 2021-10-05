
import re
import time
import webbrowser
from random import randrange
import os
import twilio
from twilio.rest import Client

try:
    from http.cookiejar import CookieJar
except ImportError:
    from cookielib import CookieJar

try:
    input = raw_input
except NameError:
    pass

try:
    from urllib.request import HTTPCookieProcessor, build_opener, install_opener, Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import HTTPCookieProcessor, build_opener, install_opener, Request, urlopen
    from urllib import urlencode




def notify():
    account_sid = 'XXXXXXXXXXXXX'
    auth_token = 'XXXXXXXXXXXXX'

    client = Client(account_sid, auth_token)

    call = client.calls.create(
            twiml='<Response><Say voice="alice">LOGIN AND REGISTER </Say></Response>',
                        to='+91XXXXXXXXXX',
                        from_='+XXXXXXXXXX'
                    )
                    
    print(call.sid)
    webbrowser.open_new(courseURL)


def wait(varDelay):
    randDelay = delay + int(randrange(11))
    time.sleep(randDelay)



def checkSeats(varCourse):
    url = varCourse
    ubcResp = urlopen(url);
    ubcPage = ubcResp.read().decode('utf-8');

  
    t = re.search(totalSeats, ubcPage)
    g = re.search(generalSeats, ubcPage)
    r = re.search(restrictedSeats, ubcPage)

    # Find remaining seats
    if t:
        if t.group(1) == '0':
            return 0
    else:
        print("Error: Can't locate number of seats.")

    if g:
        if g.group(1) != '0':
            return 1
    else:
        print("Error: Can't locate number of seats.")

    if r:
        if r.group(1) != '0':
            return 2
    else:
        print("Error: Can't locate number of seats.")



totalSeats = re.compile(
    "<td width=&#39;200px&#39;>Total Seats Remaining:</td>" + "<td align=&#39;left&#39;><strong>(.*?)</strong></td>")
generalSeats = re.compile(
    "<td width=&#39;200px&#39;>General Seats Remaining:</td>" + "<td align=&#39;left&#39;><strong>(.*?)</strong></td>")
restrictedSeats = re.compile(
    "<td width=&#39;200px&#39;>Restricted Seats Remaining\*:</td>" + "<td align=&#39;left&#39;><strong>(.*?)</strong></td>")


courseURL = input("Enter course + section link:")
season = input("Summer course (y/n):")
year = input("Term year (2015/2016/2017/...):")
acceptRestricted = input("Allowed restricted seating? (y/n):")
delay = int(input("Check after every seconds?"))


deptPattern = 'dept=(.*?)&'
coursePattern = 'course=(.*?)&'
sectionPattern = 'section=(.*)'

dept = re.search(deptPattern, courseURL)
course = re.search(coursePattern, courseURL)
sect = re.search(sectionPattern, courseURL)

if season == 'y':
    season = 'S'
else:
    season = 'W'

registerURL = 'https://courses.students.ubc.ca/cs/main?sessyr=' + year + '&sesscd=' + season + '&pname=subjarea&tname=subjareas&submit=Register%20Selected&wldel=' + dept.group(
    1) + '|' + course.group(1) + '|' + sect.group(1)
courseURL = 'https://courses.students.ubc.ca/cs/main?sessyr=' + year + '&sesscd=' + season + '&pname=subjarea&tname=subjareas&req=5&dept=' + dept.group(
    1) + '&course=' + course.group(1) + '&section=' + sect.group(1)

if delay < 20:
    delay = 20

print("Scanning seat availablility...")

while True:
    status = checkSeats(courseURL)
    if status == 0:
        wait(delay)
        print("test")
        continue
    if status == 1: 
        notify()
        break
    if status == 2:
        if acceptRestricted == "y":
            notify()
            break
        else:
            wait(delay)
            continue

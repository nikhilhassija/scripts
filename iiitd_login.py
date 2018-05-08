#!/usr/bin/env python2

import mechanize
import cookielib
from time import gmtime, strftime

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

r = br.open('http://google.com')

print strftime("%Y-%m-%d %H:%M:%S", gmtime()),

if 'IIIT' in r.read():
    br.select_form(nr=0)
    br["username"] = ""
    br["password"] = ""
    res = br.submit()
    html = res.read()
    if 'keep you' in html:
        print('Login passed')
    else:
        print('Login failed')
else:
    print("You're already logged in.")

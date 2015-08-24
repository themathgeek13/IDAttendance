import mechanize
import cookielib
import getpass

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

# User-Agent Headers
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Open Login Page and login using browser
br.open("https://courses.iitm.ac.in/login/index.php")
br.select_form(nr=0)
user=raw_input('Enter your username:')
br.form['username']=user
password=getpass.getpass('Enter your password:')
br.form['password']=password
br.submit()

# Open the ID1200 page
r=br.open("https://courses.iitm.ac.in/course/view.php?id=1783")
    
# Open the most recent attendance link
br.follow_link(nr=0)
#br.follow_link(nr=0)
br.open('https://courses.iitm.ac.in/mod/questionnaire/complete.php?id=8600')
br.select_form(nr=0)
br.form['q807']=['y']
br.submit()
br.reload()
print 'Successfully put attendance! :)'

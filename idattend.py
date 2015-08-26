import mechanize
import getpass

# Browser
br = mechanize.Browser()

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
for item in br.links():
    if 'Attend' in str(item):
        br.open(item.url)
        break

for newitem in br.links():
   if 'questions' in str(newitem):
      br.open(newitem.url)
      break
  
br.form['q807']=['y']
br.submit()
print 'Successfully put attendance! :)'

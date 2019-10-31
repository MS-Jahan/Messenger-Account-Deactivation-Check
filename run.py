from itertools import islice
from fbchat import Client
from fbchat.models import *
import time
import pickle
from getpass import getpass

try:
	print('Checking for cookies...')
	session_cookies = pickle.load(open('cookies.p','rb'))
	client = Client("cookie", "cookie", session_cookies = session_cookies)
	print('Cookies found!')
except:
	print('Cookies not found. Please enter credentials.')
	client = Client(input('Email: '), getpass('Password: '))
	session = client.getSession()
	pickle.dump(session, open('cookies.p','wb'))
	print('Cookies saved to cookies.p file.')


user = '0'
user_id = '' #Add User ID here


i = 0
while i < 1:
	localtime = time.asctime(time.localtime(time.time()))
	user = client.fetchUserInfo(user_id)[user_id]
	not_avail = "Time: " + localtime + " | " + "User" + " is not available.\n"
	avail = "Time: " + localtime + " | " + "User {}".format(user.name) + " is available.\n"

	if user.name == 'Facebook User':
		print(not_avail)
		f = open("report.txt", "a+")
		f.write(not_avail)
		f.close()
	else:
		print(avail)
		f = open("report.txt", "a+")
		f.write(avail)
		f.close()
		user = '0'
	time.sleep(50)
	i -= 1

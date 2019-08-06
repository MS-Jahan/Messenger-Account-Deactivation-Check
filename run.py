from itertools import islice
from fbchat import Client
from fbchat.models import *
import time

client = Client("email", "password")
session_cookies = client.getSession()
client.getSession()

user = '0'

i = 0
while i < 1:
	localtime = time.asctime(time.localtime(time.time()))
	user = client.fetchUserInfo("user_id")["user_id"]
	not_avail = "Time: " + localtime + " | " + "User {}".format(user.name) + " is not available.\n"
	avail = "Time: " + localtime + " | " + "User {}".format(user.name) + " is available.\n"

	if user == '0':
		print(not_avail)
		f = open("report.txt", "a")
		f.write(not_avail)
		f.close()
	else:
		print(avail)
		f = open("report.txt", "a")
		f.write(avail)
		f.close()
		user = '0'
	time.sleep(300)
	i -= 1



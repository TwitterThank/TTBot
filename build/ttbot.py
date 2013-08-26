import socket
import urllib.request
# XMl functions
from xml.dom import minidom

# Custom functions
def APIAddThank(network, user1, user1twitter, user2twitter, comment):
	request = urllib.request.urlopen("http://twitterthank.com/api/add/thank/?network="+network+"&user1="+user1+"&user1twitter="+user1twitter+"&user2twitter="+user2twitter+"&comment="+comment).read()
	if request == "SUCCESS":
		return True
	else if request == "FAILURE":
		return False
	
# define variables
network
port
serv
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

# check server
if SERVER == "freenode":
	network = "chat.freenode.net"
	port = "6666"
	serv = "freenode"
# right now we only support freenode
else:
	network,port = SERVER.split(":")

# Connect
if not network, port:
	print "Error: No network and port defined!"
else:
	irc.connect( ( network, port ) )
	print irc.recv (4096)
	# Do commands
	if serv:
		if serv == "freenode":
			irc.send('msg NickServ IDENTIFY ' + IRCUSERNAME + " " + IRCPASSWORD + "\r\n")
	else:
		if AUTHCOMMAND == "" or is not AUTHCOMMAND:
			print "Error: No Auth command inputted, and network is not a default.
		else:
			# replace with actual username and password
			AUTHCOMMAND.replace("||username||", IRCUSERNAME)
			AUTHCOMMAND.replace("||password||", IRCPASSWORD)
			irc.send(AUTHCOMMAND)
	irc.send('join #' + CHANNEL)
	# Awesome, we are logged in... Now for the while statement to catch all input to bot
	# first we need to check the LISTENTYPE (mode)
	# yes... I know I am repeating myself. I'd rather keep less within the while statement
	# besides, right now we only support public
	if LISTENTYPE == "public":
		# now while
		while True:
			userSent
			if data.find('!ttbot thank') != -1:
				userSent = data.split()[1]
				userExist = False
				xmldoc = minidom.parse(USERFILE)
				userList = xmldoc.getElementsByTagName('users')
				# Check if the user exists
				for user in userList:
					if user.attributes['ircname'].value == userSent:
						userExist = True
				if userExist == False:
					irc.send('PRIVMSG ' + userSend + " :You have not registered your IRC name with your twitter account. Please do so now, by typing !ttbot register @yourTwitterUsername")
				if userExist == True:
					# get network
					net
					if serv:
						net = serv
					else:
						net = network
					# process
					# split comment and twitter user
					TwitterUserandComment = data.split("@")
				 	twitterUser = TwitterUserandComment[1]
				 	comment = TwitterUserandComment[2]
					APIAddThank(network,userSent,user.attributes['twittername'].value,twitterUser,comment)
				
				
			
	

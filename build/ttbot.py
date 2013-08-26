import socket

network
port
serv
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

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
		if data.find('!ttbot thank') != -1:
			
	

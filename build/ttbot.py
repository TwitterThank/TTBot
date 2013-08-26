import socket

network
port

if SERVER == "freenode":
	network = "chat.freenode.net"
	port = "6666"
# right now we only support freenode
else:
	network,port = SERVER.split(":")


	

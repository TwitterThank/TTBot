# Please see http://twitterthank.com/api/ircbot/config/examples for more information...

# <SERVER> - Which server to connect to
# Predefined options include Freenode (freenode)
# For custom servers, please input the host and port (server.com:port)
# By default, we choose freenode
SERVER = "freenode"

# <USERFILE> - The config xml file which contains the connections between users on TwitterThank.com and the irc network.
# For example, user1 has an account on Twitter.com and therefore an account on TwitterThank.com as @User1
# However, user1 could not get the username on IRC as user1 because it was already taken :(
# Therefore, he/she signed up as user1a
# The USERFILE would connect user1a to @User1 and so whenever someone thanks user1a, they are essentially thanking User1
# Please note, this utilizes the api, so in order for user1a to connect to User1, they must first send a message to the bot
# requesting that the connection be made. @User1 on TwitterThank.com will receive a message in their dashboard
# asking to confirm the connection on the IRC network with the corresponding username.
# If confirmed, the connection will be made within the file.
# Please note, you should not add the connection manually as this will result in error within the api, and when a user
# Tries to thank User1 for example, it will return an error message ("Could not thank user. #102930")
# !-- End of spiel. Short form - Userfile connects aliases and do not manually edit this file!
# Options
# The default is data/users.xml
# If you would like to change this, do so here
USERFILE = "data/users.xml"

# <IRCUSERNAME> - The username the irc bot will use
# You should register this username, so no one else can take it, and make the ircbot admin on the channel
# See IRCPASSWORD below
IRCUSERNAME = "TTBOT-1292" # Change this, for example, to "YOURCHANNEL-TTBOT"

# <IRCPASSWORD> - The password for the irc bot
# See IRCUSERNAME
IRCPASSWORD = "f9dusjfio312hio12hn" # Giberish ... after setting up the account, change this.

# <AUTHCOMMAND> The command to authenticate on the server
# Leave this blank if not a custom server
AUTHCOMMAND = ""
# Custom
# AUTHCOMMAND = "!register ||username|| ||password||"
# We use "||" to show variables

# <LISTENTYPE> - Should the bot listen for private messages or !ttbot [command]
# Choose "private" for private messages and "public" for !ttbot
LISTENTYPE = "private"

# Finished!
# Thank you for choosing TTBOT and TwitterThank





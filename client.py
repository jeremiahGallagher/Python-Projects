# Distributed Computing With Python
# Jeremiah Gallagher
# CSIS 354: Week 5

# client.py
import xmlrpc.client
import sys

# test for the correct amount of arguments in command line call
if len(sys.argv) < 2:
    print("You did not provide the server, port, or input numbers!")
    exit(1)
elif len(sys.argv) < 3:
    print("You did not provide the port or input numbers!")
    exit(1)
elif len(sys.argv) < 4:
    print("you did not provide the input numbers!")
    exit(1)
elif len(sys.argv) > 5:
    print("you provided too many arguments!")
    exit(1)


serverName = sys.argv[1]                                        # capture server name from command line
serverPort = int(sys.argv[2])                                   # capture server port from command line
urlString = "http://"+serverName+":"+str(serverPort)+"/"        # combine name and port to make URL
x = int(sys.argv[3])                                            # capture first test argument from command line
y = int(sys.argv[4])                                            # capture second test argument from command line

# define help in client code ***I couldn't get the server code to recognize the system argument***
def help():
    available = proxy.system.listMethods()
    return available


# Create instance of the client proxyServer, using the URL of the server from command line
# and then call all of the math functions, followed by serverTime function, name function and help
with xmlrpc.client.ServerProxy(urlString) as proxy:
    print(str(x)+" / " + str(y) + " = " + str(proxy.divide(x, y)))
    print(str(x)+" + " + str(y) + " = " + str(proxy.add(x, y)))
    print(str(x)+" * " + str(y) + " = " + str(proxy.multiply(x, y)))
    print(str(x) + " - " + str(y) + " = " + str(proxy.subtract(x, y)))
    print(str(x)+" / " + str(y) + " = " + str(proxy.divide(x, y)))
    print("time:", proxy.serverTime())
    print(proxy.name())
    print(help())

# Distributed Computing With Python
# Jeremiah Gallagher
# CSIS 354: Week 5

# server.py
from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
import sys

# test for the correct amount of arguments in command line call
if len(sys.argv) < 2:
    print("You did not provide the server and port!")
    exit(1)
elif len(sys.argv) < 3:
    print("You did not provide the port number!")
    exit(1)
elif len(sys.argv) > 3:
    print("you provided too many arguments!")
    exit(1)


# define the singleton class, which uses the singleton design pattern
class Singleton:

    def __init__(self, cls):
        self._instance = self._cls()
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


serverName = sys.argv[1]                               # capture the server name from the command line
serverPort = int(sys.argv[2])                          # capture the port name from the command line

# assign the singleton class to the server object on creation
server = SimpleXMLRPCServer((serverName, serverPort)).instance()  # create the server with the name and port provided


# define all of the functions that will be available for client use
def name():
    """
    returns the name of the server
    """
    return serverName


def serverTime():
    """
    returns the current time on the server
    """
    now = datetime.now()                     # capture current time
    time = now.strftime("%H:%M:%S")          # format current time
    return time                              # return the current time


def add(x, y):
    """
    adds x and y and returns the result
    """
    return x + y


def subtract(x, y):
    """
    subtracts y from x and returns the result
    """
    return x - y


def multiply(x, y):
    """
    multiplies x and y and returns the result
    """
    return x * y


def divide(x, y):
    """
    divides x by y and returns the result
    """
    if y == 0:
        return "You cannot divide by 0"           # keeps a black hole from being formed
    else:
        return x / y


print("Listening on port " + str(serverPort) + "...")  # let user know the server is running

# ...Register Functions for Use by Clients...
server.register_introspection_functions()         # used for listing available methods, help, etc.
server.register_function(name, 'name')
server.register_function(serverTime, 'serverTime')
server.register_function(add, 'add')  # ...
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')

server.serve_forever()  # tell the server to run indefinitely

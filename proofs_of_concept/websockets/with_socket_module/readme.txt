This is a basic proof of concept for a websocket server and client.

There are two files:

server.py -- this is the socket server
client.py -- this is the socket client.

In order to run the files you will need to know the IP address of
the machine you will run the server on. Each file contains two constants
immediately after module imports: IP_ADDRESS and PORT.

IP_ADDRESS    will need to be changed to the IP address of the machine you will
              run the server on.
PORT          can be left alone unless it conflicts with a service you are arleady
              running or just want to change it for some reason. 

RUN FROM COMMAND LINE:
  'python3 server.py'
  'python3 client.py'   NOTE: you will need two terminal windows if running on the
                              same machine.
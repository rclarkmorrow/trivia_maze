import socket
from _thread import *

# Configure server.
IP_ADDRESS = '10.0.0.38'  # Put actual IP address here (use local network IP
                          # for testing).
PORT = 11235
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Launch server.
print('Initializing server.')

try:
    SERVER.bind((IP_ADDRESS, PORT))
except socket.error as error:
    print(error)

SERVER.listen(3)  # the argument is the max number of allowed connections.
print('Server is running: waiting for a connection.')

# A threaded client for each connection to the server
def threaded_client(connection, address):
    connection.send(str.encode(f'Connection opened to: {IP_ADDRESS}'))
    while True:
        try:
            payload = connection.recv(2048*2)
            # Decode request from a bytes object.
            request = payload.decode('utf-8')

            if not request:
                break
            else:
                response = f'Server received: \'{request}\', ROCK!!'
                print(f'Received a request: {request}')
                print(f'Sending response  : {response}')
            # Encode response into a bytes object.
            connection.sendall(str.encode(response))

        except Exception as error:
            print(error)

    print(f'Lost connection to: {address}')
    connection.close()


if __name__ == '__main__':
    # Server listens for and accepts incoming connections, passing them
    # into the client function.
    while True:
        connection, address = SERVER.accept()
        print(f'Server connected to: {address}.')
        start_new_thread(threaded_client, (connection, address))
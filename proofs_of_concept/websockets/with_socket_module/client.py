import socket

# Configure server address.
IP_ADDRESS = '10.0.0.38'
PORT = 11235

class NetworkClient:
    def __init__(self):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_ip = IP_ADDRESS
        self.__port = PORT
        self.__address = (self.__server_ip, self.__port)
        self.__client_id = self.connect()
        # Print client_id to verify connection.
        print(self.__client_id)

    @property
    def client(self):
        """ Returns client as property."""
        return self.__client

    @property
    def server_ip(self):
        """ Returns server ip as property."""
        return self.__server_ip

    @property
    def port(self):
        """ Returns port as property."""
        return self.__port

    @property
    def address(self):
        """ Returns address as property."""
        return self.__address

    @property
    def client_id(self):
        """ Returns cid as property."""
        return self.__client_id

    def connect(self):
        """ Connects to the server, returns connection response. """
        try:
            self.__client.connect(self.__address)
            return self.__client.recv(2048 * 2).decode()
        except socket.error as error:
            print(error)

    def send_and_receive(self, payload):
        """ Sends payload to server, receives and returns response."""
        try:
            self.__client.send(str.encode(payload))
            return self.__client.recv(2048 * 2).decode()
        except socket.error as error:
            print(error)


if __name__ == '__main__':
    client = NetworkClient()
    # Send a loop of requests to server.
    for iteration in range(200):
        payload = f'Hello #{iteration}'
        response = client.send_and_receive(payload)
        print(f'Received response: {response}')



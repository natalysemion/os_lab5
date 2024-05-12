import socket
import sys
import time

def f(x):

    return str(x)

def g(x):

    return str(x*x)

def main():
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('Starting up on %s port %s' % server_address)
    server.bind(server_address)

    # Listen for incoming connections
    server.listen(1)

    while True:
        # Wait for a connection
        print('Waiting for a connection')
        connection, client_address = server.accept()

        try:
            print('Connection from', client_address)

            # Receive the data in small chunks and retransmit it
            data = connection.recv(1024).decode()

            if data:
                # Perform computation based on the received data
                f_result = f(float(data))
                g_result = g(float(data))

                # Send the results back to the client
                connection.sendall(f_result.encode())
                connection.sendall(g_result.encode())
            else:
                print('No more data from', client_address)
                break

        finally:
            # Clean up the connection
            connection.close()

if __name__ == '__main__':
    main()

import socket
import sys
import time

def main():
    x = float(input("Enter the value of x: "))

    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print('Connecting to %s port %s' % server_address)
    sock.connect(server_address)

    try:
        # Send the value of x to the server
        message = str(x)
        sock.sendall(message.encode())

        # Receive results from server
        f_res = sock.recv(1024).decode()
        g_res = sock.recv(1024).decode()
        f_result = bool(f_res)
        g_result = bool(g_res)
        print( "f_result = " + str(f_result))
        print("g_result = " + str(g_result))
        if f_result:
            result = f_result
        elif g_result:
            result = g_result
        else:
            result = f_result or g_result

        print("Result of f(x) || g(x):", result)

    finally:
        print('Closing socket')
        sock.close()

if __name__ == '__main__':
    main()

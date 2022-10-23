import socket

if __name__ == '__main__':
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSock.connect("http://www.baidu.com/")

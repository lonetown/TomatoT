import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror) as e:
        print("Error: cannot reach %s" % HOST)
       return
    print('*** connected to host "%s"' % HOST)


    pass


if __name__ == '__main__':
    main()

import socket
from time import sleep
from contextlib import closing


def check_host(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(3)
        if sock.connect_ex((host, port)) == 0:
            return True
        else:
            return False
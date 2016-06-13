import socket
if __name__ == "__main__":
    host_name = socket.gethostname()
    address = socket.gethostbyname("www.baidu.com")
    print host_name,address